# -*- coding: utf-8 -*-
"""Fragenbank zum Segelschein A — getrennt vom Lehrtext.

Die Lektionen in kurs.py erklären; hier stehen die Fragen zum Abfragen. Die
Trennung hat einen praktischen Grund: Der Lehrtext soll lesbar bleiben,
während die Bank auf einige hundert Einträge wächst, und im
Karteikartenmodus ist ohnehin jede Frage für sich unterwegs.

Zugeordnet wird über die Lektionskennung. Der Erzeuger hängt sie an die
Aufgaben der jeweiligen Lektion an.

Eine Regel für alle: **Die richtige Antwort steht hier an erster Stelle.**
Gemischt wird im Erzeuger, deterministisch aus der Fragenkennung — von Hand
gemischt wäre es beim Schreiben nicht durchzuhalten und beim Prüfen nicht
nachzuvollziehen.
"""
from __future__ import unicode_literals

from kurs import mc, zahl


BANK = {

# ===========================================================================
"b-teile": [
    mc("Was bedeutet „Lee\"?",
       ["Die dem Wind abgewandte Seite.",
        "Die dem Wind zugewandte Seite.",
        "Die rechte Seite des Bootes.",
        "Der hintere Teil des Bootes."], 0,
       "Lee wie leer — dorthin bläst der Wind alles hin. Das Segel steht in "
       "Lee, die Mannschaft sitzt in Luv."),
    mc("Steuerbord ist …",
       ["in Fahrtrichtung rechts, Kennfarbe grün.",
        "in Fahrtrichtung links, Kennfarbe rot.",
        "immer die Leeseite.",
        "der Bereich um das Ruder."], 0,
       "Rechts und grün — dieselbe Zuordnung wie bei der Positionslaterne "
       "und der Steuerbordtonne."),
    mc("Wie heißt der vordere Teil des Bootes?",
       ["Bug", "Heck", "Kiel", "Süll"], 0,
       "Vorne Bug, hinten Heck. Die Wörter gelten unabhängig davon, wie man "
       "gerade sitzt."),
    mc("Was ist die Plicht?",
       ["Der offene Sitzbereich, in dem die Mannschaft sitzt.",
        "Die Pflicht zur Rettungsweste.",
        "Der Raum unter Deck.",
        "Die Leine zum Festmachen."], 0,
       "Von „Pflicht\" kommt das Wort nicht, sondern aus dem "
       "Niederdeutschen. Gemeint ist der Arbeitsplatz der Mannschaft."),
    mc("Wozu dient der Baum?",
       ["Er hält das Unterliek des Großsegels.",
        "Er trägt das Vorsegel.",
        "Er stabilisiert den Mast nach vorn.",
        "Er dient zum Anlegen."], 0,
       "Der Baum spannt das Großsegel unten aus. Was den Mast nach vorn "
       "hält, ist das Vorstag."),
    mc("Was ist ein Stag?",
       ["Ein Draht, der den Mast in Längsrichtung hält.",
        "Eine Leine zum Segelsetzen.",
        "Ein Beschlag am Baum.",
        "Der Abstand zwischen zwei Booten."], 0,
       "Vorstag und Achterstag halten den Mast längs, die Wanten quer. "
       "Alles zusammen ist das stehende Gut."),
    mc("Was ist ein Want?",
       ["Ein Draht, der den Mast seitlich hält.",
        "Eine Leine zum Reffen.",
        "Die Wand des Kajütaufbaus.",
        "Ein Teil des Ruders."], 0,
       "Wanten halten den Mast quer, Stagen längs. Beides gehört zum "
       "stehenden Gut, das im Betrieb nicht bewegt wird."),
    mc("Was gehört zum laufenden Gut?",
       ["Fallen und Schoten.", "Wanten und Stagen.",
        "Mast und Baum.", "Ruder und Schwert."], 0,
       "Laufendes Gut wird im Betrieb bewegt: Fallen ziehen Segel hoch, "
       "Schoten stellen sie. Stehendes Gut steht."),
    mc("Womit wird ein Segel dichtgeholt?",
       ["Mit der Schot.", "Mit dem Fall.",
        "Mit dem Stag.", "Mit dem Niederholer."], 0,
       "Schoten stellen den Winkel des Segels zum Wind ein. Fallen ziehen "
       "es nach oben."),
    mc("Was ist das Vorliek eines Segels?",
       ["Die vordere Kante.", "Die hintere Kante.",
        "Die untere Kante.", "Die Ecke am Baum."], 0,
       "Vorliek vorne, Achterliek hinten, Unterliek unten. Das Killen "
       "beginnt immer am Vorliek — daran erkennt man zu offene Schot."),
    mc("Wie heißt die untere vordere Ecke des Großsegels?",
       ["Hals", "Kopf", "Schothorn", "Nock"], 0,
       "Kopf oben, Hals unten vorn, Schothorn unten hinten. Die drei Ecken "
       "eines Dreiecksegels haben eigene Namen, weil dort jeweils etwas "
       "anderes befestigt wird."),
    mc("Was bewirkt der Niederholer?",
       ["Er zieht den Baum nach unten und verhindert, dass er aufsteigt.",
        "Er holt das Segel nieder, also herunter.",
        "Er zieht das Vorsegel dicht.",
        "Er senkt das Schwert ab."], 0,
       "Ohne Niederholer steigt der Baum bei offener Schot auf, das Segel "
       "verdreht sich (twistet) und verliert Kraft im oberen Bereich."),
    mc("Wozu dient das Ruder?",
       ["Zum Steuern, solange Wasser daran vorbeiströmt.",
        "Gegen die seitliche Abdrift.",
        "Zum Bremsen.", "Zur Stabilisierung gegen Krängung."], 0,
       "Das Ruder wirkt nur bei Fahrt durchs Wasser. Ein stehendes Boot "
       "lässt sich nicht steuern — deshalb wird beim Anlegen nie die ganze "
       "Fahrt weggenommen, bevor man liegt."),
    mc("Was ist Krängung?",
       ["Die seitliche Neigung des Bootes.",
        "Die Abdrift nach Lee.",
        "Das Eintauchen des Bugs.",
        "Das Schlingern bei Welle."], 0,
       "Krängung entsteht aus dem seitlichen Anteil der Segelkraft. Ein "
       "wenig ist normal, zu viel kostet Geschwindigkeit und Ruderwirkung."),
    mc("Was tut die Mannschaft bei zunehmender Krängung?",
       ["Sie geht nach Luv, um mit dem Gewicht gegenzuhalten.",
        "Sie geht nach Lee.",
        "Sie setzt sich in die Mitte.",
        "Sie geht nach vorn."], 0,
       "Ausreiten in Luv ist das einfachste Trimmmittel. Reicht das nicht, "
       "wird die Schot gefiert oder gerefft."),
    mc("Was heißt „reffen\"?",
       ["Die Segelfläche verkleinern.",
        "Die Segel bergen.", "Die Schot dichtholen.",
        "Den Mast legen."], 0,
       "Gerefft wird, bevor es nötig ist — im Sturm auf dem Vorschiff zu "
       "arbeiten ist genau das, was man vermeiden wollte."),
    mc("Was ist die Abdrift?",
       ["Das seitliche Versetzen durch den Winddruck.",
        "Das Versetzen durch die Strömung.",
        "Der Vorhaltewinkel.",
        "Die Geschwindigkeit über Grund."], 0,
       "Abdrift kommt vom Wind, Versatz von der Strömung. Gegen die Abdrift "
       "wirkt das Schwert oder der Kiel."),
    mc("Was ist ein Jollenkreuzer im Unterschied zur Jolle?",
       ["Eine Jolle mit Kajüte und meist Ballast im Schwert.",
        "Ein Boot ohne Schwert.",
        "Ein reines Motorboot.",
        "Ein Katamaran."], 0,
       "Die Jolle hat ein aufholbares Schwert ohne nennenswerten Ballast "
       "und kann kentern; der Kielkreuzer richtet sich durch seinen "
       "Ballastkiel wieder auf."),
    mc("Warum kann eine Jolle kentern, ein Kielboot aber kaum?",
       ["Der Ballastkiel richtet das Kielboot wieder auf.",
        "Das Kielboot ist schwerer.",
        "Die Jolle hat mehr Segelfläche.",
        "Das Kielboot liegt tiefer im Wasser."], 0,
       "Entscheidend ist das Gewicht **unten**. Ein Ballastkiel erzeugt mit "
       "zunehmender Krängung ein wachsendes Aufrichtmoment."),
    mc("Was ist zu tun, wenn eine Jolle gekentert ist?",
       ["Am Boot bleiben und über das Schwert aufrichten.",
        "Zum Ufer schwimmen.",
        "Die Segel abschlagen.",
        "Das Schwert einholen."], 0,
       "Das Boot schwimmt, der Mensch wird müde. Es ist außerdem von weitem "
       "sichtbar — am Boot bleiben ist die erste Regel nach dem Kentern."),
    mc("Was ist der Freibord?",
       ["Der Abstand von der Wasserlinie zum Deck.",
        "Die freie Segelfläche.",
        "Der unbelegte Teil des Decks.",
        "Der Abstand zum Nachbarboot."], 0,
       "Je kleiner der Freibord, desto eher kommt Wasser über. Bei "
       "Krängung und Welle ist das die Größe, die über Nässe im Boot "
       "entscheidet."),
    mc("Was ist die Verdrängung eines Bootes?",
       ["Die Masse des verdrängten Wassers, also das Gewicht des Bootes.",
        "Der Tiefgang.",
        "Die Segelfläche.",
        "Die Länge über alles."], 0,
       "Nach Archimedes verdrängt ein schwimmender Körper genau sein "
       "eigenes Gewicht an Wasser."),
    zahl("Ein Boot hat 2,4 t Verdrängung. Wie viele Kubikmeter Wasser "
         "verdrängt es in Süßwasser (1 t je m³)?",
         2.4, "m³",
         "Verdrängung in Tonnen ist in Süßwasser zahlenmäßig gleich dem "
         "Volumen in Kubikmetern. In Salzwasser wäre es etwas weniger, weil "
         "Salzwasser dichter ist.", toleranz=0.05),
    mc("Was ist der Tiefgang?",
       ["Der tiefste Punkt des Bootes unter der Wasserlinie.",
        "Die Höhe des Mastes.",
        "Der Abstand Deck zu Kiel.",
        "Die Wassertiefe unter dem Kiel."], 0,
       "Was unter dem Kiel bleibt, ist der Kielfreiraum. Der Tiefgang ist "
       "eine Eigenschaft des Bootes, nicht des Gewässers."),
    mc("Welche Leine gehört zum Festmachen?",
       ["Die Vor- und Achterleine sowie die Springs.",
        "Fall und Schot.",
        "Wanten und Stagen.",
        "Der Niederholer."], 0,
       "Vorleine und Achterleine halten längs, die Springs verhindern das "
       "Vor- und Zurückrutschen am Steg."),
    mc("Was ist eine Spring?",
       ["Eine Festmacherleine schräg nach vorn oder achtern.",
        "Ein federnder Beschlag am Mast.",
        "Die Leine zum Ankerwerfen.",
        "Ein Sprung im Rumpf."], 0,
       "Ohne Springs wandert das Boot am Steg hin und her, sobald Welle "
       "oder Wind längs stehen."),
    mc("Womit wird das Boot am Steg vor Scheuern geschützt?",
       ["Mit Fendern.", "Mit Springs.",
        "Mit dem Anker.", "Mit dem Schwert."], 0,
       "Fender gehören auf die richtige Höhe — zu hoch hängende Fender "
       "sind die häufigste Ursache für Schrammen am Rumpf."),
    mc("Wofür ist der Anker ausgelegt?",
       ["Zum Halten auf Grund, mit ausreichend Kette und Leine.",
        "Zum Bremsen in Fahrt.",
        "Als Ballast.",
        "Zum Abschleppen."], 0,
       "Entscheidend ist die **Kettenlänge**: Der Anker hält nur, wenn der "
       "Zug waagrecht ankommt. Faustregel ist das Drei- bis Fünffache der "
       "Wassertiefe."),
    zahl("Wassertiefe 4 m, Faustregel: fünffache Länge. Wie viel Kette und "
         "Leine steckst du?",
         20, "m",
         "4 × 5 = 20 m. Bei Wind und Welle eher mehr; bei zu kurzer Länge "
         "zieht der Anker nach oben statt waagrecht und bricht aus.",
         toleranz=0.05),
    mc("Was ist beim Ankern zu beachten?",
       ["Der Schwojkreis muss frei sein.",
        "Der Anker muss senkrecht fallen.",
        "Die Segel bleiben gesetzt.",
        "Das Schwert bleibt unten."], 0,
       "Das Boot dreht sich um den Anker mit dem Wind. Der Kreis mit dem "
       "Radius der gesteckten Länge muss frei von Booten und Untiefen "
       "sein."),
],
}


