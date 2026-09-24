# -*- coding: utf-8 -*-
"""Die Formeln des Kurses, zweimal aufgeschrieben.

Oben die Zeile so, wie sie im Lehrtext oder in der Herleitung vorkommt,
darunter dieselbe Sache gesetzt. Dazu, woher sie kommt und wo sie aufhoert
zu gelten -- eine Faustformel, die man nur auswendig kann, haelt genau so
lange, wie die Lage zum Lehrbuch passt.

Gesetzt werden die Formeln beim Bauen, siehe tools/formeln.py.
"""
from __future__ import unicode_literals


# Was die Zeichen bedeuten, je Formel -- gefunden ueber den Untertitel.
# Jedes Formelzeichen wird definiert, mit Bedeutung und Einheit, bevor es
# auftaucht: Der Kasten steht fuer sich, und wer ihn beim Durchblaettern
# zuerst sieht, hat den Text darueber noch nicht gelesen.
ZEICHEN = {
 "Wie viel Kette der Anker braucht":
   "`L` gesteckte Länge von Kette und Leine, m. `T` Wassertiefe plus "
   "Freibord, also von der Klampe bis zum Grund, m. `α` Zugwinkel am "
   "Ankerschaft gegen den Grund, Grad.",
 "Der Umweg beim Kreuzen":
   "`s` tatsächlich gesegelter Weg, km. `d` Weg in Windrichtung, den man "
   "gutmacht (Luftlinie), km. `β` Kurs zum Wind, Grad.",
 "Winddruck wächst mit dem Quadrat":
   "`F` Kraft auf die Fläche, N. `q` Staudruck, Pa. `ρ` Luftdichte, "
   "1,225 kg/m³. `v` Windgeschwindigkeit, m/s. `A` angeströmte Fläche, m². "
   "`c` Formzahl, dimensionslos.",
 "Warum eine Seemeile ausgerechnet 1852 m hat":
   "`sm` Seemeile, eine Bogenminute des Erdumfangs. `kn` Knoten, also eine "
   "Seemeile je Stunde.",
 "Wie weit das Gewitter weg ist":
   "`d` Entfernung des Blitzes, km. `t` Zeit zwischen Blitz und Donner, s. "
   "Die Schallgeschwindigkeit ist 343 m/s.",
}


# Welche Skizze zu welcher Formel gehoert; gezeichnet von tools/skizzen.py.
SKIZZEN = {
 "Wie viel Kette der Anker braucht": "skizze-anker",
 "Der Umweg beim Kreuzen": "skizze-kreuzen",
 "Winddruck wächst mit dem Quadrat": "skizze-staudruck",
 "Wie weit das Gewitter weg ist": "skizze-donner",
}


def formel(zeile, tex, untertitel, erklaerung, zeichen="", skizze=""):
    return {"code": zeile, "tex": tex, "untertitel": untertitel,
            "erklaerung": erklaerung,
            "zeichen": zeichen or ZEICHEN.get(untertitel, ""),
            "skizze": skizze or SKIZZEN.get(untertitel, "")}


KURSFORMELN = {

    "b-teile": [
        formel(
            "L = T / sin α",
            r"$L = \frac{T}{\sin\alpha}$",
            "Wie viel Kette der Anker braucht",
            "Ein Anker hält nicht durch sein Gewicht, sondern weil sich die "
            "Flunke eingräbt -- und das tut sie nur, wenn der Zug am Schaft "
            "möglichst waagrecht ankommt. Damit ist es reine Geometrie: Die "
            "gesteckte Länge ist die Hypotenuse, die Tiefe die Gegenkathete "
            "des Zugwinkels. Bei gerade noch tragbaren 20° kommt `2,9 × T` "
            "heraus, auf der sicheren Seite bei 12° `4,8 × T` -- daher die "
            "Spanne **drei bis fünf**. Sie ist keine Konvention, sondern "
            "zwei Winkel in einer Sinusfunktion."),
    ],

    "k-kurse": [
        formel(
            "s = d / cos β",
            r"$s = \frac{d}{\cos\beta}$",
            "Der Umweg beim Kreuzen",
            "Von jedem gesegelten Meter kommt nur die Komponente in "
            "Windrichtung an, und das ist die Ankathete: `d = s · cos β`. "
            "Umgekehrt gelesen kostet ein Kurs von 45° zum Wind den Faktor "
            "`1/cos 45° = 1,41`. Der Faktor hängt **nur** am Kurs zum Wind, "
            "nicht an der Zahl der Schläge: Zwei lange Schläge sind genauso "
            "weit wie zwanzig kurze. Wer 40° fährt, zahlt 1,31, wer nur 50° "
            "schafft, 1,56 -- fünf Grad höher am Wind sparen mehr Weg, als "
            "die meisten glauben."),
    ],

    "w-wind": [
        formel(
            "F = q · A · c = ½ · ρ · v² · A · c",
            r"$F = \frac{1}{2}\rho v^{2} A\,c$",
            "Winddruck wächst mit dem Quadrat",
            "Je Sekunde trifft die Masse `ρ·A·v` auf die Fläche, jedes "
            "Kilogramm bringt `½v²` an Bewegungsenergie mit; Leistung durch "
            "Geschwindigkeit ist Kraft. Übrig bleibt der Staudruck `½ρv²`, "
            "mal Fläche, mal einer Formzahl. Entscheidend ist das Quadrat: "
            "**Doppelte Windgeschwindigkeit heißt vierfache Kraft.** "
            "Deshalb ist der Sprung von 4 auf 6 Beaufort keine Steigerung "
            "um die Hälfte, sondern gut das Vierfache an Druck im Tuch -- "
            "und deshalb reffen erfahrene Segler früher, als es sich "
            "anfühlt."),
        formel(
            "1 kn = 1,852 km/h = 0,514 m/s",
            r"$1\,\mathrm{kn} = 1{,}852\,\mathrm{km/h} \approx 0{,}51\,\mathrm{m/s}$",
            "Warum eine Seemeile ausgerechnet 1852 m hat",
            "Die Seemeile ist keine willkürliche Länge, sondern eine "
            "**Bogenminute** auf dem Erdumfang: 40 007 km geteilt durch "
            "360 × 60 Minuten ergibt 1,852 km. Deshalb entspricht auf der "
            "Seekarte ein Breitengradstrich von einer Minute genau einer "
            "Seemeile -- man misst Entfernungen am seitlichen Kartenrand, "
            "nie am oberen. Ein Knoten ist eine Seemeile je Stunde, also "
            "1,852 / 3,6 = 0,514 m/s."),
    ],

    "w-gewitter": [
        formel(
            "d [km] ≈ t [s] / 3",
            r"$d\,[\mathrm{km}] \approx t\,[\mathrm{s}]\,/\,3$",
            "Wie weit das Gewitter weg ist",
            "Das Licht ist praktisch sofort da, der Schall braucht "
            "343 m/s -- für einen Kilometer also rund 2,9 Sekunden. Zählt "
            "man die Sekunden zwischen Blitz und Donner und teilt durch "
            "drei, steht die Entfernung in Kilometern da. **Wo es eng "
            "wird:** unter 15 Sekunden ist die Zelle keine fünf Kilometer "
            "entfernt, und ein Blitz kann aus dem Amboss auch weit vor der "
            "Regenwand einschlagen. Dann gehört das Boot an Land, nicht auf "
            "den See."),
    ],
}
