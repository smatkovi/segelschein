#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zeichnet die Schemata für den Segelschein.

Zeichnungen statt Fotos, aus demselben Grund wie beim Segelflug: Ein Foto
zeigt ein bestimmtes Boot bei bestimmtem Licht, und das Merkmal liegt
irgendwo darin. Eine Zeichnung zeigt das Merkmal und sonst nichts.

Alles wird bei 3x gezeichnet und am Ende verkleinert.

    tools/bilder.py            # -> bilder/*.png
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "bilder")

W, H = 440, 340
S = 3

WASSER = (28, 62, 96)
HIMMEL = (16, 22, 34)
RUMPF = (232, 236, 244)
RUMPF_DUNKEL = (150, 158, 176)
SEGEL = (248, 250, 255)
SEGEL_SCHATTEN = (196, 204, 220)
LINIE = (120, 130, 150)
TEXT = (226, 230, 240)
BETONT = (90, 169, 255)
WARN = (255, 177, 78)
GUT = (126, 231, 135)
ROT = (226, 74, 74)
GRUEN = (60, 190, 90)


def schrift(groesse):
    for pfad in ("/usr/share/fonts/dejavu/DejaVuSans.ttf",
                 "/usr/share/fonts/dejavu/DejaVuSansCondensed.ttf"):
        if os.path.exists(pfad):
            return ImageFont.truetype(pfad, groesse)
    return ImageFont.load_default()


def leinwand(farbe=HIMMEL):
    bild = Image.new("RGB", (W * S, H * S), farbe)
    return bild, ImageDraw.Draw(bild)


def sichern(bild, name):
    os.makedirs(OUT, exist_ok=True)
    klein = bild.resize((W, H), Image.LANCZOS)
    klein.save(os.path.join(OUT, name + ".png"))
    print("  %s" % name)


def text(draw, x, y, inhalt, groesse=13, farbe=TEXT, mitte=False):
    f = schrift(groesse * S)
    if mitte:
        kasten = draw.textbbox((0, 0), inhalt, font=f)
        x -= (kasten[2] - kasten[0]) / 2
    draw.text((x, y), inhalt, font=f, fill=farbe)


def boot(draw, cx, cy, winkel, laenge=46, segel_seite=1, farbe=RUMPF,
         segel=True):
    """Ein Boot von oben. winkel = Fahrtrichtung in Grad, 0 = nach oben."""
    a = math.radians(winkel)
    def dreh(dx, dy):
        return (cx + dx * math.cos(a) - dy * math.sin(a),
                cy + dx * math.sin(a) + dy * math.cos(a))

    L = laenge * S
    B = L * 0.30
    rumpf = [dreh(0, -L * 0.55),            # Bug
             dreh(B * 0.5, -L * 0.15),
             dreh(B * 0.42, L * 0.45),
             dreh(-B * 0.42, L * 0.45),
             dreh(-B * 0.5, -L * 0.15)]
    draw.polygon(rumpf, fill=farbe, outline=RUMPF_DUNKEL)

    if not segel:
        return
    # Grosssegel als Dreieck vom Mast nach achtern, zur Leeseite ausgestellt
    mast = dreh(0, -L * 0.10)
    ausschlag = segel_seite * L * 0.42
    spitze = dreh(ausschlag, L * 0.40)
    bauch = dreh(ausschlag * 0.62, L * 0.14)
    draw.polygon([mast, bauch, spitze], fill=SEGEL, outline=SEGEL_SCHATTEN)
    draw.line([mast, spitze], fill=SEGEL_SCHATTEN, width=int(1.4 * S))


def windpfeil(draw, x, y, laenge, winkel=180, farbe=BETONT, dick=3):
    """Pfeil in Windrichtung (wohin er weht)."""
    a = math.radians(winkel)
    x2 = x + laenge * math.sin(a)
    y2 = y - laenge * math.cos(a)
    draw.line([(x, y), (x2, y2)], fill=farbe, width=int(dick * S))
    for seite in (-1, 1):
        b = a + seite * math.radians(155)
        draw.line([(x2, y2), (x2 + 12 * S * math.sin(b),
                              y2 - 12 * S * math.cos(b))],
                  fill=farbe, width=int(dick * S))


# ---------------------------------------------------------------------------

