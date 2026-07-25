def calculate_ats_score(skills):
    keywords = [
        "python",
        "sql",
        "machine learning",
        "data analysis",
        "excel",
        "power bi",
        "communication",
        "problem solving",
        "teamwork",
        "pandas",
        "numpy"
    ]

    score = 0

    skills = skills.lower()

    matched = []

    for keyword in keywords:
        if keyword in skills:
            score += 10
            matched.append(keyword)

    if score > 100:
        score = 100

    missing = [k for k in keywords if k not in matched]

    return score, matched, missing