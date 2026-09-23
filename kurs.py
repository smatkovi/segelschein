# -*- coding: utf-8 -*-
"""Segelschein A (Binnen) — Theorie.

Eigene Fragen zum Lehrplan, nicht der amtliche Katalog: Den gibt es für
den A-Schein nicht frei abrufbar, und nachgebaut wäre er weder rechtlich
sauber noch verlässlich. Abgedeckt sind dieselben Fachgebiete.

Deutsch, weil die Prüfung deutsch ist. Das Format trägt Sprachpaare
(siehe ~/ps/segelflug/kurs.py), falls später Englisch dazukommt.
"""
from __future__ import unicode_literals

from herleitungen import HERLEITUNGEN


def mc(q, optionen, antwort, warum, bild=""):
    return {"kind": "mc", "q": q, "optionen": optionen, "antwort": antwort,
            "warum": warum, "bild": bild}


def zahl(q, antwort, einheit, warum, toleranz=0.1, bild=""):
    return {"kind": "zahl", "q": q, "antwort": antwort, "einheit": einheit,
            "warum": warum, "toleranz": toleranz, "bild": bild}


def lektion(ident, titel, begriffe, text, bild, aufgaben):
    # Die Herleitung haengt hinten an. Sie steht nicht im Lektionstext,
    # damit alle Formeln des Kurses an einer Stelle zu ueberblicken sind.
    h = HERLEITUNGEN.get(ident)
    if h:
        text = text + "\n\n" + h
    return {"id": ident, "titel": titel, "begriffe": begriffe, "text": text,
            "bild": bild, "aufgaben": aufgaben}


def kapitel(ident, titel, stufe, blurb, lektionen):
    return {"id": ident, "titel": titel, "stufe": stufe, "text": blurb,
            "lektionen": lektionen}



# ===========================================================================
# 1 -- Das Boot
# ===========================================================================

K_BOOT = kapitel("boot", "Das Boot", 1,
    "Die Begriffe, ohne die kein anderes Kapitel verständlich ist. Wer "
    "Luv und Lee sicher hat, versteht die halbe Prüfung von allein.", [

    lektion("b-teile", "Teile und Richtungen", ["bootsteile", "luv-lee"],
        "**Vorne ist der Bug, hinten das Heck.** In Fahrtrichtung gesehen "
        "ist links **Backbord** (rot) und rechts **Steuerbord** (grün). "
        "Diese beiden Wörter gelten immer vom Boot aus, nie vom Ufer — "
        "deshalb gibt es sie überhaupt.\n\n"
        "Die beiden wichtigsten Wörter im Segelsport sind aber **Luv** und "
        "**Lee**:\n\n"
        "**Luv** ist die Seite, von der der Wind kommt.\n"
        "**Lee** ist die Seite, zu der er weht.\n\n"
        "Merkhilfe: *Lee* wie *leer* — dorthin bläst der Wind alles hin. Das "
        "Segel steht immer in Lee, die Mannschaft sitzt beim Krängen in Luv.\n\n"
        "Am Rumpf: Das **Schwert** (oder der Kiel) wirkt gegen die seitliche "
        "Abdrift, das **Ruder** steuert. Ohne Fahrt durchs Wasser wirkt "
        "keines von beiden — ein stehendes Boot lässt sich nicht steuern.\n\n"
        "Oben: Der **Mast** trägt die Segel, der **Baum** hält das Großsegel "
        "unten, die **Schot** ist die Leine, mit der man ein Segel "
        "dichtholt oder fiert. **Fallen** ziehen Segel nach oben, **Schoten** "
        "nach hinten — wer das verwechselt, sagt es in der Prüfung einmal "
        "und nie wieder.",
        "bootsteile",
        [
            mc("Was bedeutet „Luv\"?",
               ["Die Seite, von der der Wind kommt.",
                "Die Seite, zu der der Wind weht.",
                "Die linke Seite des Bootes.",
                "Die Vorderseite des Bootes."], 0,
               "Luv ist windzugewandt, Lee windabgewandt. Fast alle "
               "Vorfahrtsregeln und Manöverbeschreibungen bauen darauf auf, "
               "deshalb steht es am Anfang.",
               bild="bootsteile"),
            mc("Backbord ist …",
               ["in Fahrtrichtung links, Kennfarbe rot.",
                "in Fahrtrichtung rechts, Kennfarbe grün.",
                "immer die Luvseite.",
                "die Rückseite des Bootes."], 0,
               "Backbord links und rot, Steuerbord rechts und grün — dieselbe "
               "Zuordnung wie bei den Positionslaternen und bei der "
               "Betonnung."),
            mc("Wozu dient das Schwert?",
               ["Es wirkt der seitlichen Abdrift entgegen.",
                "Es steuert das Boot.",
                "Es stabilisiert gegen Krängung.",
                "Es bremst beim Anlegen."], 0,
               "Ohne Schwert oder Kiel würde das Boot vom Wind einfach "
               "seitwärts geschoben. Gesteuert wird mit dem Ruder — und auch "
               "das nur, solange Wasser daran vorbeiströmt.",
               bild="bootsteile"),
            mc("Womit wird ein Segel gesetzt, also nach oben gezogen?",
               ["Mit dem Fall.", "Mit der Schot.", "Mit dem Baum.",
                "Mit dem Niederholer."], 0,
               "Fallen ziehen nach oben, Schoten nach hinten oder zur Seite. "
               "Der Niederholer zieht den Baum nach unten und gehört zur "
               "Trimmerei, nicht zum Setzen."),
        ]),
])


# ===========================================================================
# 2 -- Kurse zum Wind
# ===========================================================================

