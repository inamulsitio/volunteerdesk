# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: VolunteerDesk
def normalize_report(report):
    normalized = {}
    for key, value in report.items():
        if isinstance(value, list):
            normalized[key] = [item for item in value]
        else:
            normalized[key] = value
    return normalized


def compare_reports(report_a, report_b):
    normalized_a = normalize_report(report_a)
    normalized_b = normalize_report(report_b)

    keys = set(normalized_a.keys()) | set(normalized_b.keys())

    differences = []
    for key in sorted(keys):
        value_a = normalized_a.get(key)
        value_b = normalized_b.get(key)

        if value_a != value_b:
            differences.append({
                "key": key,
                "report_a": value_a,
                "report_b": value_b,
            })

    return differences


def summarize_comparison(differences):
    summary = {
        "total_differences": len(differences),
        "changed_keys": [diff["key"] for diff in differences],
    }
    return summary