def kurse_zum_wind():
    """Das wichtigste Diagramm im Segelsport.

    Der Wind kommt von oben. Rundherum die Kurse, in der Mitte die
    Sperrzone, in die kein Segelboot fahren kann.
    """
    bild, draw = leinwand()
    # Mitte etwas hoch und Radius knapp, damit auch die unterste
    # Beschriftung ("Vor dem Wind") noch ins Bild passt.
    cx, cy = W * S * 0.5, H * S * 0.50
    r = H * S * 0.27

    # Sperrzone: rund 45 Grad zu beiden Seiten der Windrichtung
    draw.pieslice([cx - r * 1.28, cy - r * 1.28, cx + r * 1.28, cy + r * 1.28],
                  -135, -45, fill=(52, 40, 40))
    text(draw, cx, cy - r * 1.18, "Sperrzone", 13, (200, 150, 150), mitte=True)

    windpfeil(draw, cx, H * S * 0.07, H * S * 0.10, 180, BETONT, 3)
    text(draw, cx + 14 * S, H * S * 0.055, "Wind", 14, BETONT)

    # Kurse: (Peilung des Bootes, Name, auf welcher Seite steht das Segel)
    kurse = [(45, "Am Wind", -1), (-45, "Am Wind", 1),
             (90, "Halber Wind", -1), (-90, "Halber Wind", 1),
             (135, "Raumschots", -1), (-135, "Raumschots", 1),
             (180, "Vor dem Wind", -1)]
    for peilung, name, seite in kurse:
        a = math.radians(peilung)
        bx = cx + r * math.sin(a)
        by = cy - r * math.cos(a)
        boot(draw, bx, by, peilung, 42, seite)
        # Die Beschriftung nach aussen, aber seitlich hereingezogen, damit
        # sie weder das Boot verdeckt noch aus dem Bild laeuft.
        tx = cx + (r + 40 * S) * math.sin(a) * 1.25
        ty = cy - (r + 40 * S) * math.cos(a)
        tx = max(52 * S, min(W * S - 52 * S, tx))
        ty = max(H * S * 0.12, min(H * S - 22 * S, ty))
        text(draw, tx, ty - 7 * S, name, 12, TEXT, mitte=True)

    sichern(bild, "kurse-zum-wind")


def bootsteile():
    """Die Teile, nach denen in der Prüfung gefragt wird."""
    bild, draw = leinwand()
    cx, cy = W * S * 0.40, H * S * 0.60

    # Rumpf im Profil
    draw.polygon([(cx - 110 * S, cy), (cx + 120 * S, cy),
                  (cx + 96 * S, cy + 26 * S), (cx - 86 * S, cy + 26 * S)],
                 fill=RUMPF, outline=RUMPF_DUNKEL)
    # Schwert
    draw.polygon([(cx - 14 * S, cy + 26 * S), (cx + 14 * S, cy + 26 * S),
                  (cx + 8 * S, cy + 72 * S), (cx - 8 * S, cy + 72 * S)],
                 fill=RUMPF_DUNKEL)
    # Ruderblatt
    draw.polygon([(cx - 106 * S, cy + 20 * S), (cx - 92 * S, cy + 20 * S),
                  (cx - 94 * S, cy + 60 * S), (cx - 104 * S, cy + 60 * S)],
                 fill=RUMPF_DUNKEL)
    # Mast und Baum
    draw.line([(cx + 34 * S, cy), (cx + 34 * S, cy - 190 * S)],
              fill=RUMPF_DUNKEL, width=int(4 * S))
    draw.line([(cx + 34 * S, cy - 14 * S), (cx - 70 * S, cy - 6 * S)],
              fill=RUMPF_DUNKEL, width=int(4 * S))
    # Grosssegel
    draw.polygon([(cx + 32 * S, cy - 186 * S), (cx + 32 * S, cy - 14 * S),
                  (cx - 68 * S, cy - 8 * S)], fill=SEGEL,
                 outline=SEGEL_SCHATTEN)
    # Fock
    draw.polygon([(cx + 36 * S, cy - 180 * S), (cx + 36 * S, cy - 10 * S),
                  (cx + 118 * S, cy - 2 * S)], fill=(238, 242, 250),
                 outline=SEGEL_SCHATTEN)

    marken = [((cx + 34 * S, cy - 200 * S), "Mast", 0, -14),
              ((cx - 20 * S, cy - 96 * S), "Großsegel", 0, 0),
              ((cx + 78 * S, cy - 86 * S), "Fock", 0, 0),
              ((cx - 40 * S, cy - 2 * S), "Baum", 0, 10),
              ((cx + 120 * S, cy + 6 * S), "Bug", 6, 0),
              ((cx - 112 * S, cy + 6 * S), "Heck", -34, 0),
              ((cx, cy + 78 * S), "Schwert", 0, 6),
              ((cx - 100 * S, cy + 64 * S), "Ruder", -20, 6)]
    for (px, py), name, dx, dy in marken:
        text(draw, px + dx * S, py + dy * S, name, 12, BETONT, mitte=True)

    windpfeil(draw, W * S * 0.86, H * S * 0.20, H * S * 0.09, 250, BETONT, 2)
    text(draw, W * S * 0.80, H * S * 0.10, "Wind", 12, BETONT)
    text(draw, W * S * 0.06, H * S * 0.12, "Luv", 13, WARN)
    text(draw, W * S * 0.06, H * S * 0.18, "(Windseite)", 10, LINIE)
    text(draw, W * S * 0.86, H * S * 0.74, "Lee", 13, WARN)
    text(draw, W * S * 0.80, H * S * 0.80, "(windabgewandt)", 10, LINIE)
    sichern(bild, "bootsteile")