BANK.update({

# ===========================================================================
"k-kurse": [
    mc("Wie heißt der Kurs, bei dem der Wind schräg von achtern kommt?",
       ["Raumschots", "Am Wind", "Halber Wind", "Vor dem Wind"], 0,
       "Raumschots liegt zwischen halbem Wind und vor dem Wind, also bei "
       "etwa 135 Grad. Das Segel ist weit aufgefiert."),
    mc("Auf welchem Kurs krängt ein Boot am stärksten?",
       ["Am Wind.", "Vor dem Wind.",
        "Raumschots.", "Die Krängung hängt nicht vom Kurs ab."], 0,
       "Am Wind wirkt der größte Anteil der Segelkraft quer zum Boot. Vor "
       "dem Wind drückt sie fast nur nach vorn."),
    mc("Warum ist „vor dem Wind\" nicht der schnellste Kurs?",
       ["Der scheinbare Wind wird durch die eigene Fahrt kleiner.",
        "Das Segel steht ungünstig.",
        "Die Abdrift ist am größten.",
        "Das Ruder wirkt schlechter."], 0,
       "Fährt man mit dem Wind, zieht man ihm davon: Von 6 m/s wahrem Wind "
       "bleiben bei 3 m/s Fahrt nur 3 m/s scheinbarer Wind übrig. Quer zum "
       "Wind addiert sich die Fahrt dagegen vektoriell."),
    mc("Was ist der scheinbare Wind?",
       ["Die Summe aus wahrem Wind und Fahrtwind.",
        "Der Wind in Böen.",
        "Der Wind am Ufer.",
        "Der Wind in Masthöhe."], 0,
       "Der scheinbare Wind ist das, was das Segel und der Verklicker "
       "spüren. Er dreht mit zunehmender Fahrt weiter nach vorn."),
    mc("Der Verklicker zeigt an …",
       ["die Richtung des scheinbaren Windes.",
        "die Windgeschwindigkeit.",
        "den wahren Wind.",
        "den Kurs über Grund."], 0,
       "Er hängt im Wind an Bord, also zeigt er den scheinbaren. Für den "
       "Trimm ist genau der maßgeblich."),
    mc("Was heißt „anluven\"?",
       ["Den Bug näher an den Wind drehen.",
        "Vom Wind wegdrehen.",
        "Die Schot fieren.",
        "In Lee ausweichen."], 0,
       "Anluven geht zum Wind hin, abfallen vom Wind weg. Beim Anluven "
       "muss die Schot dichter genommen werden, sonst killt das Segel."),
    mc("Was heißt „abfallen\"?",
       ["Den Bug vom Wind wegdrehen.",
        "Zum Wind hin drehen.",
        "Die Fahrt verlieren.",
        "Aus dem Boot fallen."], 0,
       "Abfallen ist das Gegenteil von Anluven; dabei wird die Schot "
       "gefiert, sonst krängt das Boot unnötig."),
    mc("Beim Anluven killt das Segel. Was tust du?",
       ["Schot dichtnehmen.", "Schot fieren.",
        "Weiter anluven.", "Schwert aufholen."], 0,
       "Je näher am Wind, desto dichter das Segel. Wer anluvt ohne "
       "dichtzunehmen, verliert Vortrieb und Fahrt."),
    mc("Was bewirkt zu dicht geholte Schot am Wind?",
       ["Das Boot krängt stärker und wird langsamer.",
        "Das Segel killt.",
        "Das Boot luvt von allein an.",
        "Nichts Nennenswertes."], 0,
       "Übertrimmt man, wächst der Querdruck ohne Gewinn an Vortrieb. Die "
       "Regel bleibt: aufmachen bis es killt, dann gerade dichtnehmen."),
    mc("Wie prüft man den Trimm mit Wollfäden?",
       ["Beide Seiten sollen waagrecht nach achtern strömen.",
        "Der Luvfaden soll flattern.",
        "Der Leefaden soll flattern.",
        "Beide sollen nach oben zeigen."], 0,
       "Strömen beide glatt, liegt die Strömung an beiden Seiten an. "
       "Flattert der Luvfaden, ist die Schot zu offen oder man ist zu hoch "
       "am Wind."),
    mc("Was bedeutet „in den Wind schießen\"?",
       ["Den Bug in den Wind drehen, bis die Segel killen und das Boot "
        "aufstoppt.",
        "Vor dem Wind beschleunigen.",
        "Eine Halse einleiten.",
        "Den Anker werfen."], 0,
       "Das ist die Bremse eines Segelbootes und die Grundlage jedes "
       "Anlegemanövers unter Segeln: Es gibt keine andere Möglichkeit, "
       "kontrolliert stehenzubleiben."),
    mc("Ein Segelboot hat keine Bremse. Wie hält man an?",
       ["Man schießt in den Wind.",
        "Man wirft den Anker.",
        "Man fiert die Schoten und wartet.",
        "Man dreht vor den Wind."], 0,
       "Nur im Wind steht das Boot ohne Vortrieb. Schoten fieren allein "
       "genügt nicht — das Boot treibt weiter."),
    mc("Was ist der Wendewinkel eines typischen Tourenbootes?",
       ["etwa 90 Grad", "etwa 45 Grad",
        "etwa 180 Grad", "etwa 30 Grad"], 0,
       "Von 45 Grad auf dem einen Bug zu 45 Grad auf dem anderen sind es "
       "rund 90 Grad Kursänderung."),
    zahl("Du segelst am Wind und musst 6 km gegen den Wind zurücklegen. Um "
         "welchen Faktor wird der tatsächliche Weg beim Kreuzen ungefähr "
         "länger?",
         1.4, "mal",
         "Bei 45 Grad Kurs zum Wind ist der Weg etwa 1/cos(45°) ≈ 1,41 mal "
         "so lang. Aus 6 km werden also gut 8,5 km — und entsprechend mehr "
         "Zeit.", toleranz=0.12),
    mc("Warum braucht ein Segelboot ein Schwert oder einen Kiel?",
       ["Sonst würde der Winddruck es seitwärts abtreiben.",
        "Zur Stabilisierung gegen Wellen.",
        "Um den Tiefgang zu erhöhen.",
        "Für die Steuerung."], 0,
       "Die Segelkraft wirkt großenteils quer. Erst der Widerstand des "
       "Schwerts gegen die Querbewegung macht daraus Vortrieb."),
    mc("Wann wird das Schwert aufgeholt?",
       ["Auf Raumschots- und Vorwindkursen sowie im Flachwasser.",
        "Immer am Wind.",
        "Bei starkem Wind.",
        "Nie."], 0,
       "Vor dem Wind gibt es kaum Querkraft, also braucht es kein Schwert — "
       "und es kostet Widerstand. Im Flachwasser ist es ohnehin oben."),
    mc("Wie entsteht der Vortrieb am Segel physikalisch?",
       ["Durch Druckunterschied zwischen Luv- und Leeseite, wie an einem "
        "Flügel.",
        "Nur durch den Staudruck von hinten.",
        "Durch Reibung der Luft am Tuch.",
        "Durch die Krängung."], 0,
       "Am Wind wirkt das Segel als Profil: Auf der Leeseite entsteht "
       "Unterdruck. Nur vor dem Wind arbeitet es tatsächlich als Widerstand."),
    mc("Was ist das Lateralzentrum?",
       ["Der Angriffspunkt der seitlichen Kräfte am Unterwasserschiff.",
        "Der Schwerpunkt des Bootes.",
        "Der Angriffspunkt der Segelkräfte.",
        "Die Mitte des Rumpfes."], 0,
       "Liegt der Segeldruckpunkt hinter dem Lateralzentrum, luvt das Boot "
       "von allein an — die Luvgierigkeit."),
    mc("Ein Boot ist stark luvgierig. Was hilft?",
       ["Großsegel fieren oder reffen, Vorsegel dichter.",
        "Großsegel dichter nehmen.",
        "Vorsegel bergen.",
        "Schwert aufholen."], 0,
       "Das Großsegel wirkt achtern und luvt an, das Vorsegel wirkt vorn "
       "und fällt ab. Wer Krängung abbaut, verringert die Luvgierigkeit "
       "ebenfalls."),
    mc("Warum luvt ein Boot bei starker Krängung von allein an?",
       ["Die Rumpfform wird asymmetrisch und drückt den Bug in den Wind.",
        "Das Ruder wirkt stärker.",
        "Der Wind dreht.",
        "Das Schwert greift tiefer."], 0,
       "Das gekrängte Unterwasserschiff ist nicht mehr symmetrisch. "
       "Deshalb ist aufrecht segeln nicht nur bequemer, sondern auch "
       "schneller."),
    mc("Was ist eine Bö?",
       ["Eine kurzzeitige Verstärkung des Windes, oft mit Richtungsänderung.",
        "Ein stetiger Wind über 6 Beaufort.",
        "Ein Wind vom Ufer.",
        "Ein Wirbel hinter dem Segel."], 0,
       "Böen kommen meist etwas raumer herein. Man erkennt sie auf dem "
       "Wasser an der dunklen, gekräuselten Fläche — rechtzeitig sichtbar, "
       "wenn man hinsieht."),
    mc("Wie reagiert man in einer Bö am Wind?",
       ["Anluven und Großschot fieren.",
        "Abfallen und dichtnehmen.",
        "Kurs halten.",
        "Schwert aufholen."], 0,
       "Anluven verringert den Anstellwinkel, Fieren die Kraft. Abfallen "
       "würde die Krängung noch vergrößern."),
    mc("Was ist ein Raumschotskurs im Vergleich zu halbem Wind?",
       ["Weiter vom Wind weg, das Segel ist weiter aufgefiert.",
        "Näher am Wind.",
        "Dasselbe.",
        "Genau gegen den Wind."], 0,
       "Halber Wind 90 Grad, raumschots etwa 135 Grad."),
    mc("Auf welchem Kurs ist die Patenthalse am ehesten zu befürchten?",
       ["Vor dem Wind.", "Am Wind.",
        "Halber Wind.", "Beim Aufschießer."], 0,
       "Vor dem Wind genügt ein kleines Abfallen oder eine Welle, und der "
       "Wind kommt auf die andere Seite des Segels."),
    mc("Wie verhindert man eine Patenthalse wirksam?",
       ["Mit einem Bullenstander, der den Baum nach vorn hält.",
        "Durch dichtere Schot.",
        "Durch Aufholen des Schwerts.",
        "Durch mehr Fahrt."], 0,
       "Der Bullenstander läuft vom Baum nach vorn an Deck und hält ihn "
       "fest — auf längeren Vorwindstrecken gehört er gesetzt."),
    mc("Was ist ein Spinnaker?",
       ["Ein großes, bauchiges Vorsegel für raume Kurse.",
        "Ein Sturmsegel.",
        "Ein zweites Großsegel.",
        "Die Persenning."], 0,
       "Er zieht nur mit dem Wind von achtern und verlangt Übung — bei viel "
       "Wind ist er das Segel, das Anfängern die Kontrolle nimmt."),
    mc("Was bedeutet „killen\" eines Segels?",
       ["Es flattert, weil die Strömung abreißt.",
        "Es reißt ein.",
        "Es wird geborgen.",
        "Es steht zu dicht."], 0,
       "Killen beginnt am Vorliek und ist das Zeichen, dass die Schot zu "
       "offen oder der Kurs zu hoch ist."),
    mc("Bei welchem Kurs steht das Segel etwa 45 Grad zur Mittschiffslinie?",
       ["Halber Wind.", "Am Wind.",
        "Vor dem Wind.", "In der Sperrzone."], 0,
       "Grobe Regel: Der Segelwinkel ist etwa halb so groß wie der "
       "Kurswinkel zum Wind. Bei 90 Grad Kurs also etwa 45 Grad Segel."),
    mc("Warum ist es sinnvoll, den Trimm nach dem Kurswechsel neu zu "
       "prüfen?",
       ["Weil sich mit dem Kurs auch der scheinbare Wind ändert.",
        "Weil die Schot sich lockert.",
        "Weil das Segel ausleiert.",
        "Das ist nicht nötig."], 0,
       "Jede Kursänderung ändert Richtung und Stärke des scheinbaren "
       "Windes — und damit den richtigen Segelstand."),
],

# ===========================================================================
"m-wende": [
    mc("Wie lautet das Ankündigungskommando zur Wende?",
       ["„Klar zur Wende?\"", "„Rund achtern!\"",
        "„Ree!\"", "„Klar zur Halse?\""], 0,
       "Erst die Frage, dann auf die Antwort „ist klar\" das "
       "Ausführungskommando „Ree!\"."),
    mc("Wie lautet das Ausführungskommando zur Wende?",
       ["„Ree!\"", "„Rund achtern!\"",
        "„Klar zur Wende?\"", "„Fall weg!\""], 0,
       "„Ree\" kommt von Ruder in Lee — historisch die Bewegung, mit der "
       "die Wende eingeleitet wurde."),
    mc("Wie lautet das Ausführungskommando zur Halse?",
       ["„Rund achtern!\"", "„Ree!\"",
        "„Klar zur Halse?\"", "„Baum über!\""], 0,
       "Die Halse geht rund achtern — das Heck durch den Wind."),
    mc("Womit beginnt eine Wende aus dem Am-Wind-Kurs?",
       ["Mit etwas Fahrt aufnehmen, dann zügig anluven.",
        "Mit dem Fieren der Großschot.",
        "Mit dem Aufholen des Schwerts.",
        "Mit dem Bergen des Vorsegels."], 0,
       "Ohne Fahrt bleibt das Boot im Wind hängen. Deshalb vor der Wende "
       "eher etwas abfallen und Fahrt machen."),
    mc("Warum wird bei der Wende das Vorsegel erst spät umgeholt?",
       ["Damit es nicht back steht und den Bug zurückdrückt.",
        "Damit es nicht reißt.",
        "Damit die Fahrt erhalten bleibt.",
        "Es wird immer zuerst umgeholt."], 0,
       "Zu früh umgeholt fehlt dem Bug der Schwung; zu spät steht es back "
       "und bremst. Es geht über, sobald der Bug durch den Wind ist."),
    mc("Das Boot bleibt in der Wende im Wind stehen. Wie kommt man heraus?",
       ["Vorsegel back halten und Ruder entsprechend legen.",
        "Großschot dichtholen.",
        "Warten.",
        "Schwert aufholen."], 0,
       "Back gehaltenes Vorsegel drückt den Bug auf die gewünschte Seite. "
       "Bei Rückwärtsfahrt wirkt das Ruder umgekehrt."),
    mc("Warum ist die Halse bei starkem Wind gefährlich?",
       ["Der Baum schlägt mit voller Kraft auf die andere Seite.",
        "Das Boot verliert Fahrt.",
        "Das Vorsegel kann reißen.",
        "Das Schwert schlägt an."], 0,
       "Bei der Halse steht das Segel bis zuletzt voll im Wind. Kommt es "
       "herüber, kommt die ganze gespeicherte Energie mit."),
    mc("Wie führt man eine Halse bei viel Wind kontrolliert durch?",
       ["Großschot dichtholen, herüberlassen, wieder auffieren.",
        "Schot ganz offen lassen.",
        "Schnell durchsteuern.",
        "Vorher das Schwert aufholen."], 0,
       "Dichtholen verkürzt den Weg des Baums und damit seine "
       "Geschwindigkeit. Danach sofort wieder fieren, sonst krängt das "
       "Boot stark."),
    mc("Was ruft der Steuermann unmittelbar vor dem Überkommen des Baums?",
       ["Eine Warnung, damit alle den Kopf einziehen.",
        "„Ree!\"", "„Klar bei Fall!\"", "Nichts."], 0,
       "Der Baum kommt auf Kopfhöhe. Das Ausführungskommando ist zugleich "
       "die Warnung — und es wird laut gegeben."),
    mc("Was ist ein Aufschießer?",
       ["Das Anluven in den Wind bis zum Stillstand.",
        "Eine missglückte Halse.",
        "Ein plötzlicher Fahrtgewinn.",
        "Das Aufrichten nach einer Kenterung."], 0,
       "Der Aufschießer ist das Grundmanöver zum Anlegen, Bojenfangen und "
       "Personenaufnehmen: kontrolliert bis zum Stillstand."),
    mc("Wovon hängt die Länge des Aufschießers ab?",
       ["Von Fahrt, Gewicht des Bootes und von Wind und Welle.",
        "Nur von der Segelfläche.",
        "Nur vom Tiefgang.",
        "Er ist immer gleich lang."], 0,
       "Ein schweres Boot bei wenig Wind schießt weit, ein leichtes gegen "
       "Welle kaum. Deshalb probiert man den Aufschießer im freien Wasser, "
       "bevor man ihn am Steg braucht."),
    mc("Wie legt man unter Segeln am besten an?",
       ["Im Aufschießer gegen den Wind, mit killenden Segeln.",
        "Mit dem Wind von achtern.",
        "Quer zum Wind mit Fahrt.",
        "Rückwärts."], 0,
       "Nur gegen den Wind lässt sich die Fahrt kontrolliert wegnehmen. "
       "Vor dem Wind anzulegen heißt, ungebremst anzukommen."),
    mc("Was tut man vor dem Ablegen mit dem Schwert?",
       ["Im Flachwasser oben lassen und erst im tiefen Wasser absenken.",
        "Immer ganz absenken.",
        "Ganz aufholen und oben lassen.",
        "Das ist gleichgültig."], 0,
       "Ein abgesenktes Schwert im Flachwasser schlägt an und kann brechen "
       "oder das Boot stoppen."),
    mc("Beim Ablegen weht der Wind auf den Steg. Was ist zu beachten?",
       ["Das Boot wird an den Steg gedrückt; man muss sich frei arbeiten.",
        "Das Ablegen ist besonders einfach.",
        "Man legt vor dem Wind ab.",
        "Man setzt zuerst das Großsegel."], 0,
       "Auflandiger Wind am Steg ist die schwierige Richtung. Oft hilft "
       "nur, das Boot an einer Leine nach vorn oder achtern zu verholen, "
       "bis der Bug frei ist."),
    mc("In welcher Reihenfolge setzt man üblicherweise die Segel?",
       ["Erst das Großsegel, dann das Vorsegel.",
        "Erst das Vorsegel, dann das Groß.",
        "Beide gleichzeitig.",
        "Das ist gleichgültig."], 0,
       "Mit gesetztem Groß liegt das Boot von selbst im Wind. Das Vorsegel "
       "zuerst würde den Bug abdrehen lassen."),
    mc("In welcher Reihenfolge birgt man die Segel?",
       ["Erst das Vorsegel, dann das Großsegel.",
        "Erst das Großsegel.",
        "Gleichzeitig.",
        "Nach Windrichtung."], 0,
       "Umgekehrt zum Setzen: Solange das Groß steht, bleibt das Boot "
       "steuerbar und liegt ruhig im Wind."),
    mc("Was bedeutet „beidrehen\"?",
       ["Das Boot mit back stehendem Vorsegel und gelegtem Ruder ruhig "
        "stellen.",
        "Eine Wende einleiten.",
        "Den Motor starten.",
        "Vor Anker gehen."], 0,
       "Beigedreht treibt das Boot langsam nach Lee und liegt ruhig — die "
       "Pause auf See, etwa zum Reffen oder Essen."),
    mc("Wozu dient das Beidrehen praktisch?",
       ["Um in Ruhe zu reffen, zu essen oder auf jemanden zu warten.",
        "Um schneller zu werden.",
        "Um zu ankern.",
        "Um die Segel zu trocknen."], 0,
       "Es nimmt dem Boot die Fahrt, ohne die Segel bergen zu müssen — und "
       "es ist auch ein Weg, bei Starkwind Ruhe ins Boot zu bekommen."),
    mc("Was ist beim Reffen zu beachten?",
       ["Früh genug reffen, möglichst beigedreht oder im Hafen.",
        "Erst wenn es nicht mehr anders geht.",
        "Nur vor dem Wind.",
        "Nach dem Setzen der Segel nie mehr."], 0,
       "Der oft zitierte Satz stimmt: Wenn man ans Reffen denkt, ist es "
       "schon Zeit dafür."),
    mc("Warum wird bei zunehmendem Wind zuerst das Großsegel gerefft?",
       ["Weil es achtern wirkt und die Luvgierigkeit verstärkt.",
        "Weil es das größere Segel ist.",
        "Weil es leichter erreichbar ist.",
        "Es wird immer zuerst das Vorsegel verkleinert."], 0,
       "Ein zu großes Groß bei viel Wind macht das Boot luvgierig und "
       "schwer steuerbar. Die Balance bleibt eher erhalten, wenn man "
       "achtern verkleinert."),
    mc("Was ist ein Sonnenschuss?",
       ["Das unkontrollierte Anluven mit starker Krängung.",
        "Ein Sonnenbrand an Bord.",
        "Eine besonders schnelle Halse.",
        "Ein Manöver vor dem Wind."], 0,
       "Meist aus einer Bö am Wind: Das Boot krängt, luvt trotz Gegenruder "
       "an und stellt sich quer. Abhilfe ist rechtzeitiges Fieren."),
    mc("Was tut man bei einem drohenden Sonnenschuss?",
       ["Großschot sofort fieren.",
        "Ruder hart legen und halten.",
        "Vorsegel dichtnehmen.",
        "Schwert aufholen."], 0,
       "Erst die Kraft aus dem Segel nehmen, dann steuern. Gegen die "
       "Krängung ansteuern gelingt nicht."),
    mc("Wie verhält man sich beim Anlegen an einer Boje?",
       ["Im Aufschießer gegen den Wind darauf zuhalten.",
        "Mit dem Wind von achtern.",
        "Quer anlaufen.",
        "Mit voller Fahrt."], 0,
       "Wie beim Steg: Nur gegen den Wind lässt sich die Fahrt so "
       "wegnehmen, dass man genau an der Boje steht."),
    mc("Was gehört vor jedem Manöver gesagt?",
       ["Was geschehen soll, damit die Mannschaft vorbereitet ist.",
        "Nichts, der Steuermann handelt.",
        "Nur bei der Halse etwas.",
        "Nur im Hafen etwas."], 0,
       "Manöverkommandos sind kein Ritual: Wer weiß, was kommt, hält die "
       "richtige Leine in der Hand und den Kopf unten."),
    mc("Ein Manöver misslingt. Was ist die bessere Reaktion?",
       ["Abbrechen, Fahrt aufnehmen und neu ansetzen.",
        "Mit mehr Kraft durchziehen.",
        "Auf Wind warten.",
        "Den Motor starten."], 0,
       "Ein zweiter Anlauf kostet Minuten, ein erzwungenes Manöver kostet "
       "Lack oder mehr."),
],

# ===========================================================================
"m-mob": [
    mc("Was ist beim Mann-über-Bord-Manöver das wichtigste Hilfsmittel?",
       ["Eine Person, die ununterbrochen hinzeigt.",
        "Das Navigationsgerät.",
        "Der Motor.",
        "Der Anker."], 0,
       "Ohne ständigen Blickkontakt ist ein Kopf im Wellengang in Sekunden "
       "verloren."),
    mc("Warum wird sofort ein Rettungsmittel geworfen, auch wenn es "
       "danebengeht?",
       ["Es markiert die Stelle.",
        "Damit sich der Verunglückte festhalten kann.",
        "Aus Vorschrift.",
        "Um die Drift zu messen."], 0,
       "Beides zählt, aber die Markierung ist der Hauptgrund: Ein Kissen "
       "auf dem Wasser ist von weitem sichtbar, ein Kopf nicht."),
    mc("Von welcher Seite nimmt man den Verunglückten auf?",
       ["Von der Leeseite, ohne Fahrt.",
        "Von der Luvseite.",
        "Über das Heck in Fahrt.",
        "Über den Bug."], 0,
       "In Luv würde das abtreibende Boot auf den Menschen zulaufen. In Lee "
       "treibt es von ihm weg."),
    mc("Was tut man mit dem Motor, sobald jemand längsseits ist?",
       ["Getriebe in Leerlauf oder Motor aus.",
        "Standgas beibehalten.",
        "Rückwärts einlegen.",
        "Vollgas zum Halten."], 0,
       "Die Schraube ist die größte Gefahr beim Bergen. Der Motor darf "
       "laufen, aber nichts darf sich drehen."),
    mc("Warum ist das Bergen aus dem Wasser körperlich schwierig?",
       ["Nasse Kleidung und Auskühlung machen den Verunglückten schwer und "
        "hilflos.",
        "Weil das Boot zu hoch liegt.",
        "Weil die Segel stören.",
        "Weil die Leinen fehlen."], 0,
       "Nach wenigen Minuten im kalten Wasser kann jemand sich nicht mehr "
       "selbst hochziehen. Eine Badeleiter oder ein Talje gehört "
       "vorbereitet."),
    mc("Was ist bei Kälte nach dem Bergen zu beachten?",
       ["Vorsichtig bewegen, waagrecht lagern, warm einpacken.",
        "Kräftig abreiben und Alkohol geben.",
        "Sofort aufstehen lassen.",
        "In heißes Wasser setzen."], 0,
       "Bei Unterkühlung kann kaltes Blut aus den Gliedern zum Herzen "
       "strömen (Bergungstod). Deshalb waagrecht und ruhig."),
    mc("Wie hält man im kalten Wasser am längsten durch?",
       ["Ruhig bleiben, Knie anziehen, Wärme sparen.",
        "Kräftig schwimmen, um warm zu bleiben.",
        "Kleidung ausziehen.",
        "Auf dem Rücken treiben mit ausgestreckten Armen."], 0,
       "Bewegung kostet Wärme. Die HELP-Haltung mit angezogenen Knien "
       "schützt die wärmeempfindlichen Körperbereiche."),
    mc("Warum soll man Kleidung im Wasser anbehalten?",
       ["Sie hält eine wärmende Wasserschicht am Körper.",
        "Sie macht schwimmfähig.",
        "Sie schützt vor Sonne.",
        "Man soll sie ausziehen."], 0,
       "Luft in der Kleidung trägt zusätzlich. Ausziehen kostet Kraft und "
       "Wärme, und beides ist knapp."),
    mc("Was ist eine Lifebelt-Leine?",
       ["Eine Sicherheitsleine, die den Träger am Boot hält.",
        "Die Leine des Rettungsrings.",
        "Ein Teil des Ankergeschirrs.",
        "Der Gurt der Rettungsweste."], 0,
       "Bei Nacht, Starkwind und Arbeiten auf dem Vorschiff wird sie "
       "eingepickt. Wer nicht über Bord geht, muss nicht geborgen werden."),
    mc("Wo wird die Sicherheitsleine eingepickt?",
       ["An einem dafür vorgesehenen, festen Punkt oder Strecktau.",
        "An der Reling.",
        "Am Want.",
        "Am Baum."], 0,
       "Die Reling ist dafür nicht ausgelegt. Strecktauen und Augbolzen "
       "sind es."),
    mc("Was ist der erste Satz, den man bei Mann über Bord ruft?",
       ["„Mann über Bord!\"",
        "„Klar zur Wende?\"",
        "„Rettungsring werfen!\"",
        "Man ruft nichts, um keine Panik auszulösen."], 0,
       "Alle an Bord müssen es sofort wissen; erst dann kann sich jeder "
       "seine Aufgabe nehmen."),
    mc("Welche Rolle hat der Steuermann beim MOB-Manöver?",
       ["Er führt das Boot und verteilt die Aufgaben.",
        "Er springt hinterher.",
        "Er beobachtet.",
        "Er funkt."], 0,
       "Beobachten ist eine eigene Aufgabe für eine eigene Person. Der "
       "Steuermann muss steuern."),
    mc("Wann wird bei MOB ein Notruf abgesetzt?",
       ["Sobald klar ist, dass fremde Hilfe nötig oder hilfreich sein kann.",
        "Immer erst nach erfolgloser Bergung.",
        "Nie.",
        "Nur bei Nacht."], 0,
       "Lieber früh und später entwarnen als spät und ohne Hilfe. Bei "
       "Lebensgefahr ist es MAYDAY."),
    mc("Was ist ein Rettungsring mit Leine gegenüber einem ohne?",
       ["Besser, weil der Verunglückte zum Boot gezogen werden kann.",
        "Schlechter, weil die Leine sich verheddert.",
        "Gleichwertig.",
        "Nur für Binnengewässer erlaubt."], 0,
       "Eine schwimmfähige Wurfleine ist auf Binnengewässern oft das "
       "wirksamste Rettungsmittel überhaupt."),
    mc("Warum wird das MOB-Manöver regelmäßig geübt?",
       ["Weil im Ernstfall keine Zeit zum Überlegen bleibt.",
        "Weil es Pflicht ist.",
        "Weil es Spaß macht.",
        "Weil die Prüfung es verlangt."], 0,
       "Geübt wird mit einem Fender. Wer es zweimal gemacht hat, verliert "
       "im Ernstfall keine Minute mit der Frage, wer was tut."),
],
})


