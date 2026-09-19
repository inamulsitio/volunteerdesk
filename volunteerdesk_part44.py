# === Stage 44: Add backup creation for the data file ===
# Project: VolunteerDesk
def backup_data_file():
    """Create a timestamped backup of the VolunteerDesk data file."""
    import shutil
    import os
    data_file = "volunteer_desk_data.csv"
    backup_file = data_file + ".bak"
    if os.path.exists(data_file):
        shutil.copy2(data_file, backup_file)
        print(f"Backup created: {backup_file}")
    else:
        print(f"Warning: {data_file} not found, cannot create backup.")
