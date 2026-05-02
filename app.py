from flask import Flask, render_template, request

app = Flask(__name__)

# =========================
# MAPPINGS
# =========================
study_method_map = {
    "coaching": 1.00,
    "mixed": 0.5,
    "group study": 0.2,
    "online videos": 0.1,
    "self-study": 0.00
}

sleep_quality_map = {
    "poor": 0.0,
    "average": 0.5,
    "good": 1.0
}

facility_map = {
    "low": 0.0,
    "medium": 0.5,
    "high": 1.0
}

internet_map = {
    "no": 0.0,
    "yes": 1.0
}

difficulty_map = {
    "hard": 0.0,
    "moderate": 0.5,
    "easy": 1.0
}

# =========================
# RANGE RULES
# =========================
def map_study_hours(x):
    if x < 2: return 0.2
    elif x < 4: return 0.5
    elif x < 6: return 0.8
    else: return 1.0

def map_attendance(x):
    if x < 60: return 0.2
    elif x < 75: return 0.5
    elif x < 90: return 0.8
    else: return 1.0

def map_sleep_hours(x):
    if x < 5: return 0.2
    elif x < 6.5: return 0.5
    elif x <= 8: return 1.0
    else: return 0.7

# =========================
# WEIGHTS
# =========================
weights = {
    "internet_access": 0.0054,
    "sleep_quality": 0.0420,
    "study_method": 0.0451,
    "facility_rating": 0.0300,
    "exam_difficulty": 0.0122,
    "study_hours": 0.5755,
    "class_attendance": 0.1549,
    "sleep_hours": 0.0679
}

# normalize weights
total = sum(weights.values())
weights = {k: v / total for k, v in weights.items()}

# =========================
# ROUTES
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # get input

        study_method = study_method_map[request.form["study_method"]]
        sleep_quality = sleep_quality_map[request.form["sleep_quality"]]
        facility = facility_map[request.form["facility"]]
        internet = internet_map[request.form["internet"]]
        difficulty = difficulty_map[request.form["difficulty"]]

        # apply rules
        features = {
            "study_hours": float(request.form["study_hours"]),
            "class_attendance": float(request.form["attendance"]),
            "sleep_hours": float(request.form["sleep_hours"]),
            "study_method": study_method,
            "sleep_quality": sleep_quality,
            "facility_rating": facility,
            "internet_access": internet,
            "exam_difficulty": difficulty
        }

        # SAW
        saw_score = sum(features[k] * weights[k] for k in features)
        saw_score_100 = saw_score * 100

        # pass/fail
        passed = saw_score_100 >= 60

        result = {
            "score": round(saw_score_100, 2),
            "status": "PASS" if passed else "FAIL"
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)