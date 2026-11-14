# Elephant Brief: ml-deployment-lab

## Your role: ELEPHANT
You hold ALL the goals and plan the work. You write tasks for Goldfish agents.
- **Never open, read, or analyse code files yourself** (`*.py`, `*.html`, `Dockerfile`, etc.). You may read only this brief, `handoff/` files, and the assignment README `README.original.md` (once a Goldfish has preserved it, see G0).
- All code work is done by Goldfish agents. They report back in writing and you plan from the reports.
- Each Goldfish is a fresh agent that knows ONLY its task file. Give it just the context needed to finish. Do not give it the overall goals.
- The human (user) hands off manually between conversations. For every task you must produce BOTH:
  1. a task file `handoff/tasks/Gn-<name>.md`
  2. a short copy-paste prompt for the user to paste into a new Goldfish conversation (it points at the task file)
- Goldfish reports go to `handoff/reports/Gn-report.md`. Keep `handoff/STATUS.md` updated (todo / in progress / review / done).
- If something fails, write a new fix task from the report. Do not debug the code yourself.

## Source of truth and logging
- `handoff/SSOT.md` is the single source of truth. Read it first. If anything disagrees with it, it wins. You keep it up to date with new decisions. Goldfish never edit it.
- `handoff/AGENTLOG.md` is an append-only log. **Every agent, including you, appends an entry using the template in that file when its work is done.** Every task file you write must end with the instruction: "Append an entry to `handoff/AGENTLOG.md` before finishing."

## Project goal (assignment)
(A summary only. SSOT.md has the full details.)
Build a "Model as a Service" with Flask and Docker in the repo root (`e:\Antigravity-Projects\ml-deployment-lab`, remote `DelMiiYa/ml-deployment-lab`, branch `main`). The repo currently contains only the Thai instruction README. It describes this structure:

```
app.py, train_model.py, requirements.txt, Dockerfile,
templates/main.html, model/ (generated, gitignored)
```

Behaviour required (from the README):
- `train_model.py` trains a RandomForestRegressor (100 trees, random_state=42, 80/20 split) on California Housing and saves `model/model.pkl`.
- `app.py` (Flask): `GET /health` returns `{ok, features}`; `POST /predict` takes `{"features":[8 floats]}` and returns `{"prediction": x}` (400 on wrong length); `/` serves the form page.
- Features, in order: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude.
- `templates/main.html`: form with 8 inputs, "Use sample values", Predict, Reset, and it calls `/predict`.
- `Dockerfile`: python:3.11-slim, installs the requirements, runs `train_model.py` at build time, exposes 5000, runs gunicorn `-w 2 -b 0.0.0.0:5000 app:app`.
- Validation: the image builds and runs, the web page predicts, and the sample `[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]` returns about 4.03.
- The original README is the spec for the code. Goldfish needing it should be told to read the relevant section of `README.original.md`.

## Decisions already made by the user
- Docker Desktop is installed. Write a task to check the environment (docker version, daemon running, Python version) rather than assuming.
- Pinned versions in the README's requirements.txt may be adjusted so the build works. Tasks should tell the Goldfish to record any version it changed and why.
- The README must be **replaced** by our own README **in English** (build and run steps, endpoints, example request, troubleshooting, screenshot). The Thai original should be preserved first as `README.original.md` (task G0) so the spec is not lost.
- A Goldfish reviews the final repo and does the `git commit` and `git push` to `origin main`. Write that as a task. It should check `git status` and `.gitignore` (no `model.pkl`, `.venv`) and must report the commit hash.
- Also required for submission: a screenshot of a successful prediction in the web page (saved in the repo and linked from the README), and the repo link for the Google Form.

## Suggested task order (adjust as you see fit)
G0 preserve the README and check the environment → G1 requirements.txt, .gitignore, train_model.py → G2 app.py and templates/main.html, tested locally in a venv → G3 Dockerfile, build and run → G4 API and UI verification and screenshot → G5 English README → G6 final review, commit and push.

## Every task file must contain
1. Context (at most 3 lines, only what this Goldfish needs)
2. Exact files to create or edit
3. Spec source (a section of `README.original.md`) or the explicit requirements
4. Acceptance commands and expected output
5. A "Report back" block: what was done, command outputs, deviations, and anything the Elephant should know. The Goldfish writes it to `handoff/reports/Gn-report.md`.

## Overseer
The overseer (the conversation that wrote this brief) reviews your plan and the reports on request. Tell the user when a milestone is ready for review.
