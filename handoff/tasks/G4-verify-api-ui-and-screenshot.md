# Task G4: Verify Containerized API & Web UI and Capture Screenshot

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to verify all API endpoints and the web UI served by the running `ds-ml-service` Docker container on `http://127.0.0.1:5000`, and save a screenshot of a successful prediction in the web UI to `screenshot.png`.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\screenshot.png`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G4-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Read the testing and validation sections in `e:\Antigravity-Projects\ml-deployment-lab\README.original.md`.
- Ensure the Docker container from `ds-ml-service` is running on port 5000 (if not running, start it with `docker run -d --name ds-ml-service-container -p 5000:5000 ds-ml-service`).
- Verify API endpoints against `http://127.0.0.1:5000`:
  1. `GET /health` → HTTP 200, `{"ok": true, "features": ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]}`
  2. `POST /predict` with sample `{"features":[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]}` → HTTP 200, `{"prediction": ~4.03}`
  3. `POST /predict` with wrong feature length `{"features":[8.3,25.0]}` → HTTP 400
- Open `http://127.0.0.1:5000/` in a browser (or automate a headless browser via Playwright/Selenium/Edge/Chrome), click **Use sample values**, click **Predict**, wait until the prediction (~4.03) is rendered on the page, and save a clear screenshot to `e:\Antigravity-Projects\ml-deployment-lab\screenshot.png`.
- **If no browser or headless-automation tool is available, or the screenshot cannot be captured:** STOP the screenshot step. Do not fake or mock an image. Finish the API checks, write the report stating exactly what is missing, and tell the human to take the screenshot manually (open `http://127.0.0.1:5000/`, click **Use sample values**, click **Predict**, save it as `screenshot.png` in the repo root).
- Inspect `e:\Antigravity-Projects\ml-deployment-lab\screenshot.png` to confirm the 8 sample input values and the prediction result (~4.03) are visibly displayed in the image.

## 4. Acceptance Commands and Expected Output
Run these commands in `e:\Antigravity-Projects\ml-deployment-lab`:
```powershell
curl.exe -s http://127.0.0.1:5000/health
# Expected: {"features":["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"],"ok":true}

curl.exe -s -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\":[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]}"
# Expected: {"prediction":4.03...}

curl.exe -s -i -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\":[8.3,25.0]}"
# Expected: HTTP/1.1 400 BAD REQUEST with error JSON

Test-Path .\screenshot.png
# Expected: True
(Get-Item .\screenshot.png).Length -gt 5000
# Expected: True
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G4-report.md` with the following sections:
- **What was done:** API tests executed, web UI interaction performed, and `screenshot.png` captured and visually verified.
- **Command outputs:** Exact outputs of the `curl.exe` commands for `/health`, `/predict` (200), `/predict` (400), and file size/verification of `screenshot.png`.
- **Deviations:** Any differences or issues encountered.
- **Anything the Elephant should know:** Exact prediction number shown in the UI screenshot and whether the container was stopped or left running.

Append an entry to `handoff/AGENTLOG.md` before finishing.
