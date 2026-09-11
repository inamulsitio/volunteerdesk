# === Stage 22: Add favorite records and quick favorite listing ===
# Project: VolunteerDesk
from dataclasses import dataclass, field
from typing import List, Optional
import json
import os

@dataclass
class FavoriteRecord:
    name: str
    hours: float = 0.0
    note: str = ""
    tags: List[str] = field(default_factory=list)

    def to_dict(self):
        return {"name": self.name, "hours": self.hours, "note": self.note, "tags": self.tags}

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

class FavoriteManager:
    def __init__(self, file_path="favorites.json"):
        self.file_path = file_path
        self.records: List[FavoriteRecord] = []
        self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                self.records = [FavoriteRecord.from_dict(r) for r in data]
            except (json.JSONDecodeError, KeyError):
                self.records = []

    def add(self, name, hours=0.0, note="", tags=None):
        if tags is None:
            tags = []
        record = FavoriteRecord(name=name, hours=hours, note=note, tags=tags)
        if not any(r.name == name for r in self.records):
            self.records.append(record)
            self._save()
            return record
        return None

    def get_favorites(self):
        return self.records

    def get_by_name(self, name):
        for r in self.records:
            if r.name == name:
                return r
        return None

    def _save(self):
        with open(self.file_path, 'w') as f:
            json.dump([r.to_dict() for r in self.records], f, indent=2)

    def quick_list(self, limit=10):
        return self.records[:limit]