K_KURSE = kapitel("kurse", "Kurse zum Wind", 2,
    "Wie ein Segel überhaupt zieht, welche Kurse es gibt und warum man "
    "gegen den Wind nicht geradeaus fahren kann.", [

    lektion("k-kurse", "Die Kurse", ["kurse", "sperrzone"],
        "Ein Boot kann in fast jede Richtung segeln — nur nicht direkt gegen "
        "den Wind. Der Bereich von etwa **45 Grad zu beiden Seiten** der "
        "Windrichtung ist die **Sperrzone**; darin steht das Segel nur noch "
        "und killt.\n\n"
        "Die Kurse, von der Sperrzone weg gezählt:\n\n"
        "**Am Wind** — so dicht am Wind wie möglich, rund 45 Grad. Das Segel "
        "ist dichtgeholt, das Boot krängt am stärksten.\n\n"
        "**Halber Wind** — der Wind kommt quer von der Seite, 90 Grad. Der "
        "schnellste Kurs der meisten Boote.\n\n"
        "**Raumschots** — der Wind kommt schräg von hinten, rund 135 Grad. "
        "Das Segel ist weit aufgefiert.\n\n"
        "**Vor dem Wind** — der Wind genau von achtern. Ruhig, aber "
        "langsamer als es sich anfühlt, und wegen der drohenden **Patenthalse** "
        "der unangenehmste Kurs.\n\n"
        "Wer ein Ziel in Luv erreichen will, muss **kreuzen**: abwechselnd "
        "auf beiden Seiten am Wind, im Zickzack. Der Weg wird dadurch etwa "
        "um die Hälfte länger als die Luftlinie.\n\n"
        "Die Grundregel fürs Trimmen gilt auf jedem Kurs: **Schot so weit "
        "aufmachen, bis das Segel vorne zu killen beginnt, dann wieder "
        "dichtnehmen, bis es gerade steht.**",
        "kurse-zum-wind",
        [
            mc("Wie heißt der Kurs, bei dem der Wind genau von der Seite "
               "kommt?",
               ["Halber Wind", "Am Wind", "Raumschots", "Vor dem Wind"], 0,
               "Neunzig Grad zum Wind. Für die meisten Boote der schnellste "
               "Kurs überhaupt — die Kraft am Segel ist groß und treibt fast "
               "vollständig nach vorn statt zur Seite.",
               bild="kurse-zum-wind"),
            mc("Dein Ziel liegt genau in Luv. Was tust du?",
               ["Kreuzen: abwechselnd am Wind auf beiden Bugen.",
                "Direkt darauf zuhalten.",
                "Vor dem Wind fahren und einen Bogen schlagen.",
                "Das Ziel ist unter Segeln nicht erreichbar."], 0,
               "Direkt gegen den Wind geht nicht, aber am Wind mit "
               "abwechselnden Wenden schon. Der Umweg kostet etwa die "
               "Hälfte mehr Strecke.",
               bild="kurse-zum-wind"),
            zahl("Wie groß ist die Sperrzone ungefähr, also der Winkel zu "
                 "*einer* Seite der Windrichtung, in den man nicht segeln "
                 "kann?",
                 45, "Grad",
                 "Etwa 45 Grad zu jeder Seite, zusammen also rund 90 Grad. "
                 "Moderne Regatta-Yachten kommen auf 35 bis 40 Grad heran, "
                 "ein Jollenkreuzer eher auf 50.",
                 toleranz=0.2, bild="kurse-zum-wind"),
            mc("Woran erkennst du, dass die Schot zu weit offen ist?",
               ["Das Segel killt am Vorliek, also vorne am Mast.",
                "Das Boot krängt stärker.",
                "Der Baum liegt auf dem Wasser.",
                "Das Segel ist ganz flach."], 0,
               "Killen heißt flattern, und es beginnt immer vorne. Die "
               "Trimmregel lautet deshalb: aufmachen bis es killt, dann so "
               "weit dichtnehmen, dass es gerade aufhört."),
        ]),
])


# ===========================================================================
# 3 -- Manöver
# ===========================================================================

