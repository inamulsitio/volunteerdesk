# === Stage 46: Add a schema version field and migration helper ===
# Project: VolunteerDesk
def bump_schema_version():
    """Bump the schema version and log a migration notice."""
    import json
    from datetime import datetime

    with open("volunteer_desk.json", "r") as f:
        data = json.load(f)

    if "schema_version" not in data:
        data["schema_version"] = 1
    data["schema_version"] += 1
    data["migration_log"] = data.get("migration_log", [])
    data["migration_log"].append({
        "version": data["schema_version"],
        "timestamp": datetime.utcnow().isoformat(),
        "note": "Schema version bumped",
    })

    with open("volunteer_desk.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Schema migrated to v{data['schema_version']}")
