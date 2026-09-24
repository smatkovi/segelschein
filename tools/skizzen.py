#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zeichnet die Skizzen zu den Herleitungen.

Eine Herleitung ist eine Kette von Saetzen, und an genau einer Stelle
haengt sie an einem Bild: dem Kraeftedreieck, der schiefen Ebene, der
Luftsaeule. Wer das Bild vor sich hat, liest die Rechnung als Beschreibung
dessen, was er sieht; wer es nicht hat, muss es sich nebenher bauen -- und
verliert dabei den Faden.

Gezeichnet wird schematisch, nicht abbildend: Ein Boot ist hier ein
Strich mit Mast, weil es auf die Winkel ankommt und nicht auf den Rumpf. Alles bei 3x und am Ende verkleinert, sonst treppen die Schraegen.

Die Beschriftung steckt im Bild, also gibt es jede Skizze zweimal:
<name>.png und <name>.en.png. Welche gezeigt wird, entscheidet die App.

    tools/skizzen.py            # -> bilder/skizze-*.png
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "bilder")

W, H = 440, 300
S = 3

GRUND = (14, 14, 18)
LINIE = (120, 130, 150)
DUENN = (70, 78, 94)
TEXT = (226, 230, 240)
BETONT = (90, 169, 255)
WARN = (255, 177, 78)
GUT = (126, 231, 135)
ROT = (226, 74, 74)
KOERPER = (232, 236, 244)

SPRACHE = "de"

EN = {
    "Wasserlinie": "waterline",
    "Grund": "seabed",
    "Wassertiefe + Freibord": "depth + freeboard",
    "gesteckte Länge": "scope",
    "Zugwinkel": "angle of pull",
    "flach ziehen heißt eingraben": "a flat pull digs in",
    "Wind": "wind",
    "Ziel": "target",
    "gesegelter Weg": "distance sailed",
    "Luftlinie": "straight line",
    "Kurs zum Wind": "course to the wind",
    "Segelfläche": "sail area",
    "doppelter Wind": "twice the wind",
    "vierfache Kraft": "four times the force",
    "Blitz": "lightning",
    "Donner": "thunder",
    "Schall: 343 m/s": "sound: 343 m/s",
    "Licht: sofort da": "light: there at once",
    "Sekunden zählen": "count the seconds",
}


def schrift(groesse):
    for pfad in ("/usr/share/fonts/dejavu/DejaVuSans.ttf",
                 "/usr/share/fonts/TTF/DejaVuSans.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(pfad):
            return ImageFont.truetype(pfad, groesse)
    return ImageFont.load_default()


def leinwand():
    bild = Image.new("RGB", (W * S, H * S), GRUND)
    return bild, ImageDraw.Draw(bild)


def sichern(bild, name):
    os.makedirs(OUT, exist_ok=True)
    if SPRACHE != "de":
        name = name + "." + SPRACHE
    bild.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, name + ".png"))
    print("  %s" % name)


def text(draw, x, y, inhalt, groesse=13, farbe=TEXT, mitte=False, rechts=False):
    if SPRACHE != "de":
        inhalt = EN.get(inhalt, inhalt)
    f = schrift(groesse * S)
    # Die Breite kommt in Geraetepunkten (die Schrift ist S-fach gross),
    # x und y sind in Zeicheneinheiten -- also erst umrechnen, sonst rueckt
    # der Text dreimal zu weit nach links und faellt aus dem Bild.
    kasten = draw.textbbox((0, 0), inhalt, font=f)
    breite = (kasten[2] - kasten[0]) / float(S)
    if mitte:
        x -= breite / 2.0
    elif rechts:
        x -= breite
    draw.text((x * S, y * S), inhalt, font=f, fill=farbe)


def strich(draw, x1, y1, x2, y2, farbe=LINIE, dicke=2):
    draw.line([(x1 * S, y1 * S), (x2 * S, y2 * S)], fill=farbe, width=dicke * S)


def gestrichelt(draw, x1, y1, x2, y2, farbe=DUENN, dicke=1, laenge=6):
    weite = math.hypot(x2 - x1, y2 - y1)
    if weite <= 0:
        return
    schritte = max(1, int(weite / laenge))
    for i in range(schritte):
        if i % 2:
            continue
        a, b = i / float(schritte), min(1.0, (i + 1) / float(schritte))
        strich(draw, x1 + (x2 - x1) * a, y1 + (y2 - y1) * a,
               x1 + (x2 - x1) * b, y1 + (y2 - y1) * b, farbe, dicke)


def pfeil(draw, x1, y1, x2, y2, farbe=BETONT, dicke=2, spitze=7):
    strich(draw, x1, y1, x2, y2, farbe, dicke)
    winkel = math.atan2(y2 - y1, x2 - x1)
    for seite in (+1, -1):
        a = winkel + seite * 2.6
        strich(draw, x2, y2, x2 + spitze * math.cos(a), y2 + spitze * math.sin(a),
               farbe, dicke)


