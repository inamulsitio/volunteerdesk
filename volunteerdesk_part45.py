# === Stage 45: Add restore from backup with validation ===
# Project: VolunteerDesk
import json
import os
from datetime import datetime

def restore_backup(backup_path, data_dir, validate=True):
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    if validate:
        with open(backup_path, 'r') as f:
            backup = json.load(f)
        required_keys = {'shifts', 'signups', 'hours', 'notes'}
        if not required_keys.issubset(backup.keys()):
            raise ValueError(f"Invalid backup: missing keys {required_keys - backup.keys()}")
    os.makedirs(data_dir, exist_ok=True)
    with open(backup_path, 'r') as src:
        with open(os.path.join(data_dir, 'volunteer_desk.json'), 'w') as dst:
            dst.write(src.read())
    print(f"Backup restored from {backup_path}")
