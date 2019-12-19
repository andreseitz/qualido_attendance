# Anwesenheitskontrolle über Qualido

## Use Case

Jedes Mitglied kann sich für eine in Qualido gepflegte Veranstaltaltung als anwesend eintragen, indem ein persönlicher Barcode gescannt wird.

## Einschränkungen

* Termin muss durch einen Qualido-Admin im Vorfeld in Qualido angelegt sein und das richtige Publikum eingeladen werden.
* Am Austragungsort muss Internet verfügbar sein.
* Am Termin muss ein Qualido-Admin anwesend sein, der die Anwesenheitserfassung auf Qualido durchführen kann.
* Das System zur Anwesenheitserfassung muss vor Ort und mit dem Internet verbunden sein.
* Ein Smartphone muss für die Barcodeerfassung eingereichtet und mit dem Erfassungssystem gekoppelt sein.

## Workflow

1. Setzen des Userkey/ID Felds auf die Qualido-Nutzer-ID
2. 

### Vorbereitung der User-Daten in Qualido

Als Admin muss in der Mitarbeiterverwaltung für jeden Nutzer unter Zusatzdaten das Feld Userkey/ID mit der ID des Nutzer befüllt werden. Die ID des Nutzers wird in der Titel-Leiste des PopUp-Fensters zum bearbeiten der mitarbeiterdaten mit angezeigt.

### Generierung der Barcodes

Zur Generierung der Barcodes muss als Admin die Liste der aktiven Mitglieder aus der Mitgliederverwaltung exportiert werden. Dazu müssen die Felder Vorname, Nachname und ID enthalten sein. Die Datei wird beispielsweise als export.xlsx abgelegt. Das Pythonscript qualido_barcode_generator erzeugt daraus ein PDF Dokument mit den zu den IDs passenden Barcodes.

```
python3 qualido_barcode_generator/qualido_barcode_generator.py -p export.xlsx
```

Die einzelnen Barcodes liegen anschließend im Ordner "barcodes", der fertige Katalog im Ordner "tex".

### Anlegen eines Termins in Qualido

Als Admin wählt man im Admin-Modus in Qualido im Menübaum "Termin & Ressourcen" aus. Über "Termin anlegen" öffnet sich ein Popup der zur Eingabe der Termindetails auffordert. Der Reiter "Stammdaten" ist auszufüllen. Im Reiter "Zielgruppen" sind alle angekreuzten Kreise zu deaktivieren und für die WW AIC sowohl "sieht" als auch "ziel" der Teilbaum "KV AICFDB - Gemeinschaften 502 - Wasserwacht 502 - OG Aichach" wieder anzukreuzen. Der Reiter "Zusatzinformationen" erfordert üblicherweise keine Änderungen. 

### Inbetriebnahme des Erfassungssystems



#### Smartphone als Barcodescanner

Auf dem Smartphone, das als Barcodescanner fungieren soll muss die App "Barcode to PC" installiert werden. Das Smartphone muss im selben WLAN hängen, wie das Erfassungssysstem. Gemäß den Ausgaben der App muss sich das Smartphone mit dem Erfassungssystem gekoppelt haben. Durch Auswahl des Kamera-Symbols und eines geeigneten Erfassungsmodus (Einzel- oder Mehrfach) wird die Erfassung gestartet.

#### Starten der Barcodeerfassung im Qualido

Am Erfassungssystem muss sich ein Admin im Qualido anmelden, im Admin-Modus den Termin auswählen,sowie über Anwesenheiten und Barcode-Erfassung die Erfassung starten. Der Cursor muss sich im Eingabefeld befinden.
