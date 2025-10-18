# DOE25 Python final examniation
## Övervakningsapplikation | Monitoring application

Slutuppgiften går ut på att skriva en övervakningsapplikation skriven i Python. Applikation samlar in information från operativsystemet och presenterar informationen för en användare.

En användare kan interagera med applikationen via en konsol för att få fram information om CPU användning, minnesanvändning, diskanvändning. När användaren interagerar med applikationen via konsolmenyn ska inga konfigurerade larm aktiveras.

Körbara filer och struktur:
- main.py - startpunkt för programmet (konsolmeny)
- monitor.py - samlar systeminfo (CPU, minne, disk)
- alarms.py - Alarm- och AlarmManager-klasser
- storage.py - sparar/laddar larm (JSON)
- logger.py - loggning till fil med datum/tid i filnamnet
- utils.py - hjälpfunktioner
- requirements.txt

## Konsol meny startar med 7 val
=== Monitor application ===
1. Start monitoring (collect status, no alarms are triggered)
2. List active monitoring
3. Create alarm
4. Show created alarms
5. Start monitoring mode (alarms are triggered)
6. Remove alarm
7. Exit
Select an option (1-7):

## Installation
### 1. Klona repot
git clone https://github.com/fofysalman/doe25-slutuppgift.git

### 2. Skapa virtuell miljö (rekommenderas)
```bash
python -m venv venv
```

### 3. Aktivera miljön 
```bash
source venv/bin/activate # mac/linux
venv\Scripts\activate # windows
```

### 3. Installera paket
```bash
pip install -r requirements.txt
```