K_MANOEVER = kapitel("manoever", "Manöver", 3,
    "Wende, Halse, Mann über Bord, An- und Ablegen. Was in der Prüfung "
    "gefragt und auf dem Wasser gebraucht wird.", [

    lektion("m-wende", "Wende und Halse", ["wende", "halse", "patenthalse"],
        "Beide Manöver bringen das Boot von einem Bug auf den anderen — aber "
        "auf entgegengesetzten Wegen.\n\n"
        "**Wende**: Der **Bug** geht durch den Wind. Man kommt vom Am-Wind-"
        "Kurs über die Sperrzone auf die andere Seite. Das Boot wird dabei "
        "langsamer, das Segel schlägt kurz und geht dann kontrolliert "
        "herüber. Kommando: *„Klar zur Wende?\" — „Ree!\"*\n\n"
        "**Halse**: Das **Heck** geht durch den Wind. Man kommt von "
        "raumschots über Vor-dem-Wind auf die andere Seite. Dabei steht das "
        "Segel voll im Wind, bis es schlagartig auf die andere Seite "
        "durchschlägt. Kommando: *„Klar zur Halse?\" — „Rund achtern!\"*\n\n"
        "Die Halse ist das gefährlichere Manöver. Bei starkem Wind kann der "
        "Baum mit voller Wucht herüberschlagen — die **Patenthalse**, wenn "
        "es ungewollt passiert. Deshalb bei viel Wind: Baum mit der Schot "
        "kontrolliert einholen, herüberlassen, wieder auffieren. Und Köpfe "
        "einziehen.\n\n"
        "Wenn eine Wende nicht durchkommt, hängt das Boot **im Wind** und "
        "treibt rückwärts. Dann Ruder umlegen und das Vorsegel back "
        "halten — also gegen den Wind stellen —, damit sich der Bug "
        "abdreht.",
        "wende-halse",
        [
            mc("Bei welchem Manöver geht das Heck durch den Wind?",
               ["Bei der Halse.", "Bei der Wende.",
                "Bei beiden.", "Bei keinem von beiden."], 0,
               "Wende: Bug durch den Wind. Halse: Heck durch den Wind. Die "
               "Eselsbrücke: bei der **W**ende zeigt der Bug kurz **w**ohin "
               "der Wind kommt.",
               bild="wende-halse"),
            mc("Was ist eine Patenthalse?",
               ["Eine ungewollte Halse, bei der der Baum unkontrolliert "
                "herüberschlägt.",
                "Eine besonders schnell gefahrene Halse.",
                "Eine Halse mit gesetztem Spinnaker.",
                "Eine Wende, die nicht durchkommt."], 0,
               "Sie passiert, wenn man vor dem Wind unaufmerksam ein wenig zu "
               "weit abfällt. Der Baum kommt mit voller Wucht — die häufigste "
               "Kopfverletzung im Segelsport und ein klassischer Grund für "
               "Mann über Bord."),
            mc("Das Boot hängt nach einer missglückten Wende im Wind und "
               "treibt rückwärts. Was hilft?",
               ["Vorsegel back halten und Ruder entsprechend legen.",
                "Großschot ganz dichtholen.",
                "Warten, bis der Wind das Boot dreht.",
                "Schwert aufholen."], 0,
               "Back halten heißt: das Vorsegel auf die falsche Seite "
               "ziehen, sodass der Wind von vorn hineindrückt und den Bug "
               "abdreht. Rückwärts wirkt das Ruder umgekehrt — daran denken."),
        ]),

    lektion("m-mob", "Mann über Bord", ["mob", "rettung"],
        "Das wichtigste Manöver überhaupt, und das einzige, bei dem "
        "Sekunden zählen.\n\n"
        "**Die Reihenfolge:**\n\n"
        "**1. Rufen** — „Mann über Bord!\", damit alle es wissen.\n\n"
        "**2. Werfen** — sofort Rettungsmittel hinterher, auch wenn es "
        "daneben geht. Es markiert die Stelle.\n\n"
        "**3. Schauen** — eine Person tut nichts anderes mehr, als den "
        "Verunglückten anzusehen und zu zeigen. Im Wellengang ist ein Kopf "
        "nach zwanzig Sekunden nicht mehr zu finden.\n\n"
        "**4. Fahren** — zurückkommen und so aufstoppen, dass das Boot "
        "**in Luv** des Verunglückten liegt? Nein: **in Lee** halten, "
        "sodass das Boot nicht auf ihn zutreibt. Aufgenommen wird auf der "
        "Leeseite, mit killenden Segeln und ohne Fahrt.\n\n"
        "Für die Rückkehr gibt es mehrere Wege; für die Prüfung genügt der "
        "Grundsatz: **Man nähert sich immer so, dass man am Ende langsam "
        "und steuerbar ist.** Ein Boot, das mit Fahrt ankommt, verletzt den "
        "Menschen im Wasser.\n\n"
        "Auf Binnengewässern kommt hinzu: Motor an, wenn vorhanden — aber "
        "**Getriebe auf Leerlauf**, sobald jemand längsseits ist. Die "
        "Schraube ist die größte Gefahr beim Bergen.",
        "",
        [
            mc("Was ist der erste Handgriff bei Mann über Bord?",
               ["Rufen und sofort ein Rettungsmittel werfen.",
                "Die Segel bergen.",
                "Den Motor starten.",
                "Eine Position im Gerät speichern."], 0,
               "Rufen, werfen, schauen — in dieser Reihenfolge, und alles "
               "innerhalb weniger Sekunden. Das geworfene Rettungsmittel "
               "markiert die Stelle, selbst wenn es den Verunglückten nicht "
               "erreicht."),
            mc("Warum wird eine Person ausschließlich zum Beobachten "
               "abgestellt?",
               ["Weil ein Kopf im Wellengang binnen Sekunden nicht mehr "
                "zu finden ist.",
                "Weil sie die Rettung koordiniert.",
                "Weil es vorgeschrieben ist.",
                "Damit sie die Zeit stoppt."], 0,
               "Sie zeigt ununterbrochen mit dem Arm hin und tut sonst "
               "nichts. Wer den Blick einmal abwendet, findet die Stelle im "
               "Zweifel nicht wieder."),
            mc("Wie liegt das Boot beim Aufnehmen zum Verunglückten?",
               ["So, dass der Verunglückte in Lee ist und das Boot nicht "
                "auf ihn zutreibt.",
                "Quer zum Wind, damit die Segel voll stehen.",
                "Mit Fahrt voraus, um schnell heranzukommen.",
                "Egal, Hauptsache schnell."], 0,
               "Ein abtreibendes Boot, das auf einen Menschen im Wasser "
               "zuläuft, ist eine Gefahr. Aufgenommen wird ohne Fahrt, mit "
               "killenden Segeln, und der Motor steht dabei im Leerlauf."),
        ]),
])


# ===========================================================================
# 4 -- Ausweichregeln
# ===========================================================================

