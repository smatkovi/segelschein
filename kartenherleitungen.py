# -*- coding: utf-8 -*-
"""Herleitungen zu den Karteikarten.

In den Karten stehen Zahlen, die nach Formeln aussehen: das Drei- bis
Fuenffache der Wassertiefe, der Faktor 1,41 beim Kreuzen, drei Sekunden je
Kilometer, 112,5 Grad Seitenlicht. Wer sie nur auswendig kann, hat nichts
in der Hand, sobald die Lage vom Lehrbuch abweicht -- und genau das ist auf
dem Wasser der Normalfall.

Deshalb haengt an jeder solchen Karte hier die Herleitung: woher die Zahl
kommt, unter welcher Annahme sie gilt, und was passiert, wenn die Annahme
nicht stimmt. Sie steht **in der Loesung**, nicht in der Frage -- vorher
waere sie die Antwort.

Der Schluessel ist der Fragetext selbst. Damit braucht keine Frage eine
Kennung, und wenn eine Frage umformuliert wird, faellt beim naechsten Bauen
sofort auf, dass ihre Herleitung verwaist ist (tools/make-kurs.py prueft
das und bricht ab).

Jedes Formelzeichen wird definiert, bevor es auftaucht, und jede Formel,
die in einer Herleitung neu eingefuehrt wird, wird selbst hergeleitet oder
als das benannt, was sie ist: eine Festlegung, eine Messung oder eine
Merkregel. Eine erfundene Herleitung waere schlimmer als gar keine.
"""
from __future__ import unicode_literals


ANKER = (
 "## Woher die drei bis fünf kommen\n\n"
 "`T` Wassertiefe plus Freibord, also von der Klampe bis zum Grund, m. "
 "`L` gesteckte Länge von Kette und Leine, m. `α` Winkel, unter dem "
 "der Zug am Ankerschaft ankommt, Grad.\n\n"
 "Die gesteckte Leine spannt sich von der Klampe zum Anker. Denkt man sie "
 "gerade, ist sie die Schräge eines rechtwinkligen Dreiecks: die "
 "senkrechte Kathete ist `T`, die Schräge ist `L`, und `α` ist der "
 "Winkel unten am Grund. Im rechtwinkligen Dreieck ist der Sinus eines "
 "Winkels die Gegenkathete durch die Hypotenuse, also `sin α = T / L` "
 "und damit\n\n"
 "`L = T / sin α`\n\n"
 "Der Anker gräbt sich nur ein, wenn der Zug flach ankommt; die Flunke "
 "braucht dafür etwa 12° bis 20°. Einsetzen: `1 / sin 12° ≈ 4,8` "
 "und `1 / sin 20° ≈ 2,9`. Das **sind** die drei bis fünf — die "
 "Faustregel ist nichts anderes als der Kehrwert des Sinus dieses Winkels.\n\n"
 "In Wirklichkeit hängt die Kette durch, und das hilft: der Bogen kommt "
 "noch flacher am Grund an als die gedachte Gerade. Deshalb hält Kette "
 "besser als Leine, und deshalb steckt man bei Wind und Welle mehr — die "
 "Ruckbelastung richtet den Zug sonst auf."
)

VERDRAENGUNG = (
 "## Archimedes, in zwei Zeilen\n\n"
 "`m` Masse des Bootes, kg. `V` verdrängtes Wasservolumen, m³. "
 "`ρ` Dichte des Wassers, kg/m³ — Süßwasser 1000, Salzwasser rund "
 "1025. `g` Fallbeschleunigung, 9,81 m/s².\n\n"
 "Ein schwimmendes Boot steht still, also heben sich die Kräfte auf: das "
 "Gewicht `m · g` nach unten, der Auftrieb nach oben. Der Auftrieb ist "
 "das Gewicht des verdrängten Wassers, und das ist `ρ · V · g` "
 "(Archimedes). Gleichsetzen:\n\n"
 "`m · g = ρ · V · g`\n\n"
 "Das `g` steht auf beiden Seiten und kürzt sich weg — deshalb gilt der "
 "Satz auch auf dem Mond. Übrig bleibt `V = m / ρ`.\n\n"
 "Mit `ρ = 1000 kg/m³`: `V = 2400 / 1000 = 2,4 m³`. In Süßwasser "
 "ist die Zahl in Tonnen also dieselbe wie die in Kubikmetern — nicht "
 "durch Zufall, sondern weil das Kilogramm einmal über einen Liter Wasser "
 "festgelegt wurde.\n\n"
 "In Salzwasser: `V = 2400 / 1025 ≈ 2,34 m³`. Dasselbe Boot taucht dort "
 "weniger tief ein, und beim Schleusen von See in den Fluss sackt es ein "
 "paar Zentimeter tiefer."
)

