# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: VolunteerDesk
def bulk_delete(self, entity_type: str, confirm: bool = False) -> int:
    """Delete multiple records of a given type. Requires confirm=True to proceed."""
    if confirm:
        deleted = []
        for record in self._entities.get(entity_type, []):
            self._entities[entity_type].remove(record)
            deleted.append(record)
        return len(deleted)
    else:
        raise ValueError(f"Confirmation required to delete {entity_type} records. Set confirm=True.")