K_REGELN = kapitel("regeln", "Ausweichregeln", 4,
    "Wer weicht wem aus. Das Kapitel mit den meisten Prüfungsfragen — und "
    "die Regeln bauen sauber aufeinander auf.", [

    lektion("r-segel", "Segelboote untereinander", ["ausweichen", "bug"],
        "Drei Regeln, in dieser Reihenfolge anzuwenden:\n\n"
        "**1. Verschiedene Bugseiten:** Das Boot mit dem Wind von **Backbord** "
        "weicht aus. Als Bug gilt die Seite, auf der der Wind einfällt — "
        "kommt er von Backbord, ist man auf Backbordbug.\n\n"
        "Eselsbrücke: *Backbord ist rot, rot heißt anhalten.*\n\n"
        "**2. Gleiche Bugseite:** Das Boot in **Luv** weicht aus. Es hat den "
        "freien Wind und kann leichter reagieren; das Boot in Lee sitzt in "
        "seinem Windschatten und kann kaum.\n\n"
        "**3. Überholen:** Der **Überholende** weicht immer aus, auf welcher "
        "Seite auch immer. Wer überholt wird, hält Kurs und Geschwindigkeit.\n\n"
        "Für alle Regeln gilt der Grundsatz: **Wer ausweicht, tut es früh "
        "und deutlich.** Eine kleine Kursänderung in letzter Sekunde ist "
        "kein Ausweichen — der andere muss erkennen können, dass ausgewichen "
        "wird. Und: Das vorfahrtberechtigte Boot hält Kurs und "
        "Geschwindigkeit, damit man sich darauf verlassen kann.",
        "ausweichen",
        [
            mc("Zwei Segelboote auf verschiedenen Bugseiten kreuzen sich. "
               "Wer weicht aus?",
               ["Das Boot mit dem Wind von Backbord.",
                "Das Boot mit dem Wind von Steuerbord.",
                "Das langsamere Boot.",
                "Das größere Boot."], 0,
               "Backbordbug weicht Steuerbordbug aus. Rot wie Backbord, rot "
               "wie anhalten.",
               bild="ausweichen"),
            mc("Zwei Segelboote auf gleichem Bug, eines in Luv, eines in "
               "Lee. Wer weicht aus?",
               ["Das Boot in Luv.", "Das Boot in Lee.",
                "Das schnellere.", "Beide nach Steuerbord."], 0,
               "Luv weicht Lee aus. Das Leeboot steckt im Windschatten und "
               "hat weniger Möglichkeiten; außerdem könnte es nur in den "
               "Wind schießen, also anhalten.",
               bild="ausweichen"),
            mc("Du holst ein anderes Segelboot ein. Was gilt?",
               ["Du weichst aus, egal auf welcher Seite du vorbeifährst.",
                "Der Eingeholte weicht aus.",
                "Es gilt die Luv-Lee-Regel.",
                "Es gilt die Bugregel."], 0,
               "Die Überholregel schlägt die anderen beiden. Der Eingeholte "
               "hält Kurs und Geschwindigkeit — er kann den Überholer unter "
               "Umständen gar nicht sehen."),
        ]),

    lektion("r-verkehr", "Segel, Motor und Berufsschifffahrt",
        ["vorfahrt", "berufsschifffahrt"],
        "Die Rangfolge richtet sich nach der **Manövrierfähigkeit**: Wer "
        "weniger ausweichen kann, hat Vorrang.\n\n"
        "**Grundsatz:** Maschinenfahrzeuge weichen Segelfahrzeugen aus.\n\n"
        "**Aber**, und das ist die Frage, die gern gestellt wird: Auf "
        "Binnengewässern und in engen Fahrwassern gilt das **nicht** "
        "gegenüber der **Berufsschifffahrt**. Ein Frachtschiff im Fahrwasser "
        "kann weder ausweichen noch anhalten — die Kleinfahrzeuge weichen "
        "aus, Segelboote eingeschlossen. Dasselbe gilt für Fahrgastschiffe "
        "und Fähren im Einsatz.\n\n"
        "**Nie behindert werden** dürfen außerdem Fahrzeuge, die erkennbar "
        "manövrierbehindert sind, und alles, was in einem engen Fahrwasser "
        "nur dort fahren kann.\n\n"
        "**Ein Segelboot unter Motor ist ein Maschinenfahrzeug** — auch wenn "
        "die Segel oben bleiben. Wer den Motor mitlaufen lässt und trotzdem "
        "Segelvorrang beansprucht, hat unrecht; tagsüber ist dafür ein "
        "schwarzer Kegel mit der Spitze nach unten zu führen.\n\n"
        "Für alle gilt zuletzt die wichtigste Regel überhaupt: **Von jeder "
        "Vorfahrt darf abgewichen werden, wenn nur so ein Zusammenstoß zu "
        "vermeiden ist.** Recht haben und Recht behalten sind auf dem Wasser "
        "zwei verschiedene Dinge.",
        "ausweichen",
        [
            mc("Ein Segelboot und ein Motorboot kreuzen sich auf einem See. "
               "Wer weicht aus?",
               ["Das Motorboot.", "Das Segelboot.",
                "Beide nach Steuerbord.", "Das langsamere."], 0,
               "Maschinenfahrzeuge weichen Segelfahrzeugen aus — der "
               "Grundsatz. Die Ausnahmen betreffen Berufsschifffahrt und "
               "enge Fahrwasser.",
               bild="ausweichen"),
            mc("Ein Frachtschiff kommt im Fahrwasser entgegen. Wer weicht "
               "aus?",
               ["Das Segelboot.", "Das Frachtschiff.",
                "Beide gleichermaßen.", "Das Schiff muss stoppen."], 0,
               "Im Fahrwasser weicht das Kleinfahrzeug aus, auch unter "
               "Segeln. Ein Frachtschiff kann dort nicht heraus und hat "
               "einen Bremsweg von mehreren hundert Metern."),
            mc("Ein Segelboot fährt mit gesetzten Segeln **und** laufendem "
               "Motor. Was ist es rechtlich?",
               ["Ein Maschinenfahrzeug.", "Ein Segelfahrzeug.",
                "Beides, je nach Bedarf.", "Ein manövrierbehindertes "
                "Fahrzeug."], 0,
               "Sobald die Maschine zum Antrieb läuft, ist es ein "
               "Maschinenfahrzeug — mit allen Pflichten. Tagsüber wird das "
               "durch einen schwarzen Kegel, Spitze nach unten, angezeigt."),
            mc("Du hast Vorfahrt, aber der andere weicht erkennbar nicht "
               "aus. Was tust du?",
               ["Selbst ausweichen — ein Zusammenstoß geht immer vor.",
                "Kurs und Geschwindigkeit halten, du hast Recht.",
                "Schallsignal geben und weiterfahren.",
                "Sofort ankern."], 0,
               "Kurs halten ist die Regel, aber sie endet dort, wo nur noch "
               "eigenes Handeln den Zusammenstoß verhindert. Diese Ausnahme "
               "steht ausdrücklich in den Vorschriften."),
        ]),
])


# ===========================================================================
# 5 -- Betonnung, Lichter und Schallsignale
# ===========================================================================

