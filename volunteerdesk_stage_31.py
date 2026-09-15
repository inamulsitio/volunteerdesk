# === Stage 31: Add compact table rendering for long lists ===
# Project: VolunteerDesk
def render_compact_table(headers, rows, max_rows=30):
    """Render a compact table from headers and rows, limiting to max_rows."""
    if not headers:
        return ""
    lines = []
    col_widths = [len(str(h)) for h in headers]
    for row in rows[:max_rows]:
        cells = [str(c) if c is not None else "" for c in row]
        for i, cell in enumerate(cells):
            col_widths[i] = max(col_widths[i], len(cell))
        lines.append(" | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(cells)))
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    lines[0] = header_line
    return "\n".join(lines)