def ausweichen():
    """Die drei Regeln, die in jeder Prüfung drankommen."""
    bild, draw = leinwand()
    draw.rectangle([0, H * S * 0.33, W * S, H * S * 0.34], fill=(40, 46, 60))
    draw.rectangle([0, H * S * 0.66, W * S, H * S * 0.67], fill=(40, 46, 60))

    # 1: Backbordbug weicht Steuerbordbug aus
    y = H * S * 0.16
    windpfeil(draw, W * S * 0.5, H * S * 0.03, H * S * 0.05, 180, BETONT, 2)
    boot(draw, W * S * 0.24, y, 60, 38, -1)
    boot(draw, W * S * 0.62, y, -60, 38, 1)
    text(draw, W * S * 0.24, y + 34 * S, "Backbordbug", 11, ROT, mitte=True)
    text(draw, W * S * 0.62, y + 34 * S, "Steuerbordbug", 11, GUT, mitte=True)
    text(draw, W * S * 0.80, y - 10 * S, "weicht aus →", 11, ROT)

    # 2: Luv weicht Lee aus
    y = H * S * 0.49
    boot(draw, W * S * 0.28, y - 16 * S, 90, 38, -1)
    boot(draw, W * S * 0.28, y + 22 * S, 90, 38, -1)
    text(draw, W * S * 0.46, y - 24 * S, "Luv: weicht aus", 11, ROT)
    text(draw, W * S * 0.46, y + 14 * S, "Lee: Vorrang", 11, GUT)

    # 3: Segel vor Motor
    y = H * S * 0.82
    boot(draw, W * S * 0.26, y, 90, 40, -1)
    boot(draw, W * S * 0.66, y, -90, 40, 1, farbe=(190, 130, 90), segel=False)
    draw.ellipse([W * S * 0.70, y - 6 * S, W * S * 0.73, y + 6 * S],
                 fill=(150, 150, 160))
    text(draw, W * S * 0.26, y + 32 * S, "Segel: Vorrang", 11, GUT, mitte=True)
    text(draw, W * S * 0.66, y + 32 * S, "Motor: weicht aus", 11, ROT, mitte=True)
    sichern(bild, "ausweichen")


def wende_halse():
    """Der Unterschied, der Köpfe kostet."""
    bild, draw = leinwand()
    windpfeil(draw, W * S * 0.5, H * S * 0.04, H * S * 0.07, 180, BETONT, 2)

    # Wende: durch den Wind, Bug dreht durch die Sperrzone
    cy = H * S * 0.30
    boot(draw, W * S * 0.20, cy + 30 * S, 45, 36, -1)
    boot(draw, W * S * 0.35, cy, 0, 36, -1, farbe=(200, 206, 220))
    boot(draw, W * S * 0.50, cy + 30 * S, -45, 36, 1)
    draw.arc([W * S * 0.16, cy - 6 * S, W * S * 0.54, cy + 66 * S],
             200, 340, fill=GUT, width=int(2 * S))
    text(draw, W * S * 0.70, cy + 4 * S, "Wende", 14, GUT)
    text(draw, W * S * 0.70, cy + 24 * S, "Bug durch den Wind,", 11, TEXT)
    text(draw, W * S * 0.70, cy + 40 * S, "langsam, ungefährlich", 11, TEXT)

    # Halse: Heck durch den Wind, Baum schlägt herüber
    cy = H * S * 0.72
    boot(draw, W * S * 0.20, cy - 26 * S, 135, 36, -1)
    boot(draw, W * S * 0.35, cy + 6 * S, 180, 36, -1, farbe=(200, 206, 220))
    boot(draw, W * S * 0.50, cy - 26 * S, -135, 36, 1)
    draw.arc([W * S * 0.16, cy - 62 * S, W * S * 0.54, cy + 22 * S],
             20, 160, fill=WARN, width=int(2 * S))
    text(draw, W * S * 0.70, cy - 22 * S, "Halse", 14, WARN)
    text(draw, W * S * 0.70, cy - 2 * S, "Heck durch den Wind,", 11, TEXT)
    text(draw, W * S * 0.70, cy + 14 * S, "Baum schlägt herüber:", 11, TEXT)
    text(draw, W * S * 0.70, cy + 30 * S, "Köpfe einziehen", 11, WARN)
    sichern(bild, "wende-halse")


