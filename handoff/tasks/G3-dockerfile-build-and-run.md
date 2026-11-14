# Task G3: Create `Dockerfile`, Build Image, and Run Container

## 1. Context
You are a Goldfish agent working in `e:\Antigravity-Projects\ml-deployment-lab`.
Your task is to create `Dockerfile`, build the Docker image `ds-ml-service`, and run a container exposing port 5000.

## 2. Exact Files to Create or Edit
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\Dockerfile`
- **Edit (only if needed for Docker build compatibility):** `e:\Antigravity-Projects\ml-deployment-lab\requirements.txt`
- **Create:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G3-report.md`
- **Append to:** `e:\Antigravity-Projects\ml-deployment-lab\handoff\AGENTLOG.md`

## 3. Spec Source & Explicit Requirements
- Read the `Dockerfile` and Docker build/run sections in `e:\Antigravity-Projects\ml-deployment-lab\README.original.md`.
- **`Dockerfile` requirements:**
  - Base image: `python:3.11-slim`
  - Set `WORKDIR /app`
  - Copy `requirements.txt` and run `pip install --no-cache-dir -r requirements.txt`
  - Copy application code (`train_model.py`, `app.py`, `templates/`) into `/app`
  - Run `python train_model.py` during the image build so `model/model.pkl` is generated inside the image
  - `EXPOSE 5000`
  - Start command: `gunicorn -w 2 -b 0.0.0.0:5000 app:app`
- Build the image with tag `ds-ml-service`.
- If any package version in `requirements.txt` fails to install on `python:3.11-slim` during `docker build`, adjust `requirements.txt`, rebuild, and record the exact version change and reason in your report and `AGENTLOG.md`.
- Run the container in detached mode on port 5000 (`--name ds-ml-service-container -p 5000:5000`) and leave it running for Task G4.

## 4. Acceptance Commands and Expected Output
Run these commands in `e:\Antigravity-Projects\ml-deployment-lab`:
```powershell
docker rm -f ds-ml-service-container 2>$null
docker build -t ds-ml-service .
# Expected: Image builds successfully; train_model.py executes during build and creates model/model.pkl

docker run -d --name ds-ml-service-container -p 5000:5000 ds-ml-service
# Expected: Container ID printed

Start-Sleep -Seconds 3
docker ps --filter "name=ds-ml-service-container"
# Expected: Status "Up ..." with ports 0.0.0.0:5000->5000/tcp

docker logs ds-ml-service-container
# Expected: Gunicorn starting 2 workers listening on 0.0.0.0:5000

curl.exe -s http://127.0.0.1:5000/health
# Expected: {"features":["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"],"ok":true}
```

## 5. Report Back
Write your report to `e:\Antigravity-Projects\ml-deployment-lab\handoff\reports\G3-report.md` with the following sections:
- **What was done:** `Dockerfile` created, `ds-ml-service` image built, `ds-ml-service-container` started on port 5000.
- **Command outputs:** Outputs of `docker build`, `docker ps`, `docker logs`, and `curl.exe -s http://127.0.0.1:5000/health`.
- **Deviations:** Any adjustments to `requirements.txt` or `Dockerfile` compared to `README.original.md`, with reasons.
- **Anything the Elephant should know:** Confirm that `ds-ml-service-container` is left running on `http://127.0.0.1:5000` for Task G4.

Append an entry to `handoff/AGENTLOG.md` before finishing.
