# doe25-slutuppgift
# Övervakningsapplikation


Körbara filer och struktur:
- main.py - startpunkt för programmet (konsolmeny)
- monitor.py - samlar systeminfo (CPU, minne, disk)
- alarms.py - Alarm- och AlarmManager-klasser
- storage.py - sparar/laddar larm (JSON)
- logger.py - loggning till fil med datum/tid i filnamnet
- utils.py - hjälpfunktioner (validering, formatering)
- requirements.txt


## Installation
1. Skapa virtuell miljö (rekommenderas)


```bash
python -m venv venv
source venv/bin/activate # mac/linux
venv\Scripts\activate # windows
pip install -r requirements.txt
