# Task Status (ml-deployment-lab)

_Last updated: 2026-11-10 by Elephant_

Allowed states: `todo` | `in progress` | `review` | `done`

| Task ID | Name | Task File | Report File | Status | Notes |
|---|---|---|---|---|---|
| **G0** | Preserve README & Check Environment | `handoff/tasks/G0-preserve-readme-and-check-env.md` | `handoff/reports/G0-report.md` | `todo` | Copies Thai `README.md` to `README.original.md`; checks Python, Docker, Git |
| **G1** | Requirements, Gitignore & Train Model | `handoff/tasks/G1-requirements-gitignore-train.md` | `handoff/reports/G1-report.md` | `todo` | Creates `.gitignore`, `requirements.txt`, `train_model.py`; trains `model/model.pkl` in `.venv` |
| **G2** | Flask App & Web UI Template | `handoff/tasks/G2-flask-app-and-template.md` | `handoff/reports/G2-report.md` | `todo` | Creates `app.py` and `templates/main.html`; tests `/`, `/health`, `/predict` locally |
| **G3** | Dockerfile, Image Build & Container Run | `handoff/tasks/G3-dockerfile-build-and-run.md` | `handoff/reports/G3-report.md` | `todo` | Creates `Dockerfile`, builds `ds-ml-service`, runs container on port 5000 |
| **G4** | API/UI Verification & Screenshot | `handoff/tasks/G4-verify-api-ui-and-screenshot.md` | `handoff/reports/G4-report.md` | `todo` | Verifies containerized API & web UI; saves `screenshot.png` showing ~4.03 prediction |
| **G5** | English README | `handoff/tasks/G5-english-readme.md` | `handoff/reports/G5-report.md` | `todo` | Replaces `README.md` with English documentation linking `screenshot.png` |
| **G6** | Final Review & LOCAL Commit (no push) | `handoff/tasks/G6-final-review-and-local-commit.md` | `handoff/reports/G6-report.md` | `todo` | Audits files and `.gitignore` (handoff/ committed, README.original.md ignored), commits locally only |
| **G7** | Push to origin | `handoff/tasks/G7-push-to-origin.md` | `handoff/reports/G7-report.md` | `todo` | Run ONLY after the human approves the G6 report; plain `git push origin main`, no force |

## Milestones for Overseer Review
1. **After G0**: Confirm environment readiness and `README.original.md` preservation (or right now to review the initial task plan G0–G6).
2. **After G4**: Confirm Docker container, API responses, and `screenshot.png` before final documentation and push.
3. **After G6 (push gate)**: Human/Overseer reviews the local commit contents before G7 is run.
4. **After G7**: Confirm the commit hash on `origin main` for Google Form submission.