K_ZEICHEN = kapitel("zeichen", "Betonnung und Lichter", 5,
    "Wie das Wasser beschildert ist und was man nachts sieht. Reine "
    "Merksache — und genau deshalb Karteikartenstoff.", [

    lektion("z-tonnen", "Betonnung", ["betonnung", "fahrwasser"],
        "Die seitliche Betonnung kennzeichnet ein Fahrwasser. Entscheidend "
        "ist die **Blickrichtung**: Alle Angaben gelten **von See kommend**, "
        "also flussaufwärts beziehungsweise in Richtung Hafen.\n\n"
        "**Backbord** (links von See kommend): **rot**, Form **stumpf** "
        "(Zylinder oder Spitze oben flach), gerade Kennziffern.\n\n"
        "**Steuerbord** (rechts): **grün**, Form **spitz** (Kegel), ungerade "
        "Kennziffern.\n\n"
        "Merkhilfe für die Fahrt hinein: *rot backbord, grün steuerbord* — "
        "dieselbe Zuordnung wie bei den Positionslaternen. Wer heraus fährt, "
        "hat sie genau andersherum an der Seite, und dieser Wechsel ist die "
        "häufigste Prüfungsfalle.\n\n"
        "Weitere Zeichen, die man kennen muss:\n\n"
        "**Mittefahrwasser**: rot-weiß längsgestreift, Kugel oben — darf "
        "beidseitig passiert werden.\n\n"
        "**Einzelgefahr**: schwarz mit rotem Band, zwei schwarze Kugeln — "
        "weiträumig umfahren.\n\n"
        "**Kardinalzeichen** zeigen mit zwei schwarzen Kegeln, auf welcher "
        "Seite man sicher vorbeikommt: Spitzen nach oben heißt nördlich "
        "passieren, nach unten südlich, auseinander östlich, zusammen "
        "westlich.",
        "betonnung",
        [
            mc("Von See kommend: Welche Farbe und Form hat die "
               "Backbordtonne?",
               ["Rot und stumpf.", "Grün und spitz.",
                "Gelb und rund.", "Schwarz mit rotem Band."], 0,
               "Rot, stumpf, gerade Nummern. Gegenstück ist grün und spitz "
               "auf der Steuerbordseite.",
               bild="betonnung"),
            mc("Du verlässt den Hafen und fährst hinaus. Wo liegen jetzt die "
               "roten Tonnen?",
               ["An Steuerbord — die Betonnung gilt von See kommend.",
                "Weiterhin an Backbord.",
                "In der Mitte.",
                "Rote Tonnen gibt es hinaus nicht."], 0,
               "Die Richtungsangabe ist fest und gilt hinein. Wer hinaus "
               "fährt, hat alles spiegelverkehrt — genau das wird gerne "
               "gefragt.",
               bild="betonnung"),
            mc("Eine Tonne ist rot-weiß längsgestreift mit einer Kugel als "
               "Toppzeichen. Was bedeutet sie?",
               ["Mittefahrwasser, beidseitig passierbar.",
                "Einzelgefahr, weiträumig umfahren.",
                "Sperrgebiet.",
                "Ankerplatz."], 0,
               "Die Längsstreifung steht für „sicheres Wasser ringsum\". "
               "Eine Einzelgefahr wäre schwarz mit rotem **Querband** und "
               "zwei Kugeln."),
        ]),

    lektion("z-lichter", "Lichter und Schallsignale", ["lichter", "signale"],
        "**Nachts** zeigt jedes Fahrzeug, was es ist und wohin es fährt.\n\n"
        "**Seitenlichter**: rot nach Backbord, grün nach Steuerbord, je "
        "112,5 Grad. **Hecklicht**: weiß nach achtern, 135 Grad. Zusammen "
        "ergeben sie den Vollkreis.\n\n"
        "**Segelboot unter Segel**: nur Seitenlichter und Hecklicht — kein "
        "weißes Licht nach vorn.\n\n"
        "**Maschinenfahrzeug**: zusätzlich ein weißes **Topplicht** nach "
        "vorn. Wer also von vorn ein weißes Licht über den farbigen sieht, "
        "hat ein Fahrzeug unter Maschine vor sich.\n\n"
        "**Boote unter 7 m** ohne Maschine dürfen sich auf ein weißes "
        "Rundumlicht beschränken, das rechtzeitig gezeigt wird.\n\n"
        "Was man daraus liest: **Rot und grün zugleich** heißt, das Fahrzeug "
        "kommt genau entgegen. **Nur rot** heißt, es zieht von rechts nach "
        "links — man sieht seine Backbordseite. **Nur weiß** heißt meist, "
        "man sieht ein Heck und fährt hinterher.\n\n"
        "**Schallsignale** auf Binnengewässern, kurz und lang:\n\n"
        "**Ein kurzer Ton**: „Ich richte meinen Kurs nach Steuerbord.\"\n"
        "**Zwei kurze**: „… nach Backbord.\"\n"
        "**Drei kurze**: „Meine Maschine geht rückwärts.\"\n"
        "**Fünf kurze oder mehr**: Warnsignal — „Ich verstehe Ihre Absicht "
        "nicht\" beziehungsweise Gefahr.\n"
        "**Ein langer Ton**: Achtungssignal, etwa beim Verlassen einer "
        "Hafenausfahrt.",
        "lichter",
        [
            mc("Du siehst nachts gleichzeitig ein rotes und ein grünes Licht "
               "ohne weißes darüber. Was ist das?",
               ["Ein Segelboot unter Segel, genau entgegenkommend.",
                "Ein Maschinenfahrzeug von der Seite.",
                "Eine Tonne.",
                "Ein Fahrzeug, das sich entfernt."], 0,
               "Beide Seitenlichter zugleich heißt Kurs genau auf dich zu. "
               "Fehlt das weiße Topplicht, fährt es unter Segeln.",
               bild="lichter"),
            mc("Du siehst nur ein weißes Licht. Was ist am "
               "wahrscheinlichsten?",
               ["Du siehst ein Heck und fährst hinterher.",
                "Das Fahrzeug kommt entgegen.",
                "Es ankert quer zu dir.",
                "Es ist manövrierunfähig."], 0,
               "Das Hecklicht ist weiß und leuchtet nach achtern. Wer nur "
               "weiß sieht, ist hinter dem anderen — und ist damit meist "
               "auch der Überholende, also ausweichpflichtig.",
               bild="lichter"),
            mc("Was bedeuten fünf kurze Töne?",
               ["Warnsignal: Gefahr oder „Absicht unklar\".",
                "„Ich gehe nach Steuerbord.\"",
                "„Ich gehe rückwärts.\"",
                "Achtungssignal beim Ablegen."], 0,
               "Fünf oder mehr kurze Töne sind das Warnsignal. Ein kurzer "
               "Ton steht für Steuerbord, zwei für Backbord, drei für "
               "Rückwärtsfahrt."),
        ]),
])