def bogen(draw, cx, cy, r, von, bis, farbe=DUENN, dicke=1):
    """Winkelbogen; die Winkel in Grad, 0 ist rechts, positiv im Uhrzeigersinn."""
    draw.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
             von, bis, fill=farbe, width=dicke * S)


# ---------------------------------------------------------------------------
# b-teile: die Geometrie der Ankerkette
# ---------------------------------------------------------------------------
def anker():
    bild, draw = leinwand()
    wasser, grund = 92, 214
    draw.rectangle([0, wasser * S, W * S, grund * S], fill=(22, 44, 68))
    strich(draw, 0, wasser, W, wasser, (90, 140, 190), 1)
    strich(draw, 0, grund, W, grund, (86, 78, 60), 2)
    text(draw, 8, wasser - 16, "Wasserlinie", 10, DUENN)
    text(draw, 8, grund + 6, "Grund", 10, DUENN)

    # Boot rechts oben, Klampe am Bug
    bx, by = 330, wasser
    draw.polygon([((bx - 40) * S, by * S), ((bx + 40) * S, by * S),
                  ((bx + 26) * S, (by - 14) * S), ((bx - 30) * S, (by - 14) * S)],
                 fill=KOERPER)
    strich(draw, bx, by - 14, bx, by - 54, KOERPER, 2)
    kx, ky = bx - 30, by - 12

    # Kette zum Anker unten links
    ax, ay = 120, grund
    strich(draw, kx, ky, ax, ay, BETONT, 2)
    draw.polygon([(ax * S, ay * S), ((ax - 10) * S, (ay - 16) * S),
                  ((ax + 10) * S, (ay - 16) * S)], fill=WARN)

    # Tiefe und Laenge
    gestrichelt(draw, kx, ky, kx, grund)
    pfeil(draw, kx + 16, ky, kx + 16, grund, GUT, 1)
    pfeil(draw, kx + 16, grund, kx + 16, ky, GUT, 1)
    text(draw, kx + 22, (ky + grund) / 2 - 16, "T", 13, GUT)
    text(draw, kx + 22, (ky + grund) / 2, "Wassertiefe + Freibord", 10, GUT)
    text(draw, (kx + ax) / 2 - 10, (ky + ay) / 2 - 24, "L", 13, BETONT)
    text(draw, (kx + ax) / 2 - 10, (ky + ay) / 2 - 8, "gesteckte Länge", 10, BETONT)

    bogen(draw, ax, ay, 46, -math.degrees(math.atan2(ay - ky, kx - ax)), 0, WARN, 1)
    text(draw, ax + 52, ay - 22, "α", 13, WARN)
    text(draw, ax + 54, ay - 38, "Zugwinkel", 10, WARN)
    text(draw, 150, 222, "flach ziehen heißt eingraben", 10, DUENN)

    text(draw, 22, 240, "sin α = T / L    →    L = T / sin α", 13, GUT)
    text(draw, 22, 262, "20°: L = 2,9 × T      12°: L = 4,8 × T", 11, TEXT)
    text(draw, 22, 280, "daher: drei- bis fünffache Wassertiefe", 11, TEXT)
    sichern(bild, "skizze-anker")


# ---------------------------------------------------------------------------
# k-kurse: warum aus 6 km gut 8,5 werden
# ---------------------------------------------------------------------------
def kreuzen():
    bild, draw = leinwand()
    # Wind kommt von oben, das Ziel liegt genau gegen den Wind
    pfeil(draw, 220, 30, 220, 66, WARN, 2)
    text(draw, 230, 38, "Wind", 12, WARN)

    sx, sy = 220, 246          # Start
    zx, zy = 220, 92           # Ziel
    gestrichelt(draw, sx, sy, zx, zy, DUENN)
    draw.ellipse([(zx - 5) * S, (zy - 5) * S, (zx + 5) * S, (zy + 5) * S], fill=GUT)
    text(draw, zx + 10, zy - 8, "Ziel", 11, GUT)
    text(draw, sx - 10, (sy + zy) / 2 - 8, "d", 13, DUENN, rechts=True)
    text(draw, sx - 10, (sy + zy) / 2 + 8, "Luftlinie", 10, DUENN, rechts=True)

    # Vier Schlaege unter 45 Grad
    punkte = [(sx, sy)]
    hoehe = (sy - zy) / 4.0
    for i in range(4):
        x, y = punkte[-1]
        dx = hoehe if i % 2 == 0 else -hoehe
        punkte.append((x + dx, y - hoehe))
    for (x1, y1), (x2, y2) in zip(punkte, punkte[1:]):
        pfeil(draw, x1, y1, x2, y2, BETONT, 2, 6)
    text(draw, punkte[1][0] + 10, punkte[1][1] - 24, "s", 13, BETONT)
    text(draw, punkte[1][0] + 22, punkte[1][1] - 22, "gesegelter Weg", 10, BETONT)

    bogen(draw, sx, sy, 44, -90, -45, WARN, 1)
    text(draw, sx - 14, sy - 52, "β = 45°", 11, WARN, rechts=True)
    text(draw, sx - 14, sy - 36, "Kurs zum Wind", 10, DUENN, rechts=True)

    text(draw, 22, 266, "d = s · cos β    →    s = d / cos 45° = 1,41 · d", 13, GUT)
    text(draw, 22, 286, "unabhängig davon, wie oft man wendet", 10, TEXT)
    sichern(bild, "skizze-kreuzen")


