# Task G2: Create `app.py` and `templates/main.html` and Test Locally

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to create the Flask server (`app.py`) and web UI form (`templates/main.html`) according to `README.original.md`, and verify all endpoints locally using `.venv`.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\app.py`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\templates\main.html`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G2-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Read the sections in `e:\Antigravity-Projects\ml-deployment-lab\README.original.md` for `app.py` and `templates/main.html`.
- **`app.py` requirements:**
  - Load `model/model.pkl` using `joblib`.
  - Define features in exact order: `["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]`.
  - `GET /`: render `main.html`.
  - `GET /health`: return HTTP 200 JSON `{"ok": true, "features": FEATURES}`.
  - `POST /predict`: accept JSON `{"features": [8 floats]}`, run model prediction, and return HTTP 200 JSON `{"prediction": <float>}`. Return HTTP 400 with an error JSON if `features` is missing, not a list of length 8, or cannot be converted to floats.
- **`templates/main.html` requirements:**
  - Follow the HTML/CSS/JS template in `README.original.md`.
  - Provide 8 input fields for `MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude`.
  - Include buttons for **Use sample values** (populates `[8.3, 25.0, 6.0, 1.0, 1200, 3.0, 34.2, -118.3]`), **Predict** (sends `POST /predict` with `{features: [...]}` and displays the returned prediction), and **Reset**.

## 4. Acceptance Commands and Expected Output
Run these verification checks in `e:\Antigravity-Projects\ml-deployment-lab` using `.venv` (via Flask test client so no orphan server process is left on port 5000):
```powershell
.\.venv\Scripts\python -c "
from app import app
client = app.test_client()

r_health = client.get('/health')
print('GET /health:', r_health.status_code, r_health.get_json())
assert r_health.status_code == 200
assert r_health.get_json()['ok'] is True
assert len(r_health.get_json()['features']) == 8

r_pred = client.post('/predict', json={'features': [8.3, 25.0, 6.0, 1.0, 1200, 3.0, 34.2, -118.3]})
print('POST /predict (valid):', r_pred.status_code, r_pred.get_json())
assert r_pred.status_code == 200
assert abs(r_pred.get_json()['prediction'] - 4.03) < 0.15

r_bad = client.post('/predict', json={'features': [1.0, 2.0, 3.0]})
print('POST /predict (bad length):', r_bad.status_code, r_bad.get_json())
assert r_bad.status_code == 400

r_index = client.get('/')
html = r_index.get_data(as_text=True)
print('GET /:', r_index.status_code, 'len=', len(html))
assert r_index.status_code == 200
for name in ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']:
    assert name in html, f'Missing {name}'
print('ALL CHECKS PASSED')
"
```
Expected output:
- `GET /health: 200 {'features': ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'], 'ok': True}`
- `POST /predict (valid): 200 {'prediction': ~4.03}`
- `POST /predict (bad length): 400 ...`
- `GET /: 200 ...`
- `ALL CHECKS PASSED`

Make sure no background Python/Flask process is left holding port 5000 when you finish.

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G2-report.md` with the following sections:
- **What was done:** Summary of `app.py` and `templates/main.html` implementation.
- **Command outputs:** Exact output from the acceptance test script above.
- **Deviations:** Any differences from `README.original.md` (with reasons).
- **Anything the Elephant should know:** Confirmation that port 5000 is free for Docker in G3.

Append an entry to `handoff/AGENTLOG.md` before finishing.