# ===========================================================================
# 6 -- Wetter und Sicherheit
# ===========================================================================

K_WETTER = kapitel("wetter", "Wetter und Sicherheit", 6,
    "Wind einschätzen, Gewitter erkennen, Ausrüstung kennen. Auf Binnenseen "
    "ist das Wetter die häufigste Unfallursache — weil es dort schnell "
    "umschlägt und das Ufer trügerisch nah aussieht.", [

    lektion("w-wind", "Wind und Beaufort", ["beaufort", "wind"],
        "Windstärken werden in **Beaufort** angegeben, und die Skala ist "
        "nicht linear — jede Stufe bringt erheblich mehr Kraft, denn der "
        "Winddruck wächst mit dem **Quadrat** der Geschwindigkeit. Doppelte "
        "Windgeschwindigkeit heißt vierfache Kraft im Segel.\n\n"
        "Die Stufen, an denen für ein Segelboot etwas kippt:\n\n"
        "**3 Bft** (12–19 km/h): angenehmes Segeln, kleine Schaumköpfe.\n\n"
        "**4 Bft** (20–28 km/h): reffen wird bei kleinen Booten ein Thema, "
        "viele Schaumköpfe.\n\n"
        "**5 Bft** (29–38 km/h): für Jollen die Grenze, überall Schaumköpfe, "
        "etwas Gischt.\n\n"
        "**6 Bft** (39–49 km/h): Sturmwarnung auf Binnenseen, Jollen bleiben "
        "am Steg.\n\n"
        "Auf Binnengewässern gibt es **Windwarnungen** über Blinklichter am "
        "Ufer: **40 Blitze je Minute** heißt Starkwind (ab 6 Bft), **90 "
        "Blitze je Minute** heißt Sturm (ab 8 Bft). Bei Starkwindwarnung "
        "gehört ein kleines Boot in den Hafen, bei Sturmwarnung jedes.\n\n"
        "Zwei örtliche Winde, die man kennen muss: Am Berg zieht tagsüber "
        "der **Talwind** hangaufwärts, nachts fällt der **Bergwind** "
        "herunter — auf Alpenseen der Grund, warum es vormittags flau ist "
        "und mittags kräftig weht.",
        "",
        [
            zahl("Bei wie vielen Blitzen je Minute zeigt eine "
                 "Uferwarnleuchte Starkwind an?",
                 40, "Blitze/Minute",
                 "40 je Minute heißt Starkwind ab etwa 6 Beaufort, 90 je "
                 "Minute heißt Sturm ab 8. Der Unterschied ist an der "
                 "Blinkfrequenz gut zu erkennen — eins ist ein ruhiges "
                 "Takten, das andere ein Flackern.",
                 toleranz=0.05),
            mc("Der Wind verdoppelt sich von 10 auf 20 Knoten. Wie ändert "
               "sich der Druck im Segel?",
               ["Er vervierfacht sich.", "Er verdoppelt sich.",
                "Er bleibt gleich.", "Er verachtfacht sich."], 0,
               "Der Staudruck wächst mit dem Quadrat der Geschwindigkeit. "
               "Deshalb ist der Sprung von 4 auf 5 Beaufort für ein kleines "
               "Boot viel größer, als die Zahlen vermuten lassen."),
            mc("Auf einem Alpensee ist es vormittags flau und wird mittags "
               "kräftig. Woran liegt das?",
               ["Am Talwind, der mit der Erwärmung hangaufwärts einsetzt.",
                "An der Gezeitenströmung.",
                "An der zunehmenden Luftfeuchte.",
                "Am Bergwind."], 0,
               "Die Sonne heizt die Hänge, die Luft steigt daran auf und "
               "zieht Luft aus dem Tal nach. Nachts kehrt sich das um: Die "
               "abgekühlte Luft fällt als Bergwind herunter."),
        ]),

    lektion("w-gewitter", "Gewitter und Ausrüstung", ["gewitter", "rettung"],
        "**Gewitter** sind auf Binnenseen die größte Gefahr. Vor der "
        "Regenwand läuft eine **Böenwalze** mit Windgeschwindigkeiten, die "
        "das Dreifache des vorherigen Windes erreichen können — und sie "
        "kommt bei noch blauem Himmel.\n\n"
        "**Anzeichen**, in dieser Reihenfolge:\n\n"
        "Aufquellende Haufenwolken mit dunkler, breiter Basis; eine "
        "**faserige** Oberseite, die verrät, dass die Wolke oben vereist "
        "ist; eine dunkle Wolkenwalze an der Unterkante; plötzliche Stille "
        "und Temperatursturz.\n\n"
        "**Was zu tun ist:** Früh entscheiden und **sofort** den nächsten "
        "Hafen ansteuern — nicht den Heimathafen. Segel bergen oder stark "
        "reffen, Rettungswesten anlegen, Mannschaft in die Plicht, Luken "
        "schließen. Ist das Gewitter da, unter Motor mit dem Bug gegen die "
        "Böen halten.\n\n"
        "**Ausrüstung**, nach der gefragt wird: Rettungswesten für alle an "
        "Bord (und getragen, nicht verstaut), Rettungsring oder "
        "-hufeisen, Paddel oder Riemen, Festmacher und Anker mit "
        "ausreichender Kette, Lenzeinrichtung, Feuerlöscher bei Motor, "
        "Signalmittel, Verbandszeug.\n\n"
        "Das **Notsignal** auf Binnengewässern: wiederholtes langsames Heben "
        "und Senken der seitlich ausgestreckten Arme. Dazu zählen auch rote "
        "Sterne, Rauch, ein Dauerschallsignal und die Nationalflagge mit "
        "einem Knoten darüber.",
        "",
        [
            mc("Woran erkennst du, dass aus einer Quellwolke ein Gewitter "
               "wird?",
               ["Die Oberseite wird faserig statt knollig.",
                "Die Wolke wird breiter als hoch.",
                "Der Wind schläft ein.",
                "Erst am Donner."], 0,
               "Faserig heißt vereist — ab da ist es ein Gewitter im Bau. "
               "Das sieht man lange, bevor es donnert, und genau dann ist "
               "die Entscheidung zu treffen."),
            mc("Ein Gewitter zieht auf. Wohin fährst du?",
               ["Zum nächstgelegenen Schutz, nicht zum Heimathafen.",
                "Zum Heimathafen, egal wie weit.",
                "In die Seemitte, dort ist es sicherer.",
                "An eine Boje im Freien."], 0,
               "Die Böenwalze läuft dem Regen weit voraus. Was zählt, ist "
               "die Zeit bis zum Schutz — welcher Hafen das ist, ist "
               "zweitrangig."),
            mc("Wie lautet das Notzeichen mit den Armen?",
               ["Langsames Heben und Senken der seitlich ausgestreckten "
                "Arme.",
                "Beide Arme über dem Kopf kreuzen.",
                "Schnelles Winken mit einem Arm.",
                "Arme waagrecht ausstrecken und halten."], 0,
               "Langsam und wiederholt, beide Arme seitlich. Schnelles "
               "Winken mit einem Arm ist ein Gruß und wird auch so "
               "verstanden — ein Unterschied, der zählt."),
            mc("Wann gehört die Rettungsweste angelegt?",
               ["Bevor es kritisch wird — spätestens bei aufziehendem "
                "Schlechtwetter.",
                "Erst wenn jemand ins Wasser fällt.",
                "Nur bei Nachtfahrt.",
                "Nur für Nichtschwimmer."], 0,
               "Eine Weste im Stauraum hat noch niemanden gerettet. Bei "
               "aufziehendem Gewitter, bei Nacht, bei Kälte und im Vorschiff "
               "wird sie getragen."),
        ]),
])


