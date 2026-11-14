# Task G0: Preserve Original README and Check Environment

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to preserve the existing Thai assignment `README.md` as `README.original.md` and check the local Python, Git, and Docker environment.
Do not write any application code or modify `README.md` in this task.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\README.original.md` (exact copy of `e:\Antigravity-Projects\ml-deployment-lab\README.md`)
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G0-report.md` (create the `handoff\reports\` folder first if it does not exist)
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Copy `README.md` to `README.original.md` with identical UTF-8 content so the original Thai specification is safely preserved.
- Inspect `README.original.md` and list its markdown section headings in your report so later tasks can reference them.
- Verify the environment by running commands to check:
  1. Python version (`python --version`)
  2. Docker CLI version (`docker --version`)
  3. Docker daemon status (`docker info`)
  4. Git repository status, branch, and remote (`git status`, `git branch`, `git remote -v`)
- Also note what package versions are listed in the `requirements.txt` section of `README.original.md` in your report.

## 4. Acceptance Commands and Expected Output
Run these commands in `e:\Antigravity-Projects\ml-deployment-lab`:
```powershell
Copy-Item -Path .\README.md -Destination .\README.original.md -Force
Test-Path .\README.original.md
# Expected: True

(Get-FileHash .\README.md).Hash -eq (Get-FileHash .\README.original.md).Hash
# Expected: True

python --version
# Expected: Python 3.x.x

docker --version
# Expected: Docker version 2x.x.x ...

docker info
# Expected: Server information confirming the Docker daemon is running (if it errors, report the exact message)

git status -sb
git remote -v
# Expected: ## main...origin/main and origin https://github.com/DelMiiYa/ml-deployment-lab
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G0-report.md` with the following sections:
- **What was done:** Confirmation that `README.original.md` was created and matches `README.md`.
- **Command outputs:** Exact outputs of the hash comparison, `python --version`, `docker --version`, `docker info` (server version/running state), `git status -sb`, `git remote -v`, the list of section headings in `README.original.md`, and the contents of the `requirements.txt` block in `README.original.md`.
- **Deviations:** Any environment issues (e.g., if Docker Desktop daemon is not running or Python is missing).
- **Anything the Elephant should know:** Any details from `README.original.md` that affect subsequent tasks.

Append an entry to `handoff/AGENTLOG.md` before finishing.