BANK.update({

# ===========================================================================
"r-segel": [
    mc("Auf welchem Bug segelt ein Boot, wenn der Wind von Steuerbord "
       "einfällt?",
       ["Steuerbordbug.", "Backbordbug.",
        "Das hängt vom Kurs ab.", "Auf beiden."], 0,
       "Der Bug ist nach der Seite benannt, von der der Wind kommt — nicht "
       "nach der Seite, auf der das Segel steht."),
    mc("Woran erkennst du von außen, auf welchem Bug ein Segelboot liegt?",
       ["Das Großsegel steht auf der Leeseite, der Wind kommt von der "
        "anderen.",
        "Am Verklicker.", "An der Flagge am Heck.",
        "An der Fahrtrichtung."], 0,
       "Steht das Segel nach Backbord, kommt der Wind von Steuerbord — also "
       "Steuerbordbug, und das Boot hat Vorrang."),
    mc("Zwei Segelboote laufen auf Kollisionskurs, beide auf Backbordbug. "
       "Wer weicht aus?",
       ["Das Boot in Luv.", "Das Boot in Lee.",
        "Das schnellere.", "Beide nach Steuerbord."], 0,
       "Gleicher Bug heißt: Luv weicht Lee aus."),
    mc("Warum hat das Leeboot Vorrang?",
       ["Es steht im Windschatten und könnte nur in den Wind schießen.",
        "Es ist meist schneller.",
        "Es hat besseren Ausguck.",
        "Historische Konvention."], 0,
       "Das Luvboot kann abfallen oder anluven, das Leeboot praktisch "
       "nicht — die Regel folgt der Manövrierfähigkeit."),
    mc("Ein Segelboot überholt ein anderes auf dessen Luvseite. Wer weicht "
       "aus?",
       ["Der Überholende.", "Der Überholte.",
        "Das Luvboot.", "Das Leeboot."], 0,
       "Die Überholregel geht den Bug- und Luv-Lee-Regeln vor."),
    mc("Wann gilt ein Boot als überholend?",
       ["Wenn es sich von mehr als 22,5 Grad achterlicher als querab "
        "nähert.",
        "Sobald es schneller ist.",
        "Wenn es in Lee vorbeizieht.",
        "Wenn beide denselben Kurs haben."], 0,
       "Das ist der Sektor, in dem man nachts nur das Hecklicht sieht — "
       "genau deshalb ist er so definiert."),
    mc("Was muss das vorfahrtberechtigte Boot tun?",
       ["Kurs und Geschwindigkeit halten.",
        "Ausweichen, wenn es kann.",
        "Beschleunigen.",
        "Nichts Bestimmtes."], 0,
       "Nur wenn der Berechtigte vorhersehbar handelt, kann der andere "
       "sinnvoll ausweichen."),
    mc("Wann darf das vorfahrtberechtigte Boot von dieser Pflicht "
       "abweichen?",
       ["Wenn nur noch eigenes Handeln den Zusammenstoß verhindert.",
        "Nie.", "Immer, wenn es knapp wird.",
        "Nur mit Schallsignal."], 0,
       "Diese Ausnahme steht ausdrücklich in den Vorschriften — und sie "
       "ist der Grund, warum Rechthaben auf dem Wasser keine Strategie "
       "ist."),
    mc("Wie soll ausgewichen werden?",
       ["Früh, deutlich und so, dass es der andere erkennt.",
        "Möglichst spät, um Weg zu sparen.",
        "Mit kleinen Korrekturen.",
        "Nur mit dem Schallsignal angekündigt."], 0,
       "Eine Kursänderung, die der andere nicht erkennt, ist kein "
       "Ausweichen. Große, frühe Manöver sind sicher und höflich."),
    mc("Zwei Segelboote begegnen sich am Hang eines Ufers. Wer weicht aus?",
       ["Das Boot, das das Ufer an Backbord hat.",
        "Das Boot mit dem Ufer an Steuerbord.",
        "Das langsamere.",
        "Es gilt nur die Bugregel."], 0,
       "Wer das Ufer rechts hat, kann nicht nach rechts ausweichen. Die "
       "Regel folgt wieder der Geometrie, nicht der Höflichkeit."),
    mc("Was gilt beim Kreuzen in einem engen Fahrwasser?",
       ["Segelboote dürfen die Durchfahrt größerer Fahrzeuge nicht "
        "behindern.",
        "Segelboote haben stets Vorrang.",
        "Es darf nicht gekreuzt werden.",
        "Nur bei Tag erlaubt."], 0,
       "Ein Schiff, das das Fahrwasser braucht, kann nicht ausweichen — "
       "deshalb geht der Segelvorrang dort nicht."),
    mc("Zwei Segelboote auf Gegenkurs, beide genau vor dem Wind. Wie "
       "verhält man sich?",
       ["Nach den Bugregeln; hilfsweise beide nach Steuerbord.",
        "Beide nach Backbord.",
        "Der Schnellere weicht aus.",
        "Kurs halten."], 0,
       "Auch vor dem Wind hat jedes Boot einen Bug — die Seite, auf der das "
       "Großsegel steht, bestimmt ihn. Im Zweifel weicht man nach "
       "Steuerbord aus."),
    mc("Ein Segelboot nähert sich einem Ruderboot. Wer weicht aus?",
       ["Es gilt die allgemeine Rücksichtnahme; auf Binnengewässern haben "
        "Kleinfahrzeuge ohne Antrieb meist Vorrang.",
        "Immer das Ruderboot.",
        "Immer das Segelboot.",
        "Das langsamere."], 0,
       "Die Rangfolge geht nach Manövrierfähigkeit. Auf vielen "
       "Binnengewässern sind Fahrzeuge ohne Maschinen- und Segelantrieb "
       "ausdrücklich geschützt."),
    mc("Was gilt gegenüber Schwimmern und Tauchern?",
       ["Weiträumig ausweichen; Taucherflaggen kennzeichnen Tauchstellen.",
        "Schwimmer müssen ausweichen.",
        "Nur nachts ausweichen.",
        "Es gilt die Bugregel."], 0,
       "Die Taucherflagge (rot mit weißem Diagonalstreifen oder die "
       "blau-weiße Flagge A) heißt: Abstand halten und langsam fahren."),
    mc("Ein Boot zeigt einen schwarzen Kegel mit der Spitze nach unten. Was "
       "bedeutet das?",
       ["Es fährt unter Maschine, obwohl die Segel gesetzt sind.",
        "Es ankert.",
        "Es ist manövrierunfähig.",
        "Es fischt."], 0,
       "Damit ist es rechtlich ein Maschinenfahrzeug und hat keinen "
       "Segelvorrang."),
    mc("Warum gilt ein Segelboot unter Motor als Maschinenfahrzeug?",
       ["Weil es dann manövrierfähig ist wie ein Motorboot.",
        "Weil der Motor lauter ist.",
        "Wegen der Abgase.",
        "Das gilt nur mit geborgenen Segeln."], 0,
       "Die ganze Rangfolge richtet sich nach Manövrierfähigkeit. Wer eine "
       "Maschine hat und nutzt, kann ausweichen."),
    mc("Zwei Maschinenfahrzeuge begegnen sich auf Gegenkurs. Was gilt?",
       ["Beide weichen nach Steuerbord aus.",
        "Beide nach Backbord.",
        "Das kleinere weicht aus.",
        "Das schnellere weicht aus."], 0,
       "Die Rechtsregel — dieselbe wie im Straßenverkehr, und auf dem "
       "Wasser ebenso einfach zu merken."),
    mc("Zwei Maschinenfahrzeuge kreuzen sich. Wer weicht aus?",
       ["Das Fahrzeug, das das andere an Steuerbord hat.",
        "Das Fahrzeug, das das andere an Backbord hat.",
        "Das langsamere.",
        "Das kleinere."], 0,
       "Wer den anderen rechts sieht, weicht aus — nachts sieht man dann "
       "dessen rotes Backbordlicht: rot heißt anhalten."),
    mc("Du siehst nachts das rote Licht eines Fahrzeugs. Was heißt das für "
       "dich?",
       ["Du siehst seine Backbordseite; in der Regel musst du ausweichen.",
        "Es hat Vorrang und du kannst weiterfahren.",
        "Es fährt von dir weg.",
        "Es ankert."], 0,
       "Das rote Licht des anderen ist die Farbe, bei der man anhält. Sieht "
       "man grün, ist man meist der Berechtigte."),
    mc("Ändert sich die Peilung zu einem anderen Fahrzeug nicht, bedeutet "
       "das …",
       ["Kollisionskurs.", "Es entfernt sich.",
        "Es ist langsamer.", "Alles in Ordnung."], 0,
       "Gleichbleibende Peilung bei abnehmendem Abstand heißt Treffpunkt. "
       "Das ist die verlässlichste Prüfung überhaupt — und sie kostet nur "
       "einen Blick über den Daumen."),
    mc("Was ist die Grundregel über allen Ausweichregeln?",
       ["Ein Zusammenstoß ist mit allen Mitteln zu vermeiden.",
        "Der Größere hat Vorrang.",
        "Der Schnellere weicht aus.",
        "Segel vor Motor gilt immer."], 0,
       "Alle Einzelregeln dienen diesem Zweck; keine erlaubt es, in einen "
       "Zusammenstoß hineinzufahren."),
    mc("Wozu dient ein Ausguck?",
       ["Ständige Beobachtung mit Augen und Ohren.",
        "Nur zur Navigation.",
        "Nur bei Nacht.",
        "Nur in Fahrwassern."], 0,
       "Der Ausguck ist Pflicht, jederzeit. Auch Hören zählt — "
       "Schallsignale kommen um Ecken, die man nicht sieht."),
    mc("Wie verhält man sich bei unklarer Lage gegenüber einem anderen "
       "Fahrzeug?",
       ["Fahrt vermindern und notfalls stoppen.",
        "Kurs halten und abwarten.",
        "Beschleunigen, um vorbeizukommen.",
        "Ein Schallsignal geben und weiterfahren."], 0,
       "Wer nicht sicher ist, ob er ausweichpflichtig ist, verhält sich so, "
       "als wäre er es."),
    mc("Was bedeutet der Begriff „Kleinfahrzeug\" auf Binnengewässern?",
       ["Ein Fahrzeug unter 20 m Länge, mit Ausnahmen.",
        "Jedes Segelboot.",
        "Jedes Boot ohne Motor.",
        "Ein Boot unter 5 m."], 0,
       "Die Grenze von 20 m entscheidet über viele Pflichten — und "
       "Kleinfahrzeuge weichen den großen grundsätzlich aus."),
    mc("Wie verhält man sich gegenüber einem Fahrgastschiff im Linienbetrieb?",
       ["Ausweichen und nicht behindern.",
        "Vorrang beanspruchen, wenn man segelt.",
        "Dicht vorbeifahren ist erlaubt.",
        "Es gelten nur die Bugregeln."], 0,
       "Fahrgastschiffe fahren nach Plan, oft in engen Fahrwassern und mit "
       "vielen Menschen an Bord. Sie werden nicht behindert."),
],

# ===========================================================================
"r-verkehr": [
    mc("Wo darf auf Binnenseen in der Regel nicht gesegelt werden?",
       ["In gekennzeichneten Bade- und Schutzzonen.",
        "In der Seemitte.",
        "In Ufernähe generell.",
        "Bei Nacht."], 0,
       "Bade- und Naturschutzzonen sind meist durch Bojenketten "
       "abgegrenzt. Dort ist das Befahren untersagt."),
    mc("Was gilt für Motorbetrieb in Ufernähe auf vielen Seen?",
       ["Geschwindigkeitsbeschränkungen und teils Motorverbot.",
        "Keine Beschränkung.",
        "Nur nachts beschränkt.",
        "Nur für Berufsschifffahrt."], 0,
       "Wellenschlag schadet Ufer und Badenden. Die örtlichen "
       "Verordnungen regeln das, oft ab 100 oder 200 m Uferabstand."),
    mc("Ein Schifffahrtszeichen zeigt ein rotes Quadrat mit weißem "
       "Querbalken. Was bedeutet es in der Regel?",
       ["Ein Verbot.", "Ein Gebot.",
        "Einen Hinweis.", "Eine Empfehlung."], 0,
       "Rot umrandete oder rote Tafeln verbieten, blaue gebieten oder "
       "weisen hin — dieselbe Logik wie im Straßenverkehr."),
    mc("Welche Farbe kennzeichnet Hinweiszeichen in der Binnenschifffahrt?",
       ["Blau.", "Rot.", "Gelb.", "Grün."], 0,
       "Blau mit weißem Symbol weist hin oder gebietet, etwa Liegestellen "
       "oder Verkehrsrichtungen."),
    mc("Was ist unter „Schleuse\" zu beachten?",
       ["Anweisungen des Schleusenpersonals haben Vorrang.",
        "Segelboote haben Vorrang.",
        "Es gilt die Bugregel.",
        "Kleinfahrzeuge dürfen nicht schleusen."], 0,
       "In der Schleuse gilt, was die Aufsicht sagt und was die Lichter "
       "zeigen — Ausweichregeln spielen keine Rolle."),
    mc("Welche Lichter an einer Schleuse bedeuten „Einfahrt frei\"?",
       ["Grün.", "Rot.", "Rot und grün zugleich.", "Gelb."], 0,
       "Zwei rote Lichter heißen gesperrt, rot-grün heißt Vorbereitung, "
       "grün heißt Einfahrt frei."),
    mc("Was gilt beim Befahren eines Hafens?",
       ["Langsam fahren, kein Wellenschlag, Vorrang für ein- und "
        "auslaufende Berufsschifffahrt.",
        "Es gelten nur die Ausweichregeln.",
        "Segeln ist immer erlaubt.",
        "Es gibt keine besonderen Regeln."], 0,
       "In vielen Häfen ist Segeln ohnehin untersagt — dort wird unter "
       "Motor oder Paddel manövriert."),
    mc("Was bedeutet ein Fahrzeug mit einem blauen Blinklicht?",
       ["Ein Fahrzeug der Behörden im Einsatz, dem Platz zu machen ist.",
        "Ein Taucherfahrzeug.",
        "Ein Fahrgastschiff.",
        "Ein manövrierunfähiges Fahrzeug."], 0,
       "Polizei, Feuerwehr und Wasserrettung im Einsatz: Weg frei machen "
       "und Wellenschlag vermeiden."),
    mc("Was zeigt die blaue Tafel eines Frachtschiffes an?",
       ["Es will Steuerbord an Steuerbord begegnen, entgegen der Regel.",
        "Es ankert.",
        "Es hat Vorrang.",
        "Es ist manövrierunfähig."], 0,
       "Die blaue Tafel mit weißem Funkellicht bedeutet: Begegnung auf der "
       "„falschen\" Seite. Man weicht dann nach Backbord aus und "
       "beantwortet das Zeichen, wenn möglich."),
    mc("Ein Frachtschiff zeigt die blaue Tafel. Was tust du?",
       ["Auf seiner Steuerbordseite vorbeifahren, also selbst nach "
        "Backbord ausweichen.",
        "Wie gewohnt rechts ausweichen.",
        "Stoppen und warten.",
        "Das Zeichen ignorieren."], 0,
       "Das Schiff fährt aus guten Gründen auf der anderen Seite — meist "
       "wegen der Strömung oder der Fahrrinne."),
    mc("Wer darf ein Segelboot mit mehr als 10 m Länge auf Binnengewässern "
       "führen?",
       ["Wer eine entsprechende Befähigung besitzt.",
        "Jeder ab 18.",
        "Nur Berufsschiffer.",
        "Jeder mit Segelschein A."], 0,
       "Die Längen- und Leistungsgrenzen entscheiden, welche Befähigung "
       "nötig ist; sie sind je nach Gewässer und Land geregelt."),
    mc("Welche Papiere gehören üblicherweise an Bord?",
       ["Befähigungsausweis, gegebenenfalls Zulassung und Versicherung.",
        "Nur der Ausweis.",
        "Gar keine.",
        "Nur die Versicherung."], 0,
       "Was genau verlangt wird, steht in den Vorschriften des jeweiligen "
       "Gewässers — dabei zu haben ist der sichere Weg."),
    mc("Wann ist eine Haftpflichtversicherung sinnvoll oder "
       "vorgeschrieben?",
       ["Auf vielen Gewässern vorgeschrieben, sonst dringend zu empfehlen.",
        "Nie nötig.",
        "Nur für Motorboote.",
        "Nur für Charterboote."], 0,
       "Ein Schaden an einem fremden Boot oder einer Steganlage übersteigt "
       "schnell den Wert des eigenen Bootes."),
    mc("Was ist bei gecharterten Booten zusätzlich zu prüfen?",
       ["Zustand, Ausrüstung und vorhandene Schäden vor dem Ablegen.",
        "Nur der Tank.",
        "Nichts, der Vermieter haftet.",
        "Nur die Segel."], 0,
       "Eine Übernahme mit Protokoll schützt beide Seiten — und wer die "
       "Sicherheitsausrüstung erst auf dem See sucht, sucht zu spät."),
    mc("Was ist ein „Fahrtenbuch\" oder Logbuch?",
       ["Eine Aufzeichnung von Fahrten, Zeiten und Besonderheiten.",
        "Die Betriebsanleitung.",
        "Das Ausrüstungsverzeichnis.",
        "Die Wetteraufzeichnung."], 0,
       "Auf Binnengewässern selten vorgeschrieben, aber für den Nachweis "
       "von Praxiszeiten — etwa für weitere Scheine — die Grundlage."),
    mc("Wie verhält man sich bei einem Unfall mit Sachschaden?",
       ["Hilfe leisten, Daten austauschen, gegebenenfalls Behörde "
        "verständigen.",
        "Weiterfahren, wenn niemand verletzt ist.",
        "Nur die Versicherung informieren.",
        "Den Schaden selbst reparieren."], 0,
       "Die Pflichten entsprechen denen im Straßenverkehr: Hilfe geht vor, "
       "dann Feststellung, dann Meldung."),
    mc("Was ist die erste Pflicht bei einem Seenotfall in der Nähe?",
       ["Hilfe leisten, soweit es ohne eigene Gefährdung möglich ist.",
        "Die Polizei rufen und weiterfahren.",
        "Nichts, dafür gibt es die Wasserrettung.",
        "Nur bei eigener Beteiligung helfen."], 0,
       "Die Hilfeleistungspflicht ist auf dem Wasser noch strenger als an "
       "Land — Hilfe ist oft nur vom nächsten Boot zu erwarten."),
    mc("Was gilt für Alkohol am Ruder in Österreich?",
       ["Es gelten Promillegrenzen wie im Straßenverkehr.",
        "Es gibt keine Grenze.",
        "Nur für Motorboote.",
        "Nur bei Nacht."], 0,
       "Unabhängig von der Zahl: Sonne, Wind und Bewegung verstärken die "
       "Wirkung deutlich gegenüber dem Land."),
    mc("Wie viele Rettungswesten gehören an Bord?",
       ["Mindestens eine je Person.",
        "Eine je Boot.", "Zwei je Boot.",
        "Nur für Nichtschwimmer."], 0,
       "Und sie gehören in Reichweite, nicht in die Backskiste unter dem "
       "Proviant."),
    mc("Wann ist eine Rettungsweste für Kinder zu tragen?",
       ["An Bord grundsätzlich, auch bei ruhigem Wetter.",
        "Nur bei Wind.",
        "Nur bei Nacht.",
        "Nur für Nichtschwimmer."], 0,
       "Kinder kühlen schneller aus und geraten leichter in Panik. Die "
       "Weste ist bei ihnen Dauerzustand."),
    mc("Welche Rettungsweste hilft einem Bewusstlosen?",
       ["Eine Feststoff- oder Automatikweste mit Ohnmachtssicherheit.",
        "Jede Schwimmhilfe.",
        "Ein Schwimmgürtel.",
        "Eine Schwimmweste ohne Kragen."], 0,
       "Schwimmhilfen (50 N) tragen nur, wer selbst schwimmt. "
       "Ohnmachtssicher wird es erst ab etwa 100 N mit Kragen."),
    mc("Was bedeutet die Angabe „150 N\" auf einer Rettungsweste?",
       ["Den Auftrieb; ab 100 N gilt sie als ohnmachtssicher.",
        "Das zulässige Körpergewicht.",
        "Die Reißfestigkeit.",
        "Die Wassertemperatur."], 0,
       "50 N ist eine Schwimmhilfe, 100 N eine Rettungsweste, 150 N für "
       "See und schwere Kleidung, 275 N für extreme Bedingungen."),
    mc("Was gehört zur Mindestausrüstung eines kleinen Segelbootes?",
       ["Rettungsmittel, Paddel, Festmacher, Lenzmittel, Anker.",
        "Nur die Segel.",
        "Nur eine Rettungsweste.",
        "Funkgerät und Radar."], 0,
       "Was genau, regelt die Verordnung des Gewässers. Der Kern ist "
       "überall ähnlich: schwimmen, bewegen, festmachen, lenzen, "
       "ankern."),
    mc("Warum gehört ein Paddel auch auf ein Segelboot?",
       ["Bei Flaute oder Motorausfall ist es das letzte Antriebsmittel.",
        "Zum Abstoßen am Steg.",
        "Als Ersatzruder.",
        "Es gehört nicht dazu."], 0,
       "Auf einem Binnensee reicht es meist bis ans Ufer — und das ist "
       "genau der Zweck."),
],

# ===========================================================================
"z-tonnen": [
    mc("Welche Kennziffern tragen Steuerbordtonnen?",
       ["Ungerade.", "Gerade.", "Keine.", "Römische."], 0,
       "Steuerbord ungerade und grün, Backbord gerade und rot — von See "
       "kommend."),
    mc("Welche Form hat eine Steuerbordtonne?",
       ["Spitz, also Kegel.", "Stumpf, also Zylinder.",
        "Kugelförmig.", "Rechteckig."], 0,
       "Spitz und grün auf der einen, stumpf und rot auf der anderen Seite "
       "— Form und Farbe sagen dasselbe, damit es auch bei schlechtem "
       "Licht erkennbar bleibt."),
    mc("Was bedeutet eine Tonne mit schwarz-gelber Färbung?",
       ["Ein Kardinalzeichen.", "Mittefahrwasser.",
        "Eine Einzelgefahr.", "Ein Sperrgebiet."], 0,
       "Kardinalzeichen sind schwarz-gelb und tragen zwei schwarze Kegel "
       "als Toppzeichen."),
    mc("Ein Kardinalzeichen trägt zwei Kegel mit den Spitzen nach oben. Wo "
       "passiert man sicher?",
       ["Nördlich.", "Südlich.", "Östlich.", "Westlich."], 0,
       "Spitzen nach oben zeigen nach Norden — die Kegel zeigen die "
       "Richtung, in der das sichere Wasser liegt."),
    mc("Zwei Kegel mit den Spitzen nach unten. Wo passiert man?",
       ["Südlich.", "Nördlich.", "Östlich.", "Westlich."], 0,
       "Nach unten heißt Süden. Die Merkhilfe ist die Himmelsrichtung, in "
       "die die Spitzen weisen."),
    mc("Zwei Kegel mit den Grundflächen zusammen (Spitzen nach außen). Wo "
       "passiert man?",
       ["Westlich.", "Östlich.", "Nördlich.", "Südlich."], 0,
       "Zusammen wie eine Sanduhr oder ein „W\" auf der Seite: West. "
       "Auseinander heißt Ost."),
    mc("Zwei Kegel mit den Spitzen gegeneinander. Wo passiert man?",
       ["Östlich.", "Westlich.", "Nördlich.", "Südlich."], 0,
       "Spitzen gegeneinander — wie ein liegendes „E\" für Ost."),
    mc("Was kennzeichnet eine Einzelgefahrenstelle?",
       ["Schwarz mit rotem Band, zwei schwarze Kugeln obenauf.",
        "Rot-weiß gestreift mit einer Kugel.",
        "Gelb mit Kreuz.",
        "Grün mit Kegel."], 0,
       "Sie steht **auf** der Gefahr, nicht daneben — also weiträumig "
       "umfahren."),
    mc("Eine Tonne ist gelb mit einem liegenden Kreuz als Toppzeichen. Was "
       "ist das?",
       ["Ein Sonderzeichen, etwa für ein Sperrgebiet oder eine Messstelle.",
        "Ein Kardinalzeichen.",
        "Eine Backbordtonne.",
        "Mittefahrwasser."], 0,
       "Gelbe Zeichen markieren Besonderes: Badezonen, Kabel, Messstellen "
       "oder Sperrgebiete."),
    mc("Was bedeutet eine rot-weiß längsgestreifte Tonne mit roter Kugel?",
       ["Sicheres Wasser ringsum, etwa die Ansteuerungstonne.",
        "Einzelgefahr.",
        "Backbordseite.",
        "Sperrgebiet."], 0,
       "Sie markiert die Mitte des Fahrwassers oder dessen Anfang — man "
       "darf beidseitig vorbei."),
    mc("Woran erkennt man die Fahrtrichtung der Betonnung auf einem Fluss?",
       ["Von See kommend, also flussaufwärts.",
        "Immer von Nord nach Süd.",
        "Nach der Strömung.",
        "Es gibt keine feste Richtung."], 0,
       "Auf Binnenwasserstraßen gilt die Richtung von der Mündung zur "
       "Quelle."),
    mc("Was zeigt eine Tonne mit grün-rot-grüner Querstreifung an?",
       ["Eine Abzweigung, Hauptfahrwasser rechts.",
        "Eine Einzelgefahr.",
        "Ein Sperrgebiet.",
        "Mittefahrwasser."], 0,
       "Die Farbe oben bestimmt, auf welcher Seite die Tonne liegt; die "
       "Streifung sagt, dass sich das Fahrwasser teilt."),
    mc("Warum sind Fahrwassertonnen oft beleuchtet?",
       ["Damit sie nachts erkennbar bleiben; die Kennung identifiziert sie.",
        "Nur zur Zierde.",
        "Um Fische anzulocken.",
        "Zur Stromversorgung von Messgeräten."], 0,
       "Die Feuerkennung — Takt und Farbe — steht in der Karte und macht "
       "aus einem Licht eine bestimmte Tonne."),
    mc("Was bedeutet die Kennung „Fl(2) 10s\"?",
       ["Zwei Blitze alle zehn Sekunden.",
        "Zehn Blitze alle zwei Sekunden.",
        "Dauerlicht mit zwei Farben.",
        "Zwei Sekunden Licht, zehn Sekunden Dunkelheit."], 0,
       "Fl steht für Funkelfeuer (flashing), die Zahl in Klammern für die "
       "Zahl der Blitze je Periode, danach die Periodendauer."),
    mc("Was ist eine Untiefentonne?",
       ["Ein Zeichen, das flaches Wasser markiert.",
        "Eine Tonne mit Tiefenmessgerät.",
        "Die tiefste Stelle des Fahrwassers.",
        "Eine Ankerboje."], 0,
       "Häufig als Kardinalzeichen ausgeführt: Es sagt dann gleich mit, auf "
       "welcher Seite man vorbeikommt."),
    mc("Wie liest man die Wassertiefe aus einer Seekarte?",
       ["Aus den Tiefenangaben und Tiefenlinien, bezogen auf ein "
        "Kartennull.",
        "Aus der Farbe des Wassers.",
        "Aus den Tonnennummern.",
        "Aus dem Maßstab."], 0,
       "Das Kartennull ist ein festgelegter Bezugswasserstand. Bei "
       "Niedrigwasser steht real weniger Wasser als in der Karte."),
    mc("Was bedeutet eine gestrichelte blaue Linie in einer Binnenkarte "
       "meist?",
       ["Eine Tiefenlinie.", "Eine Landesgrenze.",
        "Eine Fährverbindung.", "Ein Sperrgebiet."], 0,
       "Tiefenlinien verbinden Punkte gleicher Tiefe — wie Höhenlinien, "
       "nur nach unten."),
    mc("Was ist beim Befahren einer engen Fahrrinne zu beachten?",
       ["Rechts halten und größeren Fahrzeugen nicht in den Weg geraten.",
        "Mittig fahren.",
        "Links halten.",
        "Möglichst schnell durchfahren."], 0,
       "Rechts halten ist die Grundregel, und Kleinfahrzeuge halten sich "
       "möglichst ganz außerhalb der Rinne."),
    mc("Was zeigt ein Schifffahrtszeichen mit einem weißen Dreieck auf "
       "rotem Grund an?",
       ["Ein Verbot oder eine Einschränkung, je nach Symbol.",
        "Immer ein Hinweis.",
        "Immer ein Gebot.",
        "Eine Ankerstelle."], 0,
       "Die genaue Bedeutung steht im Symbol; die rote Umrandung sagt "
       "schon, dass etwas untersagt oder eingeschränkt ist."),
    mc("Was tut man, wenn die Betonnung nicht zur Karte passt?",
       ["Der Natur vertrauen und vorsichtig fahren; Karten veralten.",
        "Der Karte vertrauen.",
        "Anhalten und warten.",
        "Umkehren."], 0,
       "Tonnen werden versetzt, Fahrwasser wandern. Was draußen steht, "
       "gilt — und wer unsicher ist, fährt langsam und lotet."),
    mc("Was bedeutet ein gelbes Blinklicht an einem Fahrzeug?",
       ["Es ist ein besonderes Fahrzeug, etwa ein Arbeitsschiff.",
        "Es ankert.",
        "Es ist manövrierunfähig.",
        "Es hat Vorrang."], 0,
       "Arbeits- und Messfahrzeuge kennzeichnen sich so; ihnen gebührt "
       "Abstand, weil oft Geräte im Wasser sind."),
    mc("Warum tragen Backbordtonnen gerade Nummern?",
       ["Damit sich Seite und Position auch ohne Sicht auf die Farbe "
        "bestimmen lassen.",
        "Zufall.", "Aus historischen Gründen.",
        "Wegen der Herstellung."], 0,
       "Bei Dunst oder Gegenlicht ist die Zahl oft eher lesbar als die "
       "Farbe — die doppelte Kennzeichnung ist Absicht."),
    mc("Welche Bedeutung hat das Toppzeichen einer Tonne?",
       ["Es wiederholt die Aussage der Form und Farbe und ist von weitem "
        "sichtbar.",
        "Es dient der Befestigung.",
        "Es ist reine Zierde.",
        "Es zeigt die Wassertiefe."], 0,
       "Ein Zylinder oben gehört zu Backbord, ein Kegel zu Steuerbord — "
       "dieselbe Aussage, nur größer und höher."),
    mc("Was kennzeichnen Bojenketten an Badestränden?",
       ["Den Badebereich, der nicht befahren werden darf.",
        "Eine Untiefe.", "Eine Ankerstelle.",
        "Eine Regattabahn."], 0,
       "Meist gelbe Bojen. Hineinzufahren ist untersagt und gefährlich — "
       "Schwimmer sind von einem Boot aus kaum zu sehen."),
],
})


BANK.update({

# ===========================================================================
"z-lichter": [
    mc("Welchen Horizontbogen deckt ein Seitenlicht ab?",
       ["112,5 Grad.", "135 Grad.", "225 Grad.", "360 Grad."], 0,
       "Zwei Seitenlichter zu 112,5 Grad plus das Hecklicht mit 135 Grad "
       "ergeben genau den Vollkreis von 360 Grad."),
    mc("Welchen Bogen deckt das Hecklicht ab?",
       ["135 Grad.", "112,5 Grad.", "225 Grad.", "180 Grad."], 0,
       "Diese 135 Grad sind zugleich der Sektor, aus dem ein Fahrzeug als "
       "überholend gilt."),
    mc("Welche Farbe hat das Topplicht?",
       ["Weiß.", "Grün.", "Rot.", "Gelb."], 0,
       "Es leuchtet 225 Grad nach vorn und kennzeichnet ein "
       "Maschinenfahrzeug in Fahrt."),
    mc("Du siehst nachts grün und darüber weiß. Was ist das?",
       ["Ein Maschinenfahrzeug, das du an Steuerbord siehst.",
        "Ein Segelboot von vorn.",
        "Ein ankerndes Fahrzeug.",
        "Ein Fahrzeug, das sich entfernt."], 0,
       "Grün heißt: Du siehst seine Steuerbordseite. Das weiße Topplicht "
       "sagt, dass es unter Maschine fährt."),
    mc("Welches Licht zeigt ein ankerndes Fahrzeug?",
       ["Ein weißes Rundumlicht.", "Rot über Weiß.",
        "Zwei rote Lichter.", "Gar keines."], 0,
       "Rundum weiß, möglichst weit vorn gesetzt. Tagsüber entspricht dem "
       "ein schwarzer Ball."),
    mc("Was zeigt ein manövrierunfähiges Fahrzeug bei Nacht?",
       ["Zwei rote Rundumlichter übereinander.",
        "Zwei grüne Lichter.",
        "Ein weißes Blinklicht.",
        "Rot über Grün."], 0,
       "Merkhilfe: „rot über rot — der Kapitän ist tot\", also außer "
       "Gefecht. Tagsüber zwei schwarze Bälle."),
    mc("Ein Segelboot unter 20 m darf die Seitenlichter und das Hecklicht "
       "auch …",
       ["in einer Dreifarbenlaterne im Masttopp führen.",
        "durch ein weißes Rundumlicht ersetzen.",
        "weglassen.",
        "durch eine Taschenlampe ersetzen."], 0,
       "Die Dreifarbenlaterne ist weit sichtbar, darf aber nicht "
       "gleichzeitig mit den Seitenlichtern brennen."),
    mc("Darf die Dreifarbenlaterne unter Motor geführt werden?",
       ["Nein, unter Maschine gelten die normalen Lichter samt Topplicht.",
        "Ja, immer.",
        "Nur bei Nacht.",
        "Nur auf Binnengewässern."], 0,
       "Sonst wäre für andere nicht erkennbar, dass man ein "
       "Maschinenfahrzeug ist — und damit ausweichpflichtig."),
    mc("Was führt ein Fahrzeug unter 7 m ohne Maschine mindestens?",
       ["Ein weißes Rundumlicht, rechtzeitig gezeigt.",
        "Seitenlichter.", "Ein Topplicht.",
        "Gar nichts."], 0,
       "Eine rechtzeitig gezeigte weiße Handlampe genügt — sie muss "
       "allerdings griffbereit sein und nicht in der Backskiste liegen."),
    mc("Wann sind die Lichter zu führen?",
       ["Von Sonnenuntergang bis Sonnenaufgang und bei verminderter Sicht.",
        "Nur bei völliger Dunkelheit.",
        "Nur im Fahrwasser.",
        "Nur bei Motorbetrieb."], 0,
       "Nebel, Regen und Schneefall zählen als verminderte Sicht — auch "
       "mittags."),
    mc("Was ist ein Funkellicht?",
       ["Ein Licht mit sehr schneller Folge von Blitzen.",
        "Ein Dauerlicht.",
        "Ein Blinklicht mit langer Periode.",
        "Ein Licht in zwei Farben."], 0,
       "Es hebt sich von normalen Blinkfeuern ab und kennzeichnet "
       "Besonderes — etwa die blaue Tafel oder Kardinalzeichen."),
    mc("Ein Schallsignal von einem langen Ton bedeutet …",
       ["Achtung.", "„Ich gehe nach Steuerbord.\"",
        "„Ich gehe nach Backbord.\"", "Gefahr."], 0,
       "Ein langer Ton ist das Achtungssignal, etwa beim Verlassen einer "
       "unübersichtlichen Hafenausfahrt."),
    mc("Zwei kurze Töne bedeuten …",
       ["„Ich richte meinen Kurs nach Backbord.\"",
        "„… nach Steuerbord.\"",
        "„Meine Maschine geht rückwärts.\"",
        "Warnsignal."], 0,
       "Einer heißt Steuerbord, zwei Backbord, drei rückwärts — die Zahl "
       "steigt mit der Ungewöhnlichkeit."),
    mc("Drei kurze Töne bedeuten …",
       ["„Meine Maschine geht rückwärts.\"",
        "Warnsignal.",
        "„Ich gehe nach Backbord.\"",
        "Achtung."], 0,
       "Wichtig zu wissen, wenn ein großes Schiff vor einem im Hafen "
       "rangiert."),
    mc("Wie lange dauert ein „kurzer Ton\" etwa?",
       ["Etwa eine Sekunde.", "Etwa vier Sekunden.",
        "Etwa zehn Sekunden.", "Eine halbe Sekunde."], 0,
       "Ein langer Ton dauert etwa vier bis sechs Sekunden — der "
       "Unterschied ist deutlich hörbar."),
    mc("Welches Schallsignal gibt ein Fahrzeug bei Nebel in Fahrt?",
       ["In Abständen einen langen Ton.",
        "Fünf kurze Töne.",
        "Zwei lange Töne.",
        "Gar keines."], 0,
       "Auf Binnengewässern regeln die Vorschriften die genauen Folgen; "
       "der lange Ton in Abständen ist die Grundform."),
    mc("Was ist bei Nebel außerdem geboten?",
       ["Fahrt vermindern, Ausguck verstärken, notfalls anhalten.",
        "Mehr Fahrt, um schneller heraus zu sein.",
        "Nur Lichter setzen.",
        "Nichts Besonderes."], 0,
       "Auf einem Binnensee ist Anhalten oder Ankern oft die vernünftigste "
       "Entscheidung, bis die Sicht zurückkommt."),
    mc("Welches Tageszeichen entspricht dem Ankerlicht?",
       ["Ein schwarzer Ball im Vorschiff.",
        "Ein schwarzer Kegel.",
        "Zwei schwarze Bälle.",
        "Ein Zylinder."], 0,
       "Ein Ball heißt ankernd, zwei Bälle manövrierunfähig, ein Kegel "
       "Spitze nach unten: Segelboot unter Maschine."),
    mc("Ein Fahrzeug zeigt tagsüber zwei schwarze Bälle. Was heißt das?",
       ["Es ist manövrierunfähig.",
        "Es ankert.", "Es fischt.",
        "Es fährt unter Maschine."], 0,
       "Das Tagespendant zu „rot über rot\": Es kann nicht ausweichen, also "
       "weicht man selbst aus."),
    mc("Wozu dienen Signalzeichen überhaupt?",
       ["Damit andere die Art und Absicht eines Fahrzeugs erkennen.",
        "Zur Dekoration.",
        "Für die Statistik.",
        "Nur für die Berufsschifffahrt."], 0,
       "Auf dem Wasser kann man nicht blinken oder hupen wie im Auto — "
       "Lichter und Formen übernehmen das."),
    mc("Was ist zu tun, wenn man ein Signal nicht deutet?",
       ["Abstand halten, Fahrt vermindern, beobachten.",
        "Näher heranfahren, um es zu erkennen.",
        "Ignorieren.",
        "Ein Warnsignal geben und weiterfahren."], 0,
       "Ein unverstandenes Signal ist ein Grund, vorsichtiger zu werden — "
       "nicht neugieriger."),
    mc("Warum sind die Sektoren der Lichter so festgelegt?",
       ["Damit man aus dem gesehenen Licht auf die Lage schließen kann.",
        "Wegen der Bauweise der Laternen.",
        "Historischer Zufall.",
        "Um Strom zu sparen."], 0,
       "Welches Licht man sieht, sagt, aus welcher Richtung man auf das "
       "andere Fahrzeug schaut — und daraus folgt die Ausweichpflicht."),
],

# ===========================================================================
"w-wind": [
    zahl("Bei welcher Windstärke in Beaufort bleiben Jollen üblicherweise "
         "im Hafen?",
         6, "Beaufort",
         "Ab 6 Beaufort, also knapp 40 km/h, gilt auf Binnenseen "
         "Starkwindwarnung. Für eine Jolle ist das die Grenze.",
         toleranz=0.2),
    mc("Wie erkennt man 4 Beaufort auf dem Wasser?",
       ["Viele kleine Schaumköpfe.",
        "Spiegelglatte See.",
        "Nur Kräuselwellen.",
        "Gischtstreifen."], 0,
       "Ab 3 Beaufort einzelne Schaumköpfe, ab 4 viele, ab 5 überall und "
       "etwas Gischt."),
    mc("Woran erkennt man eine herannahende Bö auf dem Wasser?",
       ["An einer dunklen, gekräuselten Fläche.",
        "An heller werdendem Wasser.",
        "An zunehmender Welle.",
        "Gar nicht."], 0,
       "Die stärkere Kräuselung streut das Licht anders. Wer den "
       "Wasserspiegel im Blick hat, sieht Böen kommen."),
    mc("Aus welcher Richtung kommen Böen meist relativ zum Grundwind?",
       ["Etwas raumer, also weiter achterlich.",
        "Genau aus derselben Richtung.",
        "Genau entgegengesetzt.",
        "Immer von Backbord."], 0,
       "Der Wind aus der Höhe wird heruntergemischt und hat dort eine "
       "andere Richtung — deshalb der Dreher."),
    mc("Was ist ein Fallwind?",
       ["Kalte Luft, die von einem Hang herunterfällt.",
        "Ein Wind, der abends einschläft.",
        "Der Wind hinter einem Segel.",
        "Ein Wirbel im Lee einer Insel."], 0,
       "An Alpenseen kann er ohne Vorwarnung mit großer Stärke einfallen — "
       "eine der Ursachen für plötzliche Kenterungen."),
    mc("Was ist die Windabdeckung durch ein Ufer?",
       ["Ein Bereich mit weniger und unstetigerem Wind im Lee des Ufers.",
        "Ein Bereich mit stärkerem Wind.",
        "Eine Untiefe.",
        "Eine Zone mit Strömung."], 0,
       "Im Lee einer Baumreihe oder eines Hügels wechselt der Wind Stärke "
       "und Richtung — dort ist Segeln mühsam und lehrreich."),
    mc("Was ist eine Düsenwirkung?",
       ["Wind, der zwischen Hindernissen beschleunigt wird.",
        "Ein Wirbel hinter dem Segel.",
        "Die Beschleunigung durch den Fahrtwind.",
        "Ein Fallwind."], 0,
       "Zwischen zwei Uferhügeln oder in einer Bucht kann der Wind deutlich "
       "stärker sein als auf dem freien See."),
    zahl("Wie viele km/h sind ungefähr 5 m/s?",
         18, "km/h",
         "Mal 3,6: 5 × 3,6 = 18 km/h. Umgekehrt teilt man km/h durch 3,6, "
         "um m/s zu bekommen.", toleranz=0.08),
    zahl("Wie viele m/s sind etwa 20 Knoten?",
         10.3, "m/s",
         "Ein Knoten ist 1,852 km/h, also rund 0,514 m/s. 20 × 0,514 ≈ "
         "10,3 m/s — grob gerechnet: Knoten halbieren.",
         toleranz=0.1),
    mc("Was ist die Seebrise?",
       ["Ein Wind vom Wasser zum Land, tagsüber durch Erwärmung des Landes.",
        "Ein Wind vom Land zum Wasser.",
        "Der Wind bei Sonnenuntergang.",
        "Ein Sturmwind."], 0,
       "Tagsüber erwärmt sich das Land schneller, die Luft steigt auf und "
       "zieht kühlere Luft vom Wasser nach. Nachts kehrt sich das um."),
    mc("Wann weht der Landwind?",
       ["Nachts und am frühen Morgen.",
        "Am Nachmittag.", "Mittags.", "Bei Sturm."], 0,
       "Nachts kühlt das Land schneller aus als das Wasser, und die Luft "
       "fließt zum See hin."),
    mc("Was besagt die Faustregel „Wind dreht rechts mit der Höhe\"?",
       ["In der Nordhalbkugel dreht der Wind mit zunehmender Höhe im "
        "Uhrzeigersinn.",
        "Der Wind dreht am Nachmittag nach rechts.",
        "Böen kommen von rechts.",
        "Sie gilt nur am Meer."], 0,
       "Die Reibung am Boden bremst und dreht den Wind; mit der Höhe "
       "nimmt beides ab. Deshalb kommen heruntergemischte Böen raumer."),
    mc("Woraus liest man kommendes Schlechtwetter am Himmel zuerst ab?",
       ["Aus hohen, dünnen Eiswolken, die sich verdichten.",
        "Aus Quellwolken am Nachmittag.",
        "Aus Bodennebel.",
        "Aus dem Sonnenuntergang."], 0,
       "Cirrus, der zu Cirrostratus mit Halo wird, kündigt eine Warmfront "
       "einen Tag im Voraus an."),
    mc("Was bedeutet rasch fallender Luftdruck?",
       ["Windzunahme und Wetterverschlechterung.",
        "Beständiges Wetter.",
        "Nebelbildung.",
        "Nichts Bestimmtes."], 0,
       "Je schneller der Druck fällt, desto kräftiger wird es. Ein "
       "Barometer an Bord ist deshalb mehr wert als sein Preis."),
    mc("Was sind Kräuselwellen ohne Schaumköpfe ein Zeichen für?",
       ["Schwachen Wind, etwa 1 bis 2 Beaufort.",
        "4 Beaufort.", "Sturm.", "Windstille."], 0,
       "Bei Windstille ist der Spiegel glatt; Kräuselwellen ohne Schaum "
       "bedeuten 1 bis 2, einzelne Schaumköpfe 3."),
    mc("Warum ist die Wellenhöhe auf einem See kleiner als am Meer?",
       ["Weil der Windweg (Fetch) kürzer ist.",
        "Weil Süßwasser leichter ist.",
        "Weil der See flacher ist.",
        "Weil der Wind schwächer ist."], 0,
       "Wellen brauchen Strecke, um aufzulaufen. Auf einem See sind sie "
       "dafür kürzer und steiler — unangenehmer als die Höhe vermuten "
       "lässt."),
    mc("Was sind kurze, steile Wellen für ein kleines Boot?",
       ["Unangenehmer als lange hohe Wellen.",
        "Harmloser.",
        "Gleichwertig.",
        "Schneller zu durchfahren."], 0,
       "Das Boot kommt nicht darüber hinweg, sondern hinein. Genau das "
       "macht Binnenseen bei Wind anspruchsvoll."),
    mc("Welche Windrichtung ist auf einem See besonders zu beachten?",
       ["Ablandiger Wind — er treibt Boote und Schwimmer vom Ufer weg.",
        "Auflandiger Wind.",
        "Wind von Süden.",
        "Die Richtung ist gleichgültig."], 0,
       "Bei ablandigem Wind sieht es am Ufer harmlos aus, und draußen "
       "steht die volle Stärke. Die Rückkehr geht dann gegenan."),
    mc("Was ist beim Segeln in Ufernähe mit Bäumen zu erwarten?",
       ["Abdeckung, Drehungen und plötzliche Böen.",
        "Gleichmäßig stärkeren Wind.",
        "Gar keinen Wind.",
        "Stets ablandigen Wind."], 0,
       "Hindernisse machen den Wind unstet. Wer dort segelt, hält die "
       "Schot in der Hand und nicht in der Klemme."),
    mc("Wo findet man auf einem See meist den beständigsten Wind?",
       ["In der Seemitte, weit von Hindernissen.",
        "Direkt am Ufer.",
        "In Buchten.",
        "Hinter Inseln."], 0,
       "Je weiter vom Ufer, desto gleichmäßiger — dafür ist der Rückweg "
       "länger, wenn etwas passiert."),
],

# ===========================================================================
"w-gewitter": [
    mc("Wie weit kann die Böenfront einem Gewitter vorauslaufen?",
       ["Bis etwa 20 km.", "Etwa 1 km.",
        "Etwa 100 m.", "Sie läuft hinterher."], 0,
       "Deshalb kann es bei blauem Himmel über dem eigenen Kopf schon "
       "gefährlich werden."),
    mc("Um welchen Faktor kann der Wind in einer Gewitterbö zunehmen?",
       ["Auf das Zwei- bis Dreifache.",
        "Um etwa zehn Prozent.",
        "Er nimmt ab.",
        "Er bleibt gleich."], 0,
       "Aus 4 Beaufort werden binnen Minuten 8 — und der Winddruck wächst "
       "mit dem Quadrat, also auf das Vier- bis Neunfache."),
    mc("Was tut man bei aufziehendem Gewitter zuerst?",
       ["Den nächsten Schutz ansteuern und Segel verkleinern.",
        "Alle Segel setzen, um schneller zu sein.",
        "Ankern.",
        "Abwarten."], 0,
       "Die Entscheidung früh treffen: Später ist Segelbergen im "
       "Starkwind ein eigenes Problem."),
    mc("Warum soll die Mannschaft bei Gewitter in die Plicht?",
       ["Damit niemand über Bord geht und alle Westen tragen.",
        "Wegen des Blitzschlags im Mast.",
        "Damit das Boot besser trimmt.",
        "Damit man besser sieht."], 0,
       "Auf dem Vorschiff zu arbeiten ist genau das, was man in der Bö "
       "vermeiden will."),
    mc("Wie verhält man sich, wenn das Gewitter da ist?",
       ["Unter Motor mit dem Bug gegen die Böen halten.",
        "Vor dem Wind laufen.",
        "Quer zum Wind liegen bleiben.",
        "Ankern und Segel setzen lassen."], 0,
       "Gegen die Böen ist die Angriffsfläche am kleinsten und das Boot am "
       "besten steuerbar."),
    mc("Was ist ein Blitzschlagrisiko an Bord?",
       ["Der Mast ist oft der höchste Punkt weit und breit.",
        "Die Segel ziehen Blitze an.",
        "Das Wasser ist leitend, also ungefährlich.",
        "Es gibt keines."], 0,
       "Deshalb: Metallteile und Wanten nicht berühren, möglichst in die "
       "Mitte der Plicht, nichts über Bord hängen lassen."),
    mc("Welche Faustregel gibt es für die Entfernung eines Gewitters?",
       ["Sekunden zwischen Blitz und Donner durch drei ergibt Kilometer.",
        "Sekunden mal drei.",
        "Sekunden gleich Kilometer.",
        "Es gibt keine."], 0,
       "Der Schall braucht rund drei Sekunden je Kilometer. Neun Sekunden "
       "heißen also etwa drei Kilometer."),
    zahl("Zwischen Blitz und Donner vergehen 12 Sekunden. Wie weit ist das "
         "Gewitter?",
         4, "km",
         "12 geteilt durch 3 ergibt 4 km. Bei weniger als 10 Sekunden ist "
         "es Zeit, nicht mehr über die Rückkehr nachzudenken, sondern sie "
         "auszuführen.", toleranz=0.15),
    mc("Was ist die Böenwalze?",
       ["Eine dunkle, waagrecht liegende Wolkenrolle an der Unterkante.",
        "Der Amboss oben.",
        "Ein Regenschleier.",
        "Eine Nebelbank."], 0,
       "Sie markiert die Vorderkante der ausfließenden Kaltluft — ihr "
       "Erscheinen heißt: jetzt kommt der Wind."),
    mc("Was zeigt ein plötzlicher Temperatursturz vor einem Gewitter an?",
       ["Die ausfließende Kaltluft ist da; der Wind kommt sofort.",
        "Das Gewitter zieht ab.",
        "Es wird nur regnen.",
        "Nichts Besonderes."], 0,
       "Temperatursturz und Windsprung gehören zusammen und sind die "
       "letzte Vorwarnung."),
    mc("Welche Ausrüstung ist bei Gewitter griffbereit?",
       ["Rettungswesten, Lenzmittel und ein Messer.",
        "Der Spinnaker.",
        "Die Badeleiter.",
        "Der Kocher."], 0,
       "Ein Messer, weil eine klemmende Schot bei einer Bö der Unterschied "
       "sein kann."),
    mc("Warum ist ein Gewitter auf einem Binnensee besonders tückisch?",
       ["Es entsteht und trifft schnell, und das Ufer ist trügerisch nah.",
        "Weil es länger dauert als am Meer.",
        "Weil es dort mehr Blitze gibt.",
        "Weil die Wellen höher sind."], 0,
       "Auf 3 km zum Ufer bleibt bei 6 Beaufort gegenan keine halbe "
       "Stunde — und genau die fehlt dann."),
    mc("Was ist bei Hitzegewittern typisch für die Tageszeit?",
       ["Sie entstehen meist am Nachmittag und Abend.",
        "Am Vormittag.", "Nachts.", "Zu jeder Zeit gleich."], 0,
       "Der Boden braucht Zeit, um genug Energie zu sammeln. Frühstarter "
       "sind deshalb im Vorteil."),
    mc("Was ist eine Kaltfront in Bezug auf Gewitter?",
       ["Sie kann eine ganze Linie von Gewittern bringen.",
        "Sie bringt nur Regen.",
        "Sie löst Gewitter auf.",
        "Sie hat keinen Einfluss."], 0,
       "Frontgewitter ziehen als Linie durch und sind oft heftiger als "
       "einzelne Hitzegewitter — dafür sind sie besser vorhersagbar."),
    mc("Was gehört zur Vorbereitung eines Segeltages?",
       ["Wetterbericht, Warnungen und ein Plan für die Rückkehr.",
        "Nur der Blick zum Himmel.",
        "Nur die Ausrüstung prüfen.",
        "Nichts Besonderes."], 0,
       "Die meisten Wetterunfälle auf Binnenseen wären durch einen Blick "
       "auf die Vorhersage vermeidbar gewesen."),
    mc("Woher bekommt man Warnungen auf einem österreichischen See?",
       ["Von den Uferwarnleuchten und aus dem Wetterbericht.",
        "Nur vom Segelverein.",
        "Nur über Funk.",
        "Es gibt keine."], 0,
       "Die Leuchten sind weithin sichtbar, und 40 gegen 90 Blitze je "
       "Minute lassen sich gut unterscheiden."),
    mc("Was tut man, wenn die Sturmwarnung erst auf dem Wasser beginnt?",
       ["Sofort den nächsten Schutz ansteuern.",
        "Weiterfahren wie geplant.",
        "Ankern und abwarten.",
        "Segel bergen und treiben lassen."], 0,
       "90 Blitze je Minute heißen: Es wird für jedes Boot ungemütlich. "
       "Die Warnung kommt so früh, dass der nächste Hafen erreichbar ist."),
    mc("Was ist zu tun, wenn Wasser ins Boot kommt?",
       ["Lenzen und die Ursache suchen, Besatzung in Westen.",
        "Nur lenzen.",
        "Nur die Ursache suchen.",
        "Sofort das Boot verlassen."], 0,
       "Beides zugleich: Wer nur lenzt, verliert gegen ein Leck; wer nur "
       "sucht, wird überholt."),
    mc("Wann verlässt man ein Boot?",
       ["Erst, wenn es sicher sinkt — es schwimmt meist länger als man "
        "denkt.",
        "Sobald Wasser eindringt.",
        "Bei Gewitter.",
        "Bei Mastbruch."], 0,
       "Ein havariertes Boot ist eine große, sichtbare Plattform. Im Wasser "
       "ist man klein, kalt und unsichtbar."),
    mc("Was tut man nach einem Mastbruch zuerst?",
       ["Personen sichern, dann das Rigg sichern oder kappen.",
        "Sofort den Mast bergen.",
        "Den Motor starten.",
        "Funken."], 0,
       "Ein treibender Mast an Wanten schlägt gegen den Rumpf und kann ihn "
       "aufschlagen. Deshalb gehört ein Bolzenschneider oder Messer an "
       "Bord."),
],

# ===========================================================================
"u-recht": [
    mc("Wer darf das Kommando an Bord führen?",
       ["Wer die nötige Befähigung und Eignung hat.",
        "Der Eigner, immer.",
        "Der Älteste.",
        "Wer zuerst am Steg ist."], 0,
       "Und wer es führt, trägt die Verantwortung — unabhängig davon, wer "
       "gerade das Ruder hält."),
    mc("Was gehört zur Sorgfaltspflicht vor dem Ablegen?",
       ["Boot, Ausrüstung, Wetter und Besatzung prüfen.",
        "Nur den Tank prüfen.",
        "Nur die Segel prüfen.",
        "Nichts, wenn man den Platz kennt."], 0,
       "Diese Prüfung ist keine Formsache: Fast jede Kette, die zum Unfall "
       "führt, beginnt mit einem übersehenen Punkt am Steg."),
    mc("Darf man Abfall über Bord geben?",
       ["Nein, nichts davon.",
        "Nur Biologisches.",
        "Nur in der Seemitte.",
        "Nur Papier."], 0,
       "Auch Speisereste verändern das Gleichgewicht eines Sees. Alles "
       "kommt zurück an Land."),
    mc("Was ist mit Abwasser aus einer Bordtoilette zu tun?",
       ["In einen Sammeltank und an der Station entsorgen.",
        "Über Bord in der Seemitte.",
        "Nachts über Bord.",
        "Mit Chemie behandeln und über Bord."], 0,
       "Auf Binnengewässern gilt praktisch überall Einleitverbot."),
    mc("Was tut man bei einem Ölaustritt aus dem Motor?",
       ["Aufnehmen, melden und nicht verteilen.",
        "Mit Spülmittel auflösen.",
        "Abwarten.",
        "Nichts, es verdunstet."], 0,
       "Spülmittel verteilt das Öl nur feiner und macht es schwerer "
       "aufzunehmen. Ölbindemittel gehört an Bord."),
    mc("Wie verhält man sich in Naturschutzgebieten?",
       ["Langsam, leise, Abstand halten und gekennzeichnete Zonen meiden.",
        "Wie überall.",
        "Nur nachts meiden.",
        "Nur mit Motor meiden."], 0,
       "Brutvögel reagieren auf Annäherung lange bevor man sie überhaupt "
       "bemerkt."),
    mc("Was ist beim Waschen des Bootes zu beachten?",
       ["Keine Reinigungsmittel ins Wasser; an Land mit Abscheider "
        "arbeiten.",
        "Nur biologische Mittel über Bord.",
        "Nur Süßwasser verwenden.",
        "Es gibt keine Auflagen."], 0,
       "Auch als biologisch abbaubar verkaufte Mittel belasten das "
       "Gewässer unmittelbar."),
    mc("Was ist der Schwojkreis beim Ankern?",
       ["Der Kreis, den das Boot um seinen Anker beschreiben kann.",
        "Der Wendekreis des Bootes.",
        "Der Sicherheitsabstand zum Ufer.",
        "Die Ankerkette."], 0,
       "Er muss frei bleiben — auch dann, wenn der Wind dreht und "
       "Nachbarboote anders schwojen."),
    mc("Darf man überall ankern?",
       ["Nein, Ankerverbote und Schutzzonen sind zu beachten.",
        "Ja, überall.",
        "Nur nachts.",
        "Nur in Buchten."], 0,
       "Kabel, Leitungen, Schutzgebiete und Fahrwasser sind typische "
       "Ankerverbotszonen."),
    mc("Was gilt für Lärm an Bord?",
       ["Rücksicht, besonders in Ufernähe und nachts.",
        "Keine Einschränkung.",
        "Nur nach 22 Uhr.",
        "Nur im Hafen."], 0,
       "Schall trägt über Wasser weit — deutlich weiter, als es an Bord "
       "wirkt."),
    mc("Wie verhält man sich gegenüber Anglern?",
       ["Abstand halten, nicht über die Schnur fahren.",
        "Angler müssen ausweichen.",
        "Dicht vorbeifahren ist erlaubt.",
        "Es gelten keine Regeln."], 0,
       "Verankerte Boote und ausgelegte Schnüre sind schlecht sichtbar; "
       "eine gekappte Schnur ist leicht passiert."),
    mc("Was ist bei Regatten als Nichtteilnehmer zu beachten?",
       ["Abstand halten und die Bahn nicht queren.",
        "Man hat Vorrang.",
        "Man darf mitsegeln.",
        "Regattafelder weichen aus."], 0,
       "Regattaboote segeln nach eigenen Regeln und konzentriert; "
       "Durchfahren stört und ist gefährlich."),
    mc("Welche Pflicht besteht gegenüber in Not geratenen Personen?",
       ["Hilfe zu leisten, soweit ohne eigene Gefährdung möglich.",
        "Keine.",
        "Nur die Behörde zu verständigen.",
        "Nur bei eigener Beteiligung."], 0,
       "Auf dem Wasser ist das nächste Boot oft die einzige erreichbare "
       "Hilfe."),
    mc("Was ist nach einer Kollision zu tun?",
       ["Personen prüfen, Hilfe leisten, Daten austauschen, melden.",
        "Weiterfahren bei geringem Schaden.",
        "Nur die Versicherung informieren.",
        "Nur bei Verletzten melden."], 0,
       "Die Reihenfolge ist dieselbe wie an Land: Menschen, dann Sachen, "
       "dann Formalitäten."),
    mc("Wer haftet für Schäden durch Wellenschlag?",
       ["Der Verursacher.",
        "Niemand.",
        "Der Geschädigte.",
        "Die Hafenverwaltung."], 0,
       "Wellenschlag ist ein häufiger Schadensgrund an Stegen und "
       "liegenden Booten — und er ist zurechenbar."),
    mc("Was besagt das Rücksichtnahmegebot?",
       ["Niemand darf andere gefährden, schädigen oder mehr als nötig "
        "behindern.",
        "Nur Berufsschiffer müssen Rücksicht nehmen.",
        "Es gilt nur im Hafen.",
        "Es ist eine Empfehlung."], 0,
       "Es steht über den Einzelregeln und füllt jede Lücke, die sie "
       "lassen."),
    mc("Wie alt muss man mindestens sein, um ein Boot selbständig zu "
       "führen?",
       ["Das hängt von Gewässer und Bootsgröße ab.",
        "Immer 18.", "Immer 16.", "Es gibt keine Grenze."], 0,
       "Die Altersgrenzen stehen in den jeweiligen Verordnungen und "
       "unterscheiden sich nach Antrieb und Länge."),
    mc("Was ist ein Befähigungsausweis?",
       ["Der amtliche Nachweis, ein bestimmtes Fahrzeug führen zu dürfen.",
        "Die Zulassung des Bootes.",
        "Die Versicherungsbestätigung.",
        "Die Vereinsmitgliedschaft."], 0,
       "Er gilt für bestimmte Fahrzeugarten und Fahrtbereiche — und nur "
       "dafür."),
    mc("Was ist zu tun, wenn der Ausweis verloren geht?",
       ["Ersatz bei der ausstellenden Stelle beantragen.",
        "Ohne weiterfahren.",
        "Eine Kopie genügt dauerhaft.",
        "Nichts."], 0,
       "Bis zum Ersatz kann eine Bestätigung helfen; das Mitführen bleibt "
       "Pflicht."),
    mc("Was ist der beste Schutz vor rechtlichen Problemen auf dem Wasser?",
       ["Vorausschauend und rücksichtsvoll fahren.",
        "Eine gute Versicherung.",
        "Kenntnis aller Paragraphen.",
        "Ein großes Boot."], 0,
       "Die Regeln sind Werkzeuge zur Vermeidung von Zusammenstößen. Wer "
       "so fährt, braucht sie selten."),
],
})
