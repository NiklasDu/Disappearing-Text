# Disappearing Text App

Die **Disappearing Text App** ist eine einfache Anwendung, die mit PyQt6 erstellt wurde. Sie bietet eine interaktive Benutzeroberfläche, in der Benutzer Texte schreiben können, die nach einer bestimmten Zeit automatisch gelöscht werden, wenn keine Eingabe erfolgt. Die App enthält außerdem eine Funktion zum Speichern von Texten.

## Features

- **Timer-basierte Textlöschung**: Der eingegebene Text wird nach 10 Sekunden Inaktivität automatisch gelöscht.
- **Text speichern**: Benutzer können ihren Text speichern, bevor er gelöscht wird. Die gespeicherten Texte werden in einer JSON-Datei gespeichert.
- **Ansprechendes Design**: Die App verwendet ein modernes und minimalistisches Farbschema.

## Installation

1. **Repository klonen**:
   ```bash
   git clone <repository-url>
   cd Disappearing-Text

2. **Abhängigkeiten installieren**: 
    Stelle sicher, dass Python 3.10+ installiert ist. Installiere die benötigten Pakete:
    pip install -r requirements.txt

3. **App starten**:
    python disappearing-text-app/main.py

## Verwendung
1. Starte die App.
2. Schreibe deinen Text in das Eingabefeld.
3. Der Timer zeigt die verbleibenden Sekunden an, bevor der Text gelöscht wird.
4. Klicke auf "Save Text", um deinen Text zu speichern.

## Anpassungen
- Designfarben: Die Farben der App können in der Datei constants.py angepasst werden.
- Speicherpfad: Der Speicherpfad für die Texte ist in der Konstanten FILEPATH in constants.py definiert.

## Vorschläge für zukünftige Features
- Anpassbarer Timer.
- Unterstützung für mehrere Sprachen.


Viel Spaß beim Verwenden der Disappearing Text App! 