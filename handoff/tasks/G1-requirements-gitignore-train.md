# Task G1: Create `.gitignore`, `requirements.txt`, and `train_model.py`

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to create `.gitignore`, `requirements.txt`, and `train_model.py` based on `README.original.md`, install dependencies in a local `.venv`, and train the model to generate `model/model.pkl`.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\.gitignore`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\requirements.txt`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\train_model.py`
- **Generated (gitignored):** `e:\Antigravity-Projects\ml-deployment-lab\.venv\` and `e:\Antigravity-Projects\ml-deployment-lab\model\model.pkl`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G1-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Read the sections in `e:\Antigravity-Projects\ml-deployment-lab\README.original.md` covering project structure, `requirements.txt`, and `train_model.py`.
- **`.gitignore`:** Must ignore at least:
  ```gitignore
  model/
  .venv/
  __pycache__/
  *.pyc
  ```
- **`requirements.txt`:** Include `flask`, `gunicorn`, `numpy`, `scikit-learn`, `joblib`, and `pandas` as specified in `README.original.md`.
  - If any pinned version in `README.original.md` fails to install or has compatibility issues (locally or with `python:3.11-slim`), adjust the version so installation succeeds cleanly. **You must record every version change and the reason in your report and `AGENTLOG.md`.**
- **`train_model.py`:** Follow the code/specification in `README.original.md`:
  - Load the California Housing dataset (`fetch_california_housing`).
  - Feature order: `MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude`.
  - Split 80/20 (`test_size=0.2, random_state=42`).
  - Train `RandomForestRegressor(n_estimators=100, random_state=42)`.
  - Save the trained model to `model/model.pkl` using `joblib` (creating the `model/` directory if it does not exist).

## 4. Acceptance Commands and Expected Output
Run these commands in `e:\Antigravity-Projects\ml-deployment-lab`:
```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -r requirements.txt
# Expected: All packages install cleanly with exit code 0

.\.venv\Scripts\python train_model.py
# Expected: Trains model and saves model/model.pkl without errors

Test-Path .\model\model.pkl
# Expected: True

.\.venv\Scripts\python -c "import joblib, numpy as np; m = joblib.load('model/model.pkl'); pred = float(m.predict(np.array([[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]]))[0]); print('Sample prediction:', round(pred, 4))"
# Expected: Sample prediction: ~4.03 (last decimals may vary slightly by machine/scikit-learn version)
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G1-report.md` with the following sections:
- **What was done:** Files created, virtual environment setup, and model training summary.
- **Command outputs:** Outputs from `pip install -r requirements.txt`, `python train_model.py`, `Test-Path .\model\model.pkl`, and the sample prediction command.
- **Deviations:** List any package versions in `requirements.txt` that were changed from `README.original.md` (old version → new version, and why).
- **Anything the Elephant should know:** Exact installed versions (`pip freeze` for the 6 required packages) and sample prediction value.

Append an entry to `handoff/AGENTLOG.md` before finishing.