# ===========================================================================
# 7 -- Recht und Umwelt
# ===========================================================================

K_RECHT = kapitel("recht", "Recht und Umwelt", 7,
    "Was man an Bord haben muss, wo man fahren darf und was man dem See "
    "schuldet.", [

    lektion("u-recht", "Pflichten an Bord", ["papiere", "sorgfalt"],
        "Der **Schiffsführer** ist für Boot und Besatzung verantwortlich — "
        "auch dann, wenn ein anderer am Ruder sitzt. Diese Verantwortung "
        "lässt sich nicht delegieren.\n\n"
        "Vor jeder Fahrt gehört geprüft: Zustand von Rumpf, Rigg und "
        "Beschlägen, Vollständigkeit der Sicherheitsausrüstung, "
        "Wetterbericht, und ob die Besatzung der Lage gewachsen ist.\n\n"
        "**Alkohol**: Für Schiffsführer gelten Grenzen wie im "
        "Straßenverkehr; in Österreich 0,8 Promille, für Berufsschiffer "
        "weniger. Unabhängig davon macht schon wenig Alkohol zusammen mit "
        "Sonne, Wind und Schaukeln deutlich mehr als an Land.\n\n"
        "**Umwelt**: Kein Abfall und kein Öl ins Wasser, kein Waschen mit "
        "Spülmittel über Bord, Toiletten nur über Sammeltank. "
        "**Schilfgürtel und Flachwasserzonen** sind Kinderstube für Fische "
        "und Vögel — Abstand halten, nicht hineinfahren, nicht ankern. Viele "
        "Seen haben dafür ausgewiesene Schutzzonen mit Bojenketten.\n\n"
        "**Rücksicht** gehört dazu: Keine Welle in Badebereiche, Abstand zu "
        "Schwimmern, Motor aus in Ufernähe, und in Naturschutzgebieten "
        "langsam und leise.",
        "",
        [
            mc("Wer trägt die Verantwortung, wenn ein Gast am Ruder einen "
               "Fehler macht?",
               ["Der Schiffsführer.", "Der Gast am Ruder.",
                "Der Eigner.", "Beide zu gleichen Teilen."], 0,
               "Die Verantwortung des Schiffsführers ist nicht übertragbar. "
               "Wer jemanden ans Ruder lässt, bleibt dafür zuständig, dass "
               "es gutgeht."),
            mc("Was gehört bei einem Gewitterrisiko zur Vorbereitung vor dem "
               "Ablegen?",
               ["Den Wetterbericht einholen und die Rückkehr danach planen.",
                "Mehr Proviant mitnehmen.",
                "Den Anker klarmachen.",
                "Nichts Besonderes."], 0,
               "Die meisten Wetterunfälle auf Binnenseen wären durch einen "
               "Blick auf die Vorhersage und eine früher geplante Rückkehr "
               "vermeidbar gewesen."),
            mc("Warum hält man Abstand vom Schilfgürtel?",
               ["Weil er Laichplatz und Brutgebiet ist und leicht Schaden "
                "nimmt.",
                "Weil dort der Wind abreißt.",
                "Weil es dort zu tief ist.",
                "Wegen der Strömung."], 0,
               "Der Schilfgürtel ist die produktivste Zone eines Sees. "
               "Durchfahren zerstört Laich und vertreibt Brutvögel — "
               "deshalb ist er vielerorts ausdrücklich gesperrt."),
        ]),
])


