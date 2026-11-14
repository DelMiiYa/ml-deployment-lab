# Goldfish G5 Report — Replace `README.md` with English Documentation

## What was done
Replaced `README.md` with a complete English README while leaving `README.original.md` untouched. Based on `README.original.md` and `requirements.txt`, the new `README.md` includes:
1. **Overview:** Model as a Service (MaaS) built with Flask, Gunicorn, and Docker serving a California Housing `RandomForestRegressor` (`n_estimators=100`, `random_state=42`, 80/20 split), along with the pinned package versions from `requirements.txt`.
2. **Project Structure:** Directory tree showing `app.py`, `train_model.py`, `requirements.txt`, `Dockerfile`, `templates/main.html`, `model/` (gitignored), and `screenshot.png`.
3. **Build and Run with Docker:** `docker build -t ds-ml-service .`, `docker run -p 5000:5000 ds-ml-service` (with optional `--rm`), and access URLs (`http://127.0.0.1:5000/` and `http://127.0.0.1:5000/health`).
4. **Local Setup (Virtual Environment):** Commands for creating and activating `.venv`, installing `requirements.txt`, training with `python train_model.py`, and running `python app.py`.
5. **API Endpoints & Example Requests:** Exact 8-feature order (`MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`), `GET /`, `GET /health`, and `POST /predict` (including HTTP 400 validation behavior and `curl`, `curl.exe`, and PowerShell `Invoke-RestMethod` examples).
6. **Web UI Screenshot:** Embedded `![Web UI Prediction Screenshot](screenshot.png)`.
7. **Troubleshooting:** Guidance for port `5000` already in use, Docker daemon not running (and disk space / `read-only file system`), `400 Bad Request` on invalid/wrong-length `features`, missing `model/model.pkl` when running locally without `train_model.py`, plus `TemplateNotFound: main.html` and `gunicorn: not found`.

## Command outputs
Ran in `e:\Antigravity-Projects\ml-deployment-lab`:

```powershell
> Test-Path .\README.md
True

> Test-Path .\README.original.md
True

> Select-String -Path .\README.md -Pattern "screenshot.png"

README.md:30:└── screenshot.png
README.md:193:![Web UI Prediction Screenshot](screenshot.png)

> Select-String -Path .\README.md -Pattern "[\u0E00-\u0E7F]"
(no output — 0 Thai characters)

> git diff --name-only README.original.md
(no output — README.original.md untouched)
```

## Deviations
None.

## Anything the Elephant should know
`README.md` is complete, verified with all acceptance checks, and ready for the final review and local commit in G6. `README.original.md` remains untouched.
