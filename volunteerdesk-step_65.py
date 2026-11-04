# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: VolunteerDesk
def merge_imports(existing_imports, new_imports):
    merged = list(existing_imports)
    for imp in new_imports:
        if not any(_imports_match(a, imp) for a in merged):
            merged.append(imp)
    return merged

def _imports_match(a, b):
    if a == b:
        return True
    try:
        a_mod = a.split(".")[0]
        b_mod = b.split(".")[0]
        return a_mod == b_mod
    except Exception:
        return False