KAPITEL = [K_BOOT, K_KURSE, K_MANOEVER, K_REGELN, K_ZEICHEN, K_WETTER, K_RECHT]
PLAN = []

THEMEN = {
    "boot": "Das Boot",
    "kurse": "Kurse und Trimm",
    "manoever": "Manöver",
    "regeln": "Ausweichregeln",
    "zeichen": "Betonnung und Lichter",
    "wetter": "Wetter und Sicherheit",
    "recht": "Recht und Umwelt",
}


def frage(ident, stufe, thema, q, optionen, antwort, warum, bild=""):
    return {"id": ident, "stufe": stufe, "thema": thema, "q": q,
            "optionen": optionen, "antwort": antwort, "warum": warum,
            "bild": bild}


EINSTUFUNG = [
    frage("e-luv", 1, "boot", "Was bedeutet „Luv\"?",
          ["Die Seite, von der der Wind kommt.",
           "Die Seite, zu der der Wind weht.",
           "Die linke Seite.", "Die Vorderseite."], 0,
          "Luv ist windzugewandt, Lee windabgewandt.", bild="bootsteile"),
    frage("e-backbord", 1, "boot", "Backbord ist …",
          ["links, rot.", "rechts, grün.", "hinten.", "die Luvseite."], 0,
          "Links und rot, wie die Backbordlaterne und die Backbordtonne."),
    frage("e-halber", 2, "kurse",
          "Wie heißt der Kurs mit dem Wind genau von der Seite?",
          ["Halber Wind", "Am Wind", "Raumschots", "Vor dem Wind"], 0,
          "Neunzig Grad zum Wind, für die meisten Boote der schnellste "
          "Kurs.", bild="kurse-zum-wind"),
    frage("e-kreuzen", 2, "kurse",
          "Das Ziel liegt genau in Luv. Wie kommst du hin?",
          ["Kreuzen, also im Zickzack am Wind.",
           "Direkt darauf zu.", "Vor dem Wind mit Bogen.",
           "Gar nicht."], 0,
          "Direkt gegen den Wind liegt die Sperrzone.",
          bild="kurse-zum-wind"),
    frage("e-halse", 3, "manoever",
          "Bei welchem Manöver geht das Heck durch den Wind?",
          ["Halse", "Wende", "Beide", "Keines"], 0,
          "Wende: Bug. Halse: Heck.", bild="wende-halse"),
    frage("e-mob", 3, "manoever",
          "Erster Handgriff bei Mann über Bord?",
          ["Rufen und Rettungsmittel werfen.", "Segel bergen.",
           "Motor starten.", "Position speichern."], 0,
          "Rufen, werfen, schauen — in Sekunden."),
    frage("e-bug", 4, "regeln",
          "Zwei Segelboote auf verschiedenen Bugen. Wer weicht aus?",
          ["Der mit Wind von Backbord.", "Der mit Wind von Steuerbord.",
           "Der Langsamere.", "Der Größere."], 0,
          "Backbordbug weicht Steuerbordbug aus.", bild="ausweichen"),
    frage("e-luvlee", 4, "regeln",
          "Gleicher Bug, eines in Luv, eines in Lee. Wer weicht aus?",
          ["Luv", "Lee", "Der Schnellere", "Beide nach Steuerbord"], 0,
          "Luv weicht Lee aus.", bild="ausweichen"),
    frage("e-fracht", 5, "regeln",
          "Ein Frachtschiff kommt im Fahrwasser entgegen. Wer weicht aus?",
          ["Das Segelboot.", "Das Frachtschiff.", "Beide.",
           "Das Schiff stoppt."], 0,
          "Im Fahrwasser weicht das Kleinfahrzeug aus, auch unter Segeln."),
    frage("e-tonne", 5, "zeichen",
          "Von See kommend: Farbe und Form der Backbordtonne?",
          ["Rot und stumpf.", "Grün und spitz.", "Gelb und rund.",
           "Schwarz mit rotem Band."], 0,
          "Rot, stumpf, gerade Nummern.", bild="betonnung"),
    frage("e-lichter", 6, "zeichen",
          "Nachts rot und grün zugleich, kein weißes darüber. Was ist das?",
          ["Ein Segelboot, genau entgegenkommend.",
           "Ein Maschinenfahrzeug von der Seite.",
           "Eine Tonne.", "Ein Fahrzeug, das sich entfernt."], 0,
          "Beide Seitenlichter heißt Kurs auf dich zu; ohne Topplicht "
          "unter Segeln.", bild="lichter"),
    frage("e-signal", 6, "zeichen", "Was bedeuten fünf kurze Töne?",
          ["Warnsignal.", "„Ich gehe nach Steuerbord.\"",
           "„Ich gehe rückwärts.\"", "Achtungssignal."], 0,
          "Fünf oder mehr kurze Töne sind das Warnsignal."),
    frage("e-sturm", 7, "wetter",
          "Wie viele Blitze je Minute zeigt die Sturmwarnung am Ufer?",
          ["90", "40", "20", "60"], 0,
          "40 je Minute ist Starkwind, 90 ist Sturm."),
    frage("e-gewitter", 7, "wetter",
          "Ein Gewitter zieht auf. Wohin fährst du?",
          ["Zum nächsten Schutz.", "Zum Heimathafen.",
           "In die Seemitte.", "An eine Boje."], 0,
          "Die Böenwalze läuft weit voraus; es zählt die Zeit bis zum "
          "Schutz."),
    frage("e-verantwortung", 8, "recht",
          "Ein Gast am Ruder macht einen Fehler. Wer haftet?",
          ["Der Schiffsführer.", "Der Gast.", "Der Eigner.",
           "Beide."], 0,
          "Die Verantwortung des Schiffsführers ist nicht übertragbar."),
    frage("e-schilf", 8, "recht", "Warum Abstand vom Schilfgürtel?",
          ["Laich- und Brutgebiet.", "Der Wind reißt ab.",
           "Zu tief.", "Strömung."], 0,
          "Die produktivste Zone des Sees, und leicht zu zerstören."),
]
