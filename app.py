from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
model = joblib.load(MODEL_PATH)

FEATURES = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]

app = Flask(__name__, template_folder="templates")


@app.get("/health")
def health():
    """Return service health status and expected feature order."""
    return {"ok": True, "features": FEATURES}


@app.post("/predict")
def predict():
    """Validate 8 numeric features from JSON payload and return model prediction."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error=f"Expected 8 features: {FEATURES}"), 400
    x = data.get("features")
    if not isinstance(x, list) or len(x) != len(FEATURES):
        return jsonify(error=f"Expected 8 features: {FEATURES}"), 400
    if any(isinstance(v, bool) for v in x):
        return jsonify(error="All features must be convertible to floats."), 400
    try:
        vals = [float(v) for v in x]
    except (TypeError, ValueError):
        return jsonify(error="All features must be convertible to floats."), 400
    if not np.all(np.isfinite(vals)):
        return jsonify(error="All features must be finite numbers."), 400
    X = np.array([vals], dtype=float)
    yhat = float(model.predict(X).tolist()[0])
    return jsonify(prediction=yhat)


@app.route("/", methods=["GET", "POST"])
def main():
    """Render the web UI form and handle optional form POST submissions."""
    if request.method == "GET":
        return render_template("main.html")
    vals = [float(request.form.get(f)) for f in FEATURES]
    pred = float(model.predict(np.array([vals])).tolist()[0])
    return render_template("main.html", prediction=pred)


if __name__ == "__main__":
    app.run(debug=True)