KREUZEN = (
 "## Warum der Umweg genau `1 / cos β` ist\n\n"
 "`d` Weg in Windrichtung, den man gutmachen will (Luftlinie), km. "
 "`s` tatsächlich gesegelter Weg, km. `β` Kurs zum Wind, Grad.\n\n"
 "Gegen den Wind führt kein gerader Weg, also segelt man Schläge unter "
 "dem Winkel `β` zur Windrichtung. Von einem Schlag der Länge `sᵢ` "
 "zählt nur der Anteil in Windrichtung, und das ist die Ankathete im "
 "rechtwinkligen Dreieck: `sᵢ · cos β`. Summiert man über alle "
 "Schläge, steht links der gutgemachte Weg und rechts der gesegelte:\n\n"
 "`d = s · cos β`  →  `s = d / cos β`\n\n"
 "Bemerkenswert daran ist, dass die Aufteilung herausfällt: ob man zwei "
 "lange oder zwanzig kurze Schläge segelt, ändert am Umweg nichts. Nur "
 "der Winkel zählt.\n\n"
 "Bei `β = 45°` ist `cos 45° = √2 / 2 ≈ 0,707`, also "
 "`s = d · √2 ≈ 1,41 · d`. Aus 6 km werden gut 8,5 km — und die Zeit "
 "wächst mit demselben Faktor. Was hier nicht drinsteckt, kommt noch "
 "dazu: jede Wende kostet Fahrt, und Strom und Welle rechnen für sich."
)

WENDEWINKEL = (
 "## Warum rund 90 Grad\n\n"
 "`β` Kurs zum Wind, Grad. Der Wendewinkel ist die Kursänderung von "
 "einem Bug auf den anderen.\n\n"
 "Am Wind liegt ein Tourenboot bei `β ≈ 45°` zur wahren Windrichtung — "
 "näher heran killt das Segel. Nach der Wende liegt es spiegelbildlich "
 "zur selben Windachse, also wieder bei 45°, nur auf der anderen Seite. "
 "Die Kursänderung ist die Summe beider Winkel:\n\n"
 "`Wendewinkel = 2 · β = 90°`\n\n"
 "Daraus folgt der Rest von selbst: Je höher ein Boot an den Wind geht, "
 "also je kleiner `β`, desto kleiner sein Wendewinkel **und** desto "
 "kleiner sein Umweg `1 / cos β`. Eine Yacht mit `β = 35°` wendet "
 "über 70° und segelt nur das `1 / cos 35° ≈ 1,22`-fache; eine "
 "Jolle, die nur 50° schafft, wendet über 100° und segelt das "
 "1,56-fache. Höhe am Wind ist deshalb bares Geld."
)

SEGELWINKEL = (
 "## Warum das eine Merkregel ist und keine Formel\n\n"
 "`β` Kurs zum Wind, Grad. `δ` Winkel des Segels zur "
 "Mittschiffslinie, Grad. `ε` Anstellwinkel, also der Winkel zwischen "
 "Segel und anliegendem Wind, Grad.\n\n"
 "Ein Segel zieht wie ein Flügel, und ein Flügel hat sein Bestes bei "
 "einem Anstellwinkel von etwa 15° bis 20°: darüber reißt die "
 "Strömung ab, darunter killt das Tuch. Der Wind kommt unter `β` zur "
 "Mittschiffslinie, das Segel steht unter `δ` dazu, also ist "
 "`ε = β − δ`. Setzt man `δ = β / 2`, bleibt "
 "`ε = β / 2` — und das trifft den guten Bereich genau dann, wenn "
 "`β` zwischen etwa 30° und 40° liegt.\n\n"
 "Damit ist gesagt, was die Regel ist und wo sie herkommt: eine "
 "Winkelhalbierende, die auf **am Wind** gerechnet ist. Zwei Dinge "
 "verschieben sie. Der scheinbare Wind kommt weiter von vorn als der "
 "wahre, also ist `β` in Wahrheit kleiner als der Kurs zum wahren Wind. "
 "Und auf raumen Kursen zieht das Segel nicht mehr wie ein Flügel, "
 "sondern wie ein Bremsschirm; dort zählt nur noch die Fläche quer zum "
 "Wind, und `δ ≈ β / 2` wird falsch.\n\n"
 "Eine Formel, die man ausrechnet, ist das also nicht — eine Ansage für "
 "den ersten Griff schon. Genauer sagt es das Segel selbst: **aufmachen, "
 "bis es killt, dann gerade dicht nehmen.**"
)

KNOTEN = (
 "## Woher 0,514 kommt\n\n"
 "`sm` Seemeile, m. `kn` Knoten, also eine Seemeile je Stunde.\n\n"
 "Die Seemeile ist keine willkürliche Länge, sondern ein Stück Erde: "
 "eine Bogenminute auf einem Großkreis. Der Erdumfang misst rund "
 "40 007 km, ein Vollkreis hat 360 Grad und ein Grad 60 Minuten:\n\n"
 "`1 sm = 40 007 km / (360 · 60) ≈ 1,852 km`\n\n"
 "Genau deshalb ist sie heute auf 1852 m **festgelegt** — die Zahl ist "
 "gerundete Erdvermessung und keine Definition aus dem Nichts. Ihr Nutzen "
 "ist die Seekarte: eine Bogenminute Breite am Kartenrand ist eine "
 "Seemeile, man sticht sie einfach ab.\n\n"
 "Ein Knoten ist eine Seemeile je Stunde, eine Stunde hat 3600 Sekunden:\n\n"
 "`1 kn = 1852 m / 3600 s ≈ 0,514 m/s`\n\n"
 "Damit ist `20 kn ≈ 20 · 0,514 ≈ 10,3 m/s`. Die Faustregel "
 "„Knoten halbieren“ ist derselbe Faktor, auf 0,5 abgerundet: sie "
 "liegt rund 3 % zu niedrig, und das ist an Bord die harmlose Richtung."
)

KMH = (
 "## Woher die 3,6 kommt\n\n"
 "Hier ist nichts zu messen, das ist reine Buchhaltung mit Einheiten. Wer "
 "in einer Sekunde einen Meter macht, macht in einer Stunde 3600 Meter, "
 "denn eine Stunde hat 3600 Sekunden. Und 3600 Meter sind 3,6 Kilometer, "
 "denn ein Kilometer hat 1000 Meter:\n\n"
 "`1 m/s = 3600 m/h = 3600 / 1000 km/h = 3,6 km/h`\n\n"
 "Also `5 m/s = 5 · 3,6 = 18 km/h`, und rückwärts teilt man durch "
 "3,6. Wem das im Kopf zu krumm ist: **mal 3, und ein Fünftel davon "
 "dazu** — `5 · 3 = 15`, ein Fünftel davon ist 3, zusammen 18. Das ist "
 "nicht einmal genähert, sondern genau: `3 + 3/5 = 3,6`."
)

BEAUFORT = (
 "## Was Beaufort ist und was es nicht ist\n\n"
 "`B` Windstärke in Beaufort. `v` Windgeschwindigkeit in 10 m Höhe "
 "über freiem Gelände, m/s.\n\n"
 "Beaufort ist **keine gemessene Größe**, sondern eine Skala mit "
 "festgelegten Grenzen: Stufe 6 beginnt bei 10,8 m/s und endet bei "
 "13,8 m/s. Die Stufen wurden ursprünglich über das beschrieben, was man "
 "sieht — wie viel Segel ein Schiff noch tragen kann, wie die See "
 "aussieht — und erst später in Geschwindigkeiten übersetzt. An diese "
 "Übersetzung legt man die Näherung\n\n"
 "`v ≈ 0,836 · B^1,5 m/s`\n\n"
 "Sie ist an die Tabelle **angepasst** und nicht aus der Strömungslehre "
 "hergeleitet; der Exponent 1,5 ist der Wert, der die Stufengrenzen am "
 "besten trifft. Für `B = 6`: `6^1,5 = 6 · √6 ≈ 14,7`, also "
 "`v ≈ 12,3 m/s`, mal 3,6 rund 44 km/h. Mit der Untergrenze 10,8 m/s "
 "gerechnet sind es 39 km/h — daher „knapp 40“.\n\n"
 "Warum eine Jolle ausgerechnet hier im Hafen bleibt, sagt die Formel "
 "nicht. Das ist Erfahrung über Rumpflänge, Verdränger und "
 "Mannschaftsgewicht, keine Physik — der Winddruck wächst aber mit dem "
 "Quadrat, und das ist der Grund, warum die Grenze so scharf ist."
)