# ---------------------------------------------------------------------------
# w-wind: doppelter Wind, vierfache Kraft
# ---------------------------------------------------------------------------
def staudruck():
    bild, draw = leinwand()
    for spalte, (v, kraft, farbe, beschriftung) in enumerate((
            (1, 1, BETONT, "v"), (2, 4, WARN, "doppelter Wind"))):
        x0 = 60 + spalte * 200
        y0 = 80
        # Segelflaeche als Rechteck
        draw.rectangle([x0 * S, y0 * S, (x0 + 70) * S, (y0 + 96) * S],
                       outline=KOERPER, width=2 * S)
        text(draw, x0 + 35, y0 - 46, "Segelfläche", 10, DUENN, mitte=True)
        text(draw, x0 + 35, y0 - 32, "A", 12, KOERPER, mitte=True)
        # Windpfeile, doppelt so lang
        for i in range(3):
            y = y0 + 20 + i * 28
            pfeil(draw, x0 - 20 - 22 * v, y, x0 - 8, y, farbe, 2, 6)
        text(draw, x0 - 20 - 22 * v, y0 + 110, beschriftung, 10, farbe)
        # Kraftpfeil nach rechts, vierfach
        pfeil(draw, x0 + 72, y0 + 48, x0 + 72 + 22 * kraft, y0 + 48, ROT, 3, 8)
        text(draw, x0 + 76, y0 + 26, "F" if kraft == 1 else "4F", 13, ROT)
    text(draw, 274, 200, "vierfache Kraft", 10, ROT)

    text(draw, 22, 238, "q = ½·ρ·v²      F = q · A · c", 13, GUT)
    text(draw, 22, 260, "F ∝ v²  —  von 4 auf 6 Beaufort ist gut das Vierfache",
         11, TEXT)
    text(draw, 22, 280, "deshalb reffen, bevor es sich nötig anfühlt", 10, DUENN)
    sichern(bild, "skizze-staudruck")


# ---------------------------------------------------------------------------
# w-gewitter: Sekunden zaehlen
# ---------------------------------------------------------------------------
def donner():
    bild, draw = leinwand()
    wasser = 214
    draw.rectangle([0, wasser * S, W * S, H * S], fill=(22, 44, 68))

    # Wolke links mit Blitz
    for (cx, cy, r) in ((70, 70, 30), (104, 62, 36), (140, 72, 28), (118, 84, 30)):
        draw.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
                     fill=(96, 102, 118))
    zacken = [(104, 96), (94, 126), (108, 124), (96, 158)]
    for (x1, y1), (x2, y2) in zip(zacken, zacken[1:]):
        strich(draw, x1, y1, x2, y2, (255, 236, 120), 3)
    text(draw, 60, 168, "Blitz", 11, (255, 236, 120))
    text(draw, 60, 184, "Licht: sofort da", 10, DUENN)

    # Boot rechts
    bx = 366
    draw.polygon([((bx - 26) * S, wasser * S), ((bx + 26) * S, wasser * S),
                  ((bx + 16) * S, (wasser - 12) * S),
                  ((bx - 18) * S, (wasser - 12) * S)], fill=KOERPER)
    strich(draw, bx, wasser - 12, bx, wasser - 52, KOERPER, 2)

    # Schallbögen
    for r in (60, 96, 132, 168):
        draw.arc([(104 - r) * S, (128 - r) * S, (104 + r) * S, (128 + r) * S],
                 -55, 55, fill=DUENN, width=1 * S)
    pfeil(draw, 150, 128, 330, 128, GUT, 2)
    text(draw, 240, 106, "Donner", 12, GUT, mitte=True)
    text(draw, 240, 136, "Schall: 343 m/s", 10, GUT, mitte=True)

    text(draw, 22, 244, "d = c · t      1 km braucht 1000 ÷ 343 ≈ 2,9 s", 12, TEXT)
    text(draw, 22, 266, "d [km] ≈ t [s] / 3   —  Sekunden zählen, durch drei", 13, GUT)
    text(draw, 22, 286, "unter 15 s: keine fünf Kilometer weg", 10, WARN)
    sichern(bild, "skizze-donner")


def main():
    global SPRACHE
    for SPRACHE in ("de", "en"):
        print("Skizzen (%s):" % SPRACHE)
        anker()
        kreuzen()
        staudruck()
        donner()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
