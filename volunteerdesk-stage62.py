# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: VolunteerDesk
def recommend_volunteers(shifts, volunteers):
    scores = {}
    for v in volunteers:
        score = 0
        if shifts and v['shifts']:
            score += 10
        if v['hours'] >= 20:
            score += 5
        if v['skills'].issuperset(shifts[0]['skills']):
            score += 15
        if not v['notes_sent']:
            score += 8
        scores[v['name']] = score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
