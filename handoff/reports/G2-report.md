# G2 Report — Create `app.py` and `templates/main.html` and Test Locally

## What was done
- Created `app.py` in `e:\Antigravity-Projects\ml-deployment-lab\app.py`:
  - Loads `model/model.pkl` via `joblib.load`.
  - Defines `FEATURES` in the exact required order: `["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]`.
  - Implements `GET /health` returning HTTP 200 JSON `{"ok": true, "features": FEATURES}`.
  - Implements `POST /predict` validating a JSON object containing `"features"` as a list of 8 finite numeric values convertible to `float` (rejecting non-dict payloads, non-list/wrong-length `features`, booleans, non-numeric entries, or non-finite values with HTTP 400 JSON error) and returning HTTP 200 JSON `{"prediction": <float>}`.
  - Implements `GET /` (and `POST /` form fallback) rendering `templates/main.html`.
- Created `templates/main.html` in `e:\Antigravity-Projects\ml-deployment-lab\templates\main.html` following `README.original.md`:
  - Provides 8 labeled numeric input fields for `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, and `Longitude`.
  - Includes **Use sample values** (populates `[8.3, 25, 6.0, 1.0, 1200, 3.0, 34.2, -118.3]`), **Predict** (submits `POST /predict` with `{ features: vals }` and renders the formatted prediction or error), and **Reset** buttons.
- Ran the G2 acceptance test script via `.venv` using Flask's `test_client()`, plus extra edge-case validation checks and a port 5000 check.

## Command outputs
Acceptance command output:
```text
GET /health: 200 {'features': ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'], 'ok': True}
POST /predict (valid): 200 {'prediction': 4.029472199999998}
POST /predict (bad length): 400 {'error': "Expected 8 features: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']"}
GET /: 200 len= 5867
ALL CHECKS PASSED
```

Additional validation and port check output:
```text
EDGE CASES PASSED
```
(`netstat -ano | Select-String ":5000 "` returned empty output, confirming no listener on port 5000.)

## Deviations
- In `app.py` `POST /predict`, added explicit input validation beyond the minimal snippet in `README.original.md`: verifies that the parsed JSON body is a `dict`, `features` is a `list` of length 8, no elements are `bool`, all elements convert cleanly to `float` (returning HTTP 400 on `TypeError`/`ValueError` instead of an unhandled 500), and all values are finite (`np.isfinite`), as required by task G2's spec ("Return HTTP 400 with an error JSON if `features` is missing, not a list of length 8, or cannot be converted to floats"). Also cast the returned prediction explicitly with `float(...)`.
- `templates/main.html` matches `README.original.md` directly with no deviations.

## Anything the Elephant should know
- Port 5000 is completely free (all tests ran in-process via `app.test_client()`, and `netstat -ano` confirmed no process is listening on port 5000), so Docker in G3 can bind port 5000 without conflict.
