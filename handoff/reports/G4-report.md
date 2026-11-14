# Goldfish G4 Report — Verify Containerized API & Web UI and Capture Screenshot

## What was done
1. Read `handoff/tasks/G4-verify-api-ui-and-screenshot.md` and sections 3.7 and 4 of `README.original.md`.
2. Confirmed that the Docker container `ds-ml-service-container` (`b153e457758f`, image `ds-ml-service`) was already running and mapped to `0.0.0.0:5000->5000/tcp`.
3. Verified all API endpoints against `http://127.0.0.1:5000` using `curl.exe`:
   - `GET /health` returned HTTP 200 with `ok: true` and the 8 expected `features`.
   - `POST /predict` with the 8-feature sample `[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]` returned HTTP 200 with `{"prediction":4.029472199999998}`.
   - `POST /predict` with the invalid 2-feature payload `[8.3,25.0]` returned `HTTP/1.1 400 BAD REQUEST` and error JSON.
4. Opened `http://127.0.0.1:5000/` in the built-in browser agent, clicked **Use sample values** to populate all 8 input fields, clicked **Predict**, waited for `#output` to render, and captured the screenshot.
5. Copied the captured browser screenshot to `e:\Antigravity-Projects\ml-deployment-lab\screenshot.png` and visually inspected it:
   - Title `California Housing — ML Predictor` is visible.
   - All 8 sample input values (`8.3`, `25`, `6`, `1`, `1200`, `3`, `34.2`, `-118.3`) are populated in the form.
   - The prediction result box displays `Prediction: 4.029` and `Inputs: [8.3, 25, 6, 1, 1200, 3, 34.2, -118.3]`.

## Command outputs

### Container check
```powershell
docker ps -a --filter "ancestor=ds-ml-service" --format "{{.ID}} {{.Names}} {{.Status}} {{.Ports}}"
```
Output:
```text
b153e457758f ds-ml-service-container Up 15 minutes 0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp
```

### `GET /health`
```powershell
curl.exe -s http://127.0.0.1:5000/health
```
Output:
```json
{"features":["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"],"ok":true}
```

### `POST /predict` (valid, HTTP 200)
```powershell
curl.exe -s -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{\"features\":[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]}'
```
Output:
```json
{"prediction":4.029472199999998}
```

### `POST /predict` (invalid feature length, HTTP 400)
```powershell
curl.exe -s -i -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{\"features\":[8.3,25.0]}'
```
Output:
```http
HTTP/1.1 400 BAD REQUEST
Server: gunicorn
Date: Sat, 14 Nov 2026 06:11:55 GMT
Connection: close
Content-Type: application/json
Content-Length: 132

{"error":"Expected 8 features: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']"}
```

### `screenshot.png` verification
```powershell
Test-Path .\screenshot.png
(Get-Item .\screenshot.png).Length
(Get-Item .\screenshot.png).Length -gt 5000
```
Output:
```text
True
125931
True
```

## Deviations
- In PowerShell, passing `-d "{\"features\":...}"` with outer double quotes caused PowerShell to strip the backslashes/quotes before `curl.exe` received the argument (yielding `{"error":"Expected 8 features: ..."}` due to unquoted JSON key `features`). Wrapping the payload in single quotes (`'{\"features\":...}'`) passed valid JSON to `curl.exe` as expected.
- Used the built-in browser subagent (`browser`) to interact with `http://127.0.0.1:5000/` and capture the screenshot, then copied the resulting PNG (`final_step_4.png`) to `screenshot.png`.

## Anything the Elephant should know
- **Exact prediction number shown in the UI screenshot:** `4.029` (formatted to 3 decimal places by `y.toFixed(3)` in `templates/main.html`; raw API value is `4.029472199999998`).
- **Container state:** `ds-ml-service-container` (`b153e457758f`) was **left running** on `http://127.0.0.1:5000`.
