import json
from alarms import Alarm

def load_alarms_from_file(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            alarms_data = json.load(file)
        alarms = []
        for alarm_entry in alarms_data:
            if 'threshold' not in alarm_entry:
                raise ValueError("Alarm entry missing 'threshold' key.")
            try:
                threshold_value = int(alarm_entry['threshold'])
            except Exception as error:
                raise ValueError(f"Invalid threshold value for alarm: {alarm_entry.get('threshold')}") from error
            alarms.append(Alarm(alarm_entry['alarm_type'], threshold_value))
        return alarms
    except FileNotFoundError:
        return []
    
def save_alarms_to_file(alarms, filename: str):
    alarms_data = [{'alarm_type': alarm.alarm_type, 'threshold': alarm.threshold} for alarm in alarms]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(alarms_data, file, indent=2, ensure_ascii=False)