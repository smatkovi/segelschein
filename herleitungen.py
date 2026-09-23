# -*- coding: utf-8 -*-
"""Die Herleitung jeder Formel des Kurses.

Drei Regeln fuer jeden Eintrag:

1. **Jedes Formelzeichen wird definiert**, mit Bedeutung und Einheit,
   bevor es auftaucht.
2. **Jede Formel wird hergeleitet** -- auch die, die erst in einer
   Herleitung auftaucht. Eine Begruendung, die ihrerseits eine
   unbegruendete Formel benutzt, hat nichts erklaert, sondern nur
   verschoben. Deshalb steht der Staudruck hier ausgerechnet.
3. **Jede sagt, wo sie aufhoert zu gelten.** Wer weiss, WORAUS die drei-
   bis fuenffache Kettenlaenge kommt, weiss auch, wann sie nicht reicht.
"""
from __future__ import unicode_literals

HERLEITUNGEN = {

"b-teile":
    "## Formelzeichen\n\n"
    "`T` Wassertiefe unter dem Bug, m — genauer: Tiefe plus Freibord, "
    "also der Hoehenunterschied zwischen Klampe und Grund. "
    "`L` gesteckte Laenge von Kette und Leine, m. `α` Zugwinkel am "
    "Ankerschaft gegen den Grund, Grad.\n\n"
    "## Herleitung: warum das Drei- bis Fuenffache der Wassertiefe\n\n"
    "Ein Anker haelt nicht durch sein Gewicht, sondern weil sich seine "
    "Flunke in den Grund graebt. Eingraben tut sie sich nur, wenn der Zug "
    "am Schaft moeglichst **waagrecht** ankommt. Zieht die Kette schraeg "
    "nach oben, kippt der Anker aus und rutscht.\n\n"
    "Damit ist es reine Geometrie. Die gesteckte Laenge `L` ist die "
    "Hypotenuse des Dreiecks aus Klampe, Anker und dem Punkt senkrecht "
    "unter der Klampe; die Hoehe `T` ist die Gegenkathete des Zugwinkels "
    "`α`:\n\n"
    "    sin α = T / L      →      L = T / sin α\n\n"
    "Jetzt setzt man ein, was der Anker noch vertraegt. Ein gerade noch "
    "tragbarer Zugwinkel von 20°:\n\n"
    "    L = T / sin 20° = T / 0,342 ≈ 2,9 × T\n\n"
    "und fuer die sichere Seite, rund 12°:\n\n"
    "    L = T / sin 12° = T / 0,208 ≈ 4,8 × T\n\n"
    "Daher die Spanne **drei bis fuenf**. Sie ist keine Konvention, "
    "sondern zwei Winkel in einer Sinusfunktion.\n\n"
    "**Warum Kette besser haelt als Leine.** Eine schwere Kette haengt in "
    "der Mitte durch. Dieser Bauch liegt tiefer als die gerade "
    "Verbindung, und dadurch kommt der Zug am Anker noch flacher an als "
    "die Rechnung oben annimmt — die wirksame Kettenlaenge ist also "
    "groesser als die geometrische. Leine hat dieses Gewicht nicht; "
    "deshalb steckt man bei Leine eher das Siebenfache.\n\n"
    "**Und warum mehr bei Wind.** Der Zug waechst mit dem Quadrat der "
    "Windgeschwindigkeit (siehe das Kapitel Wetter). Doppelter Wind heisst "
    "vierfacher Zug, der die Kette strafft, den Bauch herauszieht und den "
    "Winkel vergroessert. Genau dann braucht man die Laenge.",

"k-kurse":
    "## Formelzeichen\n\n"
    "`s` tatsaechlich gesegelter Weg, km. `d` Weg in Windrichtung, den "
    "man gutmacht (Luftlinie), km. `β` Kurs zum Wind, Grad — wie hoch "
    "das Boot an den Wind geht.\n\n"
    "## Herleitung: woher der Faktor 1,4 beim Kreuzen kommt\n\n"
    "Gegen den Wind geht nicht geradeaus. Ein Boot am Wind faehrt etwa "
    "`β = 45°` zur Windrichtung, also schraeg zu der Linie, die es "
    "eigentlich zuruecklegen will.\n\n"
    "Von jedem gesegelten Meter kommt nur die Komponente in Windrichtung "
    "an. Das ist die Ankathete im rechtwinkligen Dreieck:\n\n"
    "    d = s · cos β\n\n"
    "Umgekehrt gelesen — fuer einen gewuenschten Fortschritt `d` muss man "
    "segeln:\n\n"
    "    s = d / cos β = d / cos 45° = d / 0,707 = 1,41 · d\n\n"
    "Aus 6 km Luftlinie werden also gut 8,5 km — **unabhaengig davon, wie "
    "oft man wendet.** Der Faktor haengt nur an β, nicht an der Zahl der "
    "Schlaege: Zwei lange Schlaege sind genauso weit wie zwanzig kurze. "
    "Die Wenden kosten nur zusaetzlich Fahrt, nicht Weg.\n\n"
    "**Wer hoeher kann, gewinnt doppelt.** Bei 40° Kurs zum Wind ist der "
    "Faktor 1/cos 40° = 1,31, bei 50° schon 1,56. Fuenf Grad hoeher am "
    "Wind sparen mehr Weg, als fuenf Grad mehr Fahrt einbringen.\n\n"
    "**Wo die Rechnung endet:** Sie unterstellt stillstehendes Wasser. "
    "Mit Strom kommt ein Vektor dazu, und dann ist der guenstigste Schlag "
    "nicht mehr der symmetrische.",

"w-wind":
    "## Formelzeichen\n\n"
    "`ρ` Luftdichte, kg/m³; rund 1,225 in Meereshoehe. `v` "
    "Windgeschwindigkeit, m/s. `A` angestroemte Flaeche, m². `q` "
    "Staudruck, Pa. `F` Kraft auf das Segel, N. `c` Beiwert des Segels, "
    "dimensionslos.\n\n"
    "## Herleitung: der Staudruck\n\n"
    "Luft, die auf das Segel trifft und dort abgebremst wird, gibt ihre "
    "Bewegungsenergie ab. Je Sekunde trifft die Masse `ρ·A·v` auf die "
    "Flaeche `A`, und jedes Kilogramm bringt `½v²` an Energie mit. "
    "Leistung ist Energie je Zeit, Kraft ist Leistung durch "
    "Geschwindigkeit:\n\n"
    "    Leistung = (ρ·A·v) · ½v²\n"
    "    Kraft    = Leistung / v = ½·ρ·v²·A\n\n"
    "Druck ist Kraft durch Flaeche:\n\n"
    "    q = ½·ρ·v²\n\n"
    "Die Probe auf die Einheiten: kg/m³ · m²/s² = kg/(m·s²) = N/m² = Pa.\n\n"
    "## Und daraus: warum doppelter Wind vierfache Kraft bedeutet\n\n"
    "Die Kraft auf das Segel ist dieser Druck mal Flaeche mal einem "
    "Beiwert, der beschreibt, wie das Segel steht:\n\n"
    "    F = q · A · c = ½ · ρ · v² · A · c\n\n"
    "Alles darin ist fest ausser `v`. Also gilt schlicht\n\n"
    "    F ∝ v²\n\n"
    "Verdoppelt sich der Wind von 10 auf 20 Knoten, vervierfacht sich die "
    "Kraft. Verdreifacht er sich, ist es das Neunfache.\n\n"
    "**Deshalb ist die Beaufort-Skala nicht linear.** Sie zaehlt nicht "
    "Geschwindigkeit, sondern Wirkung. Der Sprung von 4 auf 5 Beaufort "
    "sind rund 5 auf 8 m/s — also Faktor 1,6 in der Geschwindigkeit, aber "
    "**2,6 in der Kraft**. Fuer eine Jolle ist das der Unterschied "
    "zwischen einem schoenen Tag und einem, der reffen verlangt.\n\n"
    "## Die Umrechnungen, und woher sie kommen\n\n"
    "**m/s in km/h:** Eine Stunde hat 3600 Sekunden, ein Kilometer 1000 "
    "Meter. Also\n\n"
    "    km/h = m/s × 3600/1000 = m/s × 3,6\n\n"
    "**Knoten:** Ein Knoten ist eine Seemeile je Stunde, und die Seemeile "
    "ist eine Bogenminute auf einem Grosskreis der Erde. Der Erdumfang "
    "betraegt rund 40 007 km, ein Grosskreis hat 360 Grad zu je 60 "
    "Minuten:\n\n"
    "    1 sm = 40 007 / (360 × 60) = 1,852 km\n"
    "    1 kn = 1,852 km/h = 1,852 / 3,6 = 0,514 m/s\n\n"
    "Im Kopf: **Knoten halbieren gibt ungefaehr m/s** (0,5 statt 0,514, "
    "also 3 % zu wenig).",

"w-gewitter":
    "## Formelzeichen\n\n"
    "`c` Schallgeschwindigkeit, m/s; rund 343 bei 20 °C. `t` gezaehlte "
    "Zeit zwischen Blitz und Donner, s. `d` Entfernung, km.\n\n"
    "## Herleitung: warum Sekunden durch drei\n\n"
    "Das Licht des Blitzes ist praktisch sofort da — 300 000 km in der "
    "Sekunde, also fuer jede denkbare Entfernung unter einer "
    "Millisekunde. Der Donner ist Schall und braucht seine Zeit. Weg ist "
    "Geschwindigkeit mal Zeit:\n\n"
    "    d = c · t\n\n"
    "Fuer einen Kilometer braucht der Schall also\n\n"
    "    t = 1000 m ÷ 343 m/s ≈ 2,9 s\n\n"
    "aufgerundet **drei Sekunden je Kilometer**. Umgestellt:\n\n"
    "    d [km] ≈ t [s] / 3\n\n"
    "Neun Sekunden sind drei Kilometer.\n\n"
    "**Warum 343 und nicht etwas anderes.** Die Schallgeschwindigkeit in "
    "Luft haengt nur von der Temperatur ab, nicht vom Druck: rund "
    "331 + 0,6 · T[°C] m/s. Bei 0 °C sind es 331, bei 20 °C 343, bei "
    "30 °C 349. Fuer die Faustregel ist der Unterschied belanglos.\n\n"
    "**Was die Zahl wert ist.** Sie sagt, wo der Blitz war, nicht wo der "
    "naechste sein wird. Eine Gewitterzelle zieht mit 30 bis 60 km/h; in "
    "den drei Minuten, die man zum Nachdenken braucht, kommt sie zwei "
    "Kilometer naeher. Und der Winddruck der Boe waechst mit dem Quadrat "
    "der Geschwindigkeit: Aus 4 Beaufort werden binnen Minuten 8, das ist "
    "**viermal** so viel Kraft im Segel.\n\n"
    "Deshalb ist die praktische Regel nicht „ab drei Kilometern wird "
    "es eng“, sondern: Wer das Gewitter zaehlen kann, haette schon am "
    "Ufer sein sollen.",

}
