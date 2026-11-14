# Task G6: Final Repository Review and LOCAL Commit (do NOT push)

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to audit the repository deliverables and `.gitignore`, verify that no generated artifacts are tracked, and create a **local commit only**. **Do NOT run `git push`.** A human reviews your report first, and a separate task (G7) pushes.

## 2. Exact Files to Create or Edit
- **Edit:** `e:\Antigravity-Projects\ml-deployment-lab\.gitignore` (ensure `model/`, `.venv/`, `__pycache__/`, `*.pyc` and `README.original.md` are ignored. **`handoff/` must NOT be ignored**: it is committed as evidence of the workflow)
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G6-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Stop and remove any running test container (`docker rm -f ds-ml-service-container 2>$null`).
- Verify all required files exist: `.gitignore`, `README.md` (English), `requirements.txt`, `train_model.py`, `app.py`, `templates/main.html`, `Dockerfile`, `screenshot.png`, and the `handoff/` folder.
- Do NOT delete `README.original.md` from disk (it stays local, ignored).
- Write your G6 report and the AGENTLOG entry BEFORE committing, so they are included in the commit.
- Stage: `.gitignore README.md requirements.txt train_model.py app.py templates/main.html Dockerfile screenshot.png handoff/`
- Check that neither `model/model.pkl`, `.venv/` nor `README.original.md` is staged.
- Commit locally with message `Implement Flask & Docker California Housing ML service`.
- **Do not push.** Stop after the commit and report.

## 4. Acceptance Commands and Expected Output
```powershell
docker rm -f ds-ml-service-container 2>$null

git add .gitignore README.md requirements.txt train_model.py app.py templates/main.html Dockerfile screenshot.png handoff/
git status -sb
# Expected: only the files above staged; no model/, .venv/, __pycache__/, README.original.md

git diff --cached --stat
git commit -m "Implement Flask & Docker California Housing ML service"
git rev-parse HEAD
git status -sb
# Expected: clean tree; branch is ahead of origin/main by 1 commit
git log --oneline -3
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G6-report.md` with:
- **What was done:** the audit and the local commit.
- **Command outputs:** `git status -sb` (before and after the commit), `git diff --cached --stat`, `git log --oneline -3`, `git rev-parse HEAD`.
- **Deviations:** any issues.
- **Anything the Elephant should know:** the local commit hash and the exact list of committed files. State clearly that the push has NOT been done.

Append an entry to `handoff/AGENTLOG.md` before committing.