def betonnung():
    """Backbord rot, Steuerbord grün — von See kommend."""
    bild, draw = leinwand(WASSER)
    draw.rectangle([0, 0, W * S, H * S * 0.14], fill=HIMMEL)
    text(draw, W * S * 0.5, H * S * 0.03, "Fahrwasser, von See kommend",
         13, TEXT, mitte=True)

    # Fahrwasser
    draw.polygon([(W * S * 0.30, H * S * 1.0), (W * S * 0.70, H * S * 1.0),
                  (W * S * 0.58, H * S * 0.16), (W * S * 0.42, H * S * 0.16)],
                 fill=(38, 82, 126))

    for i, y in enumerate((0.30, 0.52, 0.76)):
        t = (y - 0.16) / 0.84
        links = W * S * (0.42 - 0.12 * t) - 26 * S
        rechts = W * S * (0.58 + 0.12 * t) + 26 * S
        yy = H * S * y
        groesse = (14 + 8 * t) * S
        # Backbord: rot, stumpf (Zylinder)
        draw.rectangle([links - groesse * 0.5, yy - groesse,
                        links + groesse * 0.5, yy + groesse * 0.4], fill=ROT)
        # Steuerbord: gruen, spitz (Kegel)
        draw.polygon([(rechts, yy - groesse * 1.1),
                      (rechts + groesse * 0.6, yy + groesse * 0.4),
                      (rechts - groesse * 0.6, yy + groesse * 0.4)], fill=GRUEN)
        if i == 1:
            text(draw, links, yy + groesse * 0.9, "Backbord", 11, ROT, mitte=True)
            text(draw, links, yy + groesse * 1.9, "rot, stumpf", 10, LINIE, mitte=True)
            text(draw, rechts, yy + groesse * 0.9, "Steuerbord", 11, GRUEN, mitte=True)
            text(draw, rechts, yy + groesse * 1.9, "grün, spitz", 10, LINIE, mitte=True)

    boot(draw, W * S * 0.5, H * S * 0.88, 0, 40, -1)
    sichern(bild, "betonnung")


def lichter():
    """Was man nachts sieht und was es bedeutet."""
    bild, draw = leinwand()
    text(draw, W * S * 0.5, H * S * 0.04, "Lichterführung von vorn",
         13, TEXT, mitte=True)

    faelle = [(0.30, "Segelboot unter Segel", [(-1, ROT), (1, GRUEN)], None),
              (0.58, "Maschinenfahrzeug", [(-1, ROT), (1, GRUEN)],
               (0, (250, 250, 240))),
              (0.86, "Boot unter 7 m: ein weißes Rundumlicht", [], 
               (0, (250, 250, 240)))]
    for y, name, seiten, topp in faelle:
        yy = H * S * y
        cx = W * S * 0.30
        boot(draw, cx, yy, 180, 40, -1, segel=(topp is None))
        for seite, farbe in seiten:
            draw.ellipse([cx + seite * 17 * S - 5 * S, yy - 5 * S,
                          cx + seite * 17 * S + 5 * S, yy + 5 * S], fill=farbe)
        if topp:
            draw.ellipse([cx - 5 * S, yy - 26 * S, cx + 5 * S, yy - 16 * S],
                         fill=topp[1])
        text(draw, W * S * 0.46, yy - 8 * S, name, 12, TEXT)
    text(draw, W * S * 0.46, H * S * 0.66, "weißes Topplicht dazu", 10, LINIE)
    text(draw, W * S * 0.10, H * S * 0.16, "rot = Backbord", 11, ROT)
    text(draw, W * S * 0.55, H * S * 0.16, "grün = Steuerbord", 11, GRUEN)
    sichern(bild, "lichter")


def main():
    print("Bilder:")
    kurse_zum_wind()
    bootsteile()
    ausweichen()
    wende_halse()
    betonnung()
    lichter()


if __name__ == "__main__":
    main()