STAUDRUCK = (
 "## Warum der Winddruck mit dem Quadrat wächst\n\n"
 "`F` Kraft auf die Fläche, N. `q` Staudruck, Pa. `ρ` Luftdichte, "
 "1,225 kg/m³. `v` Windgeschwindigkeit, m/s. `A` angeströmte Fläche, "
 "m². `c` Formzahl, dimensionslos. `t` Zeit, s. `m` Luftmasse, kg.\n\n"
 "In der Zeit `t` trifft die Luft aus einem Schlauch der Länge `v · t` "
 "und des Querschnitts `A` auf die Fläche, also die Masse\n\n"
 "`m = ρ · A · v · t`\n\n"
 "Wird sie an der Fläche abgebremst, gibt sie ihren Impuls `m · v` ab. "
 "Kraft ist Impuls je Zeit (das zweite Newtonsche Gesetz in seiner "
 "ursprünglichen Form):\n\n"
 "`F = m · v / t = ρ · A · v²`\n\n"
 "Die beiden `v` haben verschiedene Aufgaben, und genau darin steckt das "
 "Quadrat: das eine sagt, **wie viel** Luft ankommt, das andere, **wie "
 "schnell** sie ist. Doppelter Wind bringt doppelt so viel Luft mit "
 "doppelter Geschwindigkeit — also die vierfache Kraft.\n\n"
 "Genauer gerechnet wird die Luft nicht vollständig gestoppt, sondern "
 "umgelenkt; aus der Energiebilanz fällt die Hälfte heraus, und die "
 "Form der Fläche steckt in `c`:\n\n"
 "`q = ½ ρ v²`  und  `F = c · q · A`\n\n"
 "Aus 4 Bft (rund 6,7 m/s) werden in der Bö 8 Bft (rund 18,9 m/s): "
 "`(18,9 / 6,7)² ≈ 8`. Das ist das Vier- bis Neunfache der Regel — "
 "und der Grund, warum eine Bö ein Boot legt, das bei stetigem Wind "
 "derselben Stärke ruhig segelt."
)

DONNER = (
 "## Woher „durch drei“ kommt\n\n"
 "`d` Entfernung des Blitzes, km. `t` Zeit zwischen Blitz und Donner, s. "
 "`c` Schallgeschwindigkeit, rund 343 m/s bei 20 °C.\n\n"
 "Licht braucht für zehn Kilometer 33 Millionstel Sekunden. Gegen eine "
 "Zählzeit von Sekunden ist das nichts — der Blitz ist da, sobald er "
 "passiert. Was man misst, ist also allein die Laufzeit des Schalls:\n\n"
 "`d = c · t`\n\n"
 "Wie lange braucht der Schall für einen Kilometer? "
 "`t = 1000 m / 343 m/s ≈ 2,9 s`. Auf drei gerundet:\n\n"
 "`d [km] ≈ t [s] / 3`\n\n"
 "Also `12 s / 3 = 4 km`. Genau gerechnet sind es `12 · 0,343 = 4,1 km` "
 "— die Regel schätzt das Gewitter also eher etwas näher, als es ist, "
 "und das ist die richtige Richtung.\n\n"
 "Die Schallgeschwindigkeit hängt an der Temperatur "
 "(`c ≈ 331 + 0,6 · θ` m/s mit `θ` in °C), aber zwischen 0 °C "
 "und 30 °C ändert sich das nur um ein paar Prozent — weniger, als man "
 "beim Zählen ohnehin danebenliegt. Wichtiger: gezählt wird bis zum "
 "**ersten** Donner, nicht bis zum lautesten."
)

