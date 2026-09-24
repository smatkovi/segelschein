# Segelschein

Theorie für den **Segelschein A (Binnen)** auf dem Nokia N9 und N950
(MeeGo 1.2 Harmattan) und auf Sailfish OS.

Sieben Kapitel, elf Lektionen, 291 Aufgaben: vom Boot und seinen Teilen über
die Kurse zum Wind, Wende und Halse, die Ausweichregeln, Betonnung und
Lichter bis zu Wetter, Sicherheit und Umweltrecht. Zu jeder Lektion gehören
gezeichnete Schemata — Kurse zum Wind, Vorfahrtsfälle, Tonnen und
Lichterführung —, und was einmal saß, kommt in wachsenden Abständen zur
Wiederholung wieder.

**Die Fragen sind eigene zum Lehrplan, nicht der amtliche Katalog.** Sie
decken denselben Stoff ab, ersetzen aber keine Prüfungsvorbereitung mit den
offiziellen Bögen.

## Wie das gebaut ist

Das Programm ist [C-Lehrer](https://github.com/smatkovi/c-lehrer)
beziehungsweise dessen Sailfish-Fassung
[harbour-lehrer](https://github.com/smatkovi/harbour-lehrer), unverändert:
Die App liest ihren ganzen Kurs aus `data/kurs.json` und weiß nichts vom
Thema. Ein zweiter Kurs ist deshalb ein zweites Paket, kein zweites Programm
— nur Daten, Bilder, Icon und Name unterscheiden sich.

Dieses Repo ist der Kurs:

```
kurs.py            Kapitel, Lektionen, Bildverweise
fragen.py          die Aufgaben, nach Kapiteln
tools/make-kurs.py schreibt data/kurs.json
tools/bilder.py    zeichnet bilder/*.png (Pillow, keine Fotos)
tools/build-deb.sh packt das Harmattan-.deb
```

Die richtige Antwort steht beim Schreiben immer vorne; `make-kurs.py` mischt
deterministisch und zählt danach nach, damit kein Muster entsteht.

## Bauen

```sh
python3 tools/bilder.py          # Schemata zeichnen
python3 tools/make-kurs.py       # data/kurs.json erzeugen
tools/build-deb.sh 3.1           # braucht ~/ps/c-lehrer/build/c-lehrer
```

Die Sailfish-RPMs entstehen im Baum von `harbour-lehrer`
(`cmake -DKURS=segelschein`), wo `kurs.json` und die Bilder als
`kurse/segelschein/` liegen.

## Installieren

* **N9 / N950:** `dpkg -i segelschein_3.1_armel.deb`
* **Sailfish OS:** `pkcon install-local harbour-segelschein-1.0.0-1.<arch>.rpm`

Die Pakete für beide Systeme hängen an den
[Releases](https://github.com/smatkovi/segelschein/releases).
