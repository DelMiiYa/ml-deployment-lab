# Task G5: Replace `README.md` with English Documentation

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to replace `README.md` with a clear, complete **English** README covering the project overview, structure, build/run steps, API endpoints, example requests, troubleshooting, and embedded screenshot (`screenshot.png`).

## 2. Exact Files to Create or Edit
- **Edit (overwrite):** `e:\Antigravity-Projects\ml-deployment-lab\README.md`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G5-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Refer to `e:\Antigravity-Projects\ml-deployment-lab\README.original.md` for the original assignment details and `requirements.txt` for the actual package versions used.
- Keep `README.original.md` untouched.
- Write `README.md` entirely in **English** (no Thai text) and include all of the following sections:
  1. **Overview:** Model as a Service (MaaS) with Flask, Gunicorn, and Docker serving a California Housing `RandomForestRegressor` model (`n_estimators=100, random_state=42`, 80/20 split).
  2. **Project Structure:**
     ```text
     ml-deployment-lab/
     ├── app.py
     ├── train_model.py
     ├── requirements.txt
     ├── Dockerfile
     ├── templates/
     │   └── main.html
     ├── model/              # generated at build/train time (gitignored)
     └── screenshot.png
     ```
  3. **Build and Run with Docker:**
     - Build image: `docker build -t ds-ml-service .`
     - Run container: `docker run -p 5000:5000 ds-ml-service`
     - Access Web UI: `http://127.0.0.1:5000/`
     - Access Health Check: `http://127.0.0.1:5000/health`
  4. **Local Setup (Virtual Environment):**
     - Commands to create `.venv`, install `requirements.txt`, run `python train_model.py`, and start `python app.py`.
  5. **API Endpoints & Example Requests:**
     - Feature order (`MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`).
     - `GET /`: serves the HTML prediction form.
     - `GET /health`: returns `{"ok": true, "features": [...]}`.
     - `POST /predict`: takes `{"features": [8.3, 25.0, 6.0, 1.0, 1200, 3.0, 34.2, -118.3]}` and returns `{"prediction": ~4.03}` (returns HTTP 400 if `features` does not have 8 numeric items). Include both `curl` and PowerShell `Invoke-RestMethod` examples.
  6. **Web UI Screenshot:**
     - Embed the screenshot using `![Web UI Prediction Screenshot](screenshot.png)`.
  7. **Troubleshooting:**
     - Port 5000 already in use, Docker daemon not running, 400 Bad Request on wrong feature length, `model/model.pkl` missing when running locally without running `train_model.py` first.

## 4. Acceptance Commands and Expected Output
Run these checks in `e:\Antigravity-Projects\ml-deployment-lab`:
```powershell
Test-Path .\README.md
# Expected: True

Test-Path .\README.original.md
# Expected: True

Select-String -Path .\README.md -Pattern "screenshot.png"
# Expected: Matches the markdown image link ![...](screenshot.png)

Select-String -Path .\README.md -Pattern "[\u0E00-\u0E7F]"
# Expected: No output (no Thai characters in README.md)
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G5-report.md` with the following sections:
- **What was done:** Summary of sections written in the new English `README.md`.
- **Command outputs:** Outputs from the acceptance commands above.
- **Deviations:** None expected; note any if applicable.
- **Anything the Elephant should know:** Confirmation that `README.md` is ready for final commit.

Append an entry to `handoff/AGENTLOG.md` before finishing.
