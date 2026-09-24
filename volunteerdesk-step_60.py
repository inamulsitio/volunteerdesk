# === Stage 60: Add saved views for frequently used filters ===
# Project: VolunteerDesk
class SavedView:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    def apply(self, queryset):
        for key, value in self.filters.items():
            if value is not None:
                if key == 'status':
                    queryset = queryset.filter(status=value)
                elif key == 'role':
                    queryset = queryset.filter(role__name=value)
                elif key == 'date_from':
                    queryset = queryset.filter(date_from__gte=value)
                elif key == 'date_to':
                    queryset = queryset.filter(date_to__lte=value)
        return queryset

    def __repr__(self):
        return f"<SavedView {self.name!r} filters={self.filters!r}>"
