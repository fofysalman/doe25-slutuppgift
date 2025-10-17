import json
from alarms import Alarm

def load_alarms_from_file(filename: str):
    """Load alarms from a JSON file and return a list of Alarm objects."""
    try:
        with open(filename, 'r', encoding='utf-8') as file: # Open the file in read (r) mode
            alarms_data = json.load(file) # Load the list of alarms from the file
        alarms = [] # Initialize an empty list to store Alarm objects
        for alarm_entry in alarms_data:
            # Expecting each alarm_entry in the JSON object to be a dict with 'type' and 'threshold' keys
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
    """Save a list of Alarm objects to a JSON file."""
    alarms_data = [{'alarm_type': alarm.alarm_type, 'threshold': alarm.threshold} for alarm in alarms]  # Convert Alarm objects to dicts
    with open(filename, 'w', encoding='utf-8') as file:  # Open the file in write (w) mode
        json.dump(alarms_data, file, indent=2, ensure_ascii=False) # Write the list of dicts to the file as JSON