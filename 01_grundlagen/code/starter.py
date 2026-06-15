"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# rabatt sollte durch 100 geteilt werden.

# Defect (fehlerhafte Stelle im Code):
# Zeile 19

# Failure (was der Benutzer bemerken würde):
# eine ungueltige und minuse Anzahl rauskommt. 


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    rabatt = preis * prozent / 100
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))
    print(berechne_rabatt_korrigiert(100.0, 0))
    print(berechne_rabatt_korrigiert(100.0, 100))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | *        |           |
# | Programm mit Testdaten ausführen    |          | *         |
# | Syntaxprüfung durch den Editor      | *        |           |
# | Walkthroughs im Team                | *        |           |
# | Unit-Tests laufen lassen            |          | *         |
# | Checklisten für Codestruktur        | *        |           |
#
# Warum reicht statisches Testen allein nicht aus?
# manualle Code Lesen und Testen koennte auch fehlahaft sein. Ausserdem 
# nach jeder Aenderung im Code muss man alle betroffene Code noch mal Ueberpruefen. 
# Ob man eine standarade Massnahme behalten kann, ist eine Frage. 


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
