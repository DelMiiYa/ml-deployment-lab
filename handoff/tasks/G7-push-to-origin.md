# Task G7: Push to `origin main` (run ONLY after the human approves G6)

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
A local commit already exists. Your only job is to push it to GitHub and report the result.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G7-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`
- Do not edit any other file. The report and log are updated after the push (a small follow-up commit is NOT required).

## 3. Explicit Requirements
- Check `git status -sb` shows the branch ahead of `origin/main` with a clean tree. If not, STOP and report. Do not fix anything.
- Run `git push origin main`. Never force-push. If the push is rejected, STOP and report the exact message.

## 4. Acceptance Commands and Expected Output
```powershell
git status -sb
# Expected: ## main...origin/main [ahead 1]
git push origin main
# Expected: main -> main succeeds
git status -sb
# Expected: ## main...origin/main
git rev-parse HEAD
git ls-remote origin main
# Expected: both show the same SHA
```

## 5. Report Back
Write your report to `handoff/reports/G7-report.md`: the command outputs, the final commit hash, and the repo URL `https://github.com/DelMiiYa/ml-deployment-lab`. Append an entry to `handoff/AGENTLOG.md`.