SEKTOREN = (
 "## Woher 112,5 und 135 kommen\n\n"
 "Alle Winkel vom Boot aus gemessen, 0° ist genau voraus.\n\n"
 "Ein Seitenlicht soll von vorn bis „ein Stück hinter querab“ zu "
 "sehen sein. Von voraus bis querab sind es 90°, und dazu kommen die "
 "klassischen **zwei Kompassstriche**. Ein Strich ist der "
 "zweiunddreißigste Teil des Vollkreises, also `360° / 32 = 11,25°`; "
 "zwei Striche sind `22,5°`. Zusammen:\n\n"
 "`90° + 22,5° = 112,5°` je Seite\n\n"
 "Das Hecklicht füllt genau den Rest auf, damit rundum kein Loch bleibt:\n\n"
 "`360° − 2 · 112,5° = 135°`\n\n"
 "Das sind 67,5° nach jeder Seite. Und das Topplicht deckt beide "
 "Seitenlichter zusammen ab: `2 · 112,5° = 225°`.\n\n"
 "Damit ist auch die Überholregel erklärt: Überholer ist, wer aus "
 "mehr als 22,5° achterlicher als querab aufkommt — also genau aus dem "
 "Sektor, in dem man nachts nur das weiße Hecklicht sieht und kein "
 "farbiges Licht. Die Regel ist nicht zusätzlich definiert, sie ist "
 "dieselbe Geometrie."
)


# Fragetext -> Herleitung. Der Text muss mit dem in fragen.py bzw. kurs.py
# wortgleich sein; tools/make-kurs.py bricht ab, wenn ein Schluessel ins
# Leere zeigt.
HERLEITUNGEN = {
 "Wofür ist der Anker ausgelegt?": ANKER,
 "Wassertiefe 4 m, Faustregel: fünffache Länge. Wie viel Kette und Leine "
 "steckst du?": ANKER,
 "Ein Boot hat 2,4 t Verdrängung. Wie viele Kubikmeter Wasser verdrängt es "
 "in Süßwasser (1 t je m³)?": VERDRAENGUNG,
 "Du segelst am Wind und musst 6 km gegen den Wind zurücklegen. Um welchen "
 "Faktor wird der tatsächliche Weg beim Kreuzen ungefähr länger?": KREUZEN,
 "Was ist der Wendewinkel eines typischen Tourenbootes?": WENDEWINKEL,
 "Bei welchem Kurs steht das Segel etwa 45 Grad zur Mittschiffslinie?":
   SEGELWINKEL,
 "Wie viele m/s sind etwa 20 Knoten?": KNOTEN,
 "Wie viele km/h sind ungefähr 5 m/s?": KMH,
 "Bei welcher Windstärke in Beaufort bleiben Jollen üblicherweise im Hafen?":
   BEAUFORT,
 "Um welchen Faktor kann der Wind in einer Gewitterbö zunehmen?": STAUDRUCK,
 "Welche Faustregel gibt es für die Entfernung eines Gewitters?": DONNER,
 "Zwischen Blitz und Donner vergehen 12 Sekunden. Wie weit ist das Gewitter?":
   DONNER,
 "Welchen Horizontbogen deckt ein Seitenlicht ab?": SEKTOREN,
 "Welchen Bogen deckt das Hecklicht ab?": SEKTOREN,
 "Welche Farbe hat das Topplicht?": SEKTOREN,
}


# Fragetext -> Skizze. Gezeichnet von tools/skizzen.py, zweisprachig.
SKIZZEN = {
 "Wofür ist der Anker ausgelegt?": "skizze-anker",
 "Wassertiefe 4 m, Faustregel: fünffache Länge. Wie viel Kette und Leine "
 "steckst du?": "skizze-anker",
 "Du segelst am Wind und musst 6 km gegen den Wind zurücklegen. Um welchen "
 "Faktor wird der tatsächliche Weg beim Kreuzen ungefähr länger?":
   "skizze-kreuzen",
 "Was ist der Wendewinkel eines typischen Tourenbootes?": "skizze-kreuzen",
 "Um welchen Faktor kann der Wind in einer Gewitterbö zunehmen?":
   "skizze-staudruck",
 "Welche Faustregel gibt es für die Entfernung eines Gewitters?":
   "skizze-donner",
 "Zwischen Blitz und Donner vergehen 12 Sekunden. Wie weit ist das Gewitter?":
   "skizze-donner",
 "Welchen Horizontbogen deckt ein Seitenlicht ab?": "skizze-sektoren",
 "Welchen Bogen deckt das Hecklicht ab?": "skizze-sektoren",
 "Welche Farbe hat das Topplicht?": "skizze-sektoren",
}
