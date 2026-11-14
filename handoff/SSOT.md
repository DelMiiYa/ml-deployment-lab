# SSOT: Single Source of Truth (ml-deployment-lab)

> If any other file (task, report, README, chat) disagrees with this file, **this file wins**.
> Only the Elephant or the Overseer edit this file. Goldfish agents read it only if their task file tells them to, and they never edit it. They record what they did in `AGENTLOG.md`.

_Last updated: 2026-11-10 by Elephant_

## 1. Goal
Complete the "Model as a Service with Flask and Docker" assignment: a containerised Flask API and web UI serving a California Housing RandomForest model, published on GitHub with an English README and a screenshot.

## 2. Locations
- Local repo: `e:\Antigravity-Projects\ml-deployment-lab`
- Remote: `https://github.com/DelMiiYa/ml-deployment-lab` (branch `main`)
- Original spec (Thai README): preserved as `README.original.md` by task G0.

## 3. Required deliverables
| Item | Requirement |
|---|---|
| `train_model.py` | RandomForestRegressor(n_estimators=100, random_state=42), 80/20 split, random_state=42, saves `model/model.pkl` |
| `app.py` | `GET /health` → `{ok, features}`; `POST /predict` with `{"features":[8 floats]}` → `{"prediction": x}`, 400 on wrong length; `/` serves the form |
| `templates/main.html` | 8 inputs, "Use sample values", Predict, Reset; calls `/predict` |
| `requirements.txt` | flask, gunicorn, numpy, scikit-learn, joblib, pandas (versions adjustable, see §5) |
| `Dockerfile` | python:3.11-slim; install requirements; run `train_model.py` at build; EXPOSE 5000; gunicorn `-w 2 -b 0.0.0.0:5000 app:app` |
| `.gitignore` | at least `model/`, `.venv/`, `__pycache__/` |
| `README.md` | **English**, replaces the Thai one: overview, structure, build/run, endpoints, example request, troubleshooting, screenshot |
| Screenshot | successful prediction in the web UI, saved as `screenshot.png` in the repo root and linked from the README |
| Submission | repo pushed to `origin main`; the link goes to the Google Form (https://forms.gle/D8UCryawXbEn4FSe7) by the user |

## 4. API contract
- Feature order: `MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude`
- Sample input: `{"features":[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]}` → prediction ≈ 4.03 (last decimals may differ by machine)
- Docker image name: `ds-ml-service`; port 5000; URLs `http://127.0.0.1:5000/` and `/health`

## 5. Decisions (made by the user)
1. Workflow: Elephant/Goldfish. The Elephant plans and writes tasks and never reads code. Goldfish agents do the work and report back. The Overseer reviews on request.
2. Handoff is manual by the user: task file in `handoff/tasks/` plus a copy-paste prompt.
3. Pinned versions in the original README may be adjusted so the build works. Each change must be logged in `AGENTLOG.md` and the task report.
4. Docker Desktop is installed, but a task must still verify the environment.
5. README is replaced by our own English version.
6. A Goldfish reviews and makes a LOCAL commit (G6) and stops. After a human approves the report, another Goldfish pushes (G7). No push without that approval.
7. If the screenshot cannot be automated (G4), the Goldfish stops and the human captures it manually; no faked images.

## 6. File map (coordination)
| File | Purpose | Who writes |
|---|---|---|
| `handoff/SSOT.md` | this file, the truth | Elephant, Overseer |
| `handoff/ELEPHANT_BRIEF.md` | the Elephant's instructions | Overseer |
| `handoff/STATUS.md` | task states (todo / in progress / review / done) | Elephant |
| `handoff/tasks/Gn-*.md` | one task per Goldfish | Elephant |
| `handoff/reports/Gn-report.md` | Goldfish result report | Goldfish |
| `handoff/AGENTLOG.md` | append-only log of what every agent did | **all agents** |


## 7. Open items
- Task files `G0`–`G7` have been written to `handoff/tasks/` (G6 revised to a local commit, G7 added for the push).
- Decided by the user (13:39): `handoff/` (including `AGENTLOG.md`) IS committed and pushed. `README.original.md` stays local and gitignored.
