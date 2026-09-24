Segelschein 2.5 — der Kurs auf Englisch

**Alle 1694 Texte übersetzt.** Kapitel, Lektionen, alle 291 Aufgaben mit
Antworten und Begründungen, die Einstufung und die Herleitungen. Der
Sprachschalter erscheint auf der Startseite, weil `sprachen` jetzt
`["de", "en"]` ist — vorher hat der Erzeuger Englisch bewusst nicht
angeboten, solange es unvollständig war.

**Zu den Fachwörtern:** Die Prüfung ist deutsch, und wer sie ablegt, muss
die deutschen Wörter können. Deshalb steht in der englischen Fassung bei
jedem Fachwort das deutsche in Klammern dahinter — „windward (Luv)",
„tacking (Wende)", „clew (Schothorn)". Ein englischer Segler auf einem
deutschen Binnensee hört „Luv" und nicht „windward"; wer den Kurs auf
Englisch liest, soll die Prüfungsbegriffe trotzdem mitnehmen.

Der Erzeuger bricht ab, wenn eine Übersetzung fehlt, und bietet Englisch
erst an, wenn es vollständig ist. `data/fehlt.json` ist verschwunden.

**Neu: die Formeln stehen zweimal da** — oben die Zeile, wie sie im
Lehrtext vorkommt, darunter dieselbe Sache gesetzt, und dazu, woher sie
kommt und wo sie aufhört zu gelten:

    L = T / sin α           wie viel Kette der Anker braucht
    s = d / cos β           der Umweg beim Kreuzen

Fünf Formeln in vier Lektionen: Ankerkette, Kreuzen, Winddruck,
Seemeile und Knoten, Entfernung des Gewitters.

Gesetzt wird beim Bauen mit `tools/formeln.py` (matplotlib.mathtext in
Computer Modern, also ohne TeX-Installation); das Gerät zeigt nur ein PNG,
auf Sailfish vom Thema eingefärbt. Die Formeln stehen in
`kursformeln.py`, nach Lektion geordnet.

**Pakete**

* `segelschein_2.8_armel.deb` — Nokia N9 / N950, `dpkg -i`
* `harbour-segelschein-1.5.0-1.aarch64.rpm` und `…armv7hl.rpm` — Sailfish
