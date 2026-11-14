# Task G3 Report: Create `Dockerfile`, Build Image, and Run Container

## What was done
- Created `e:\Antigravity-Projects\ml-deployment-lab\Dockerfile` using base image `python:3.11-slim`, `WORKDIR /app`, `pip install --no-cache-dir -r requirements.txt`, explicit copies of `train_model.py`, `app.py`, and `templates/`, `RUN python train_model.py` (generating `model/model.pkl` inside the image), `EXPOSE 5000`, and `CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]`.
- Started Docker Desktop (which was not running at task start) so the `desktop-linux` engine (`29.9.3`) was available.
- Built Docker image `ds-ml-service:latest` via `docker build -t ds-ml-service .`.
- Started container `ds-ml-service-container` in detached mode on port `5000` (`docker run -d --name ds-ml-service-container -p 5000:5000 ds-ml-service`) and verified it via `docker ps`, `docker logs`, and `curl.exe -s http://127.0.0.1:5000/health`.

## Command outputs

### `docker build -t ds-ml-service .`
```text
#0 building with "desktop-linux" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 313B 0.0s done
#1 DONE 0.1s

#2 [internal] load metadata for docker.io/library/python:3.11-slim
#3 [auth] library/python:pull token for registry-1.docker.io
#3 DONE 0.0s
#2 DONE 5.4s

#4 [internal] load .dockerignore
#4 transferring context: 2B done
#4 DONE 0.1s

#5 [1/7] FROM docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84f7a7b535
#5 resolve docker.io/library/python:3.11-slim@sha256:07d4824036af339fa1b6ef769cc99d9c10a141769538b52b3b597c84f7a7b535 0.1s done
#6 [internal] load build context
#6 transferring context: 8.74kB done
#6 DONE 0.2s
#5 DONE 17.3s

#7 [2/7] WORKDIR /app
#7 DONE 0.4s

#8 [3/7] COPY requirements.txt .
#8 DONE 0.1s

#9 [4/7] RUN pip install --no-cache-dir -r requirements.txt
#9 2.356 Collecting flask==3.1.3 (from -r requirements.txt (line 1))
#9 3.924 Collecting gunicorn==26.2.0 (from -r requirements.txt (line 2))
#9 5.010 Collecting numpy==2.4.6 (from -r requirements.txt (line 3))
#9 5.457 Collecting scikit-learn==1.9.1 (from -r requirements.txt (line 4))
#9 5.706 Collecting joblib==1.6.0 (from -r requirements.txt (line 5))
#9 6.270 Collecting pandas==3.1.1 (from -r requirements.txt (line 6))
...
#9 31.93 Installing collected packages: tzdata, threadpoolctl, numpy, narwhals, markupsafe, itsdangerous, gunicorn, cloudpickle, click, blinker, werkzeug, scipy, python-dateutil, joblib, jinja2, scikit-learn, pandas, flask
#9 47.19 Successfully installed blinker-1.9.0 click-8.5.1 cloudpickle-3.1.2 flask-3.1.3 gunicorn-26.2.0 itsdangerous-2.2.0 jinja2-3.1.6 joblib-1.6.0 markupsafe-3.0.4 narwhals-2.28.0 numpy-2.4.6 pandas-3.1.1 python-dateutil-4.0.0 scikit-learn-1.9.1 scipy-1.17.1 threadpoolctl-3.8.0 tzdata-2026.6 werkzeug-3.1.9
#9 DONE 48.8s

#10 [5/7] COPY train_model.py app.py ./
#10 DONE 0.3s

#11 [6/7] COPY templates/ ./templates/
#11 DONE 0.1s

#12 [7/7] RUN python train_model.py
#12 11.99 บันทึกโมเดลเรียบร้อยที่ model/model.pkl
#12 DONE 12.6s

#13 exporting to image
#13 exporting layers 14.9s done
#13 exporting manifest sha256:879bcef2f4db7bd8c0429a8c6758e0f3e3b4c7ba65787a71203b5315f4c3e12f 0.1s done
#13 exporting config sha256:4c8a31a7276cdaf7a49fa12e6660aa2395935b4af7d8c2149d141f8f8094de66 0.0s done
#13 exporting attestation manifest sha256:886d6a70473836537b00fcb6dcf6bfd01a821b7cfd76fa0ef9c04998e4354141 0.1s done
#13 exporting manifest list sha256:a2955f300a279e82afdf3c08a1c653732533f20ba3626cc224e3f4a4c090e95f 0.0s done
#13 naming to docker.io/library/ds-ml-service:latest 0.0s done
#13 unpacking to docker.io/library/ds-ml-service:latest 8.1s done
#13 DONE 23.5s
```

### `docker run -d --name ds-ml-service-container -p 5000:5000 ds-ml-service`
```text
b153e457758fe37aadb566dd0a6e8145d5c22c1277f69b710522536b55ff0bfe
```

### `docker ps --filter "name=ds-ml-service-container"`
```text
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                         NAMES
b153e457758f   ds-ml-service   "gunicorn -w 2 -b 0.…"   4 seconds ago   Up 3 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   ds-ml-service-container
```

### `docker logs ds-ml-service-container`
```text
[2026-11-14 05:56:04 +0000] [1] [INFO] Starting gunicorn 26.2.0
[2026-11-14 05:56:04 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
[2026-11-14 05:56:04 +0000] [1] [INFO] Using worker: sync
[2026-11-14 05:56:04 +0000] [7] [INFO] Booting worker with pid: 7
[2026-11-14 05:56:04 +0000] [8] [INFO] Booting worker with pid: 8
[2026-11-14 05:56:04 +0000] [1] [INFO] Control socket listening at /root/.gunicorn/gunicorn.ctl
```

### `curl.exe -s http://127.0.0.1:5000/health`
```json
{"features":["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"],"ok":true}
```

## Deviations
- **`requirements.txt`:** No changes needed; all pinned packages installed cleanly on `python:3.11-slim`.
- **`Dockerfile` (`COPY` scope):** `README.original.md` (Section 3.6) uses `COPY . .` (and includes Thai comments). Per Task G3 Section 3, `Dockerfile` instead copies only `train_model.py`, `app.py`, and `templates/` (`COPY train_model.py app.py ./` and `COPY templates/ ./templates/`) so unrelated workspace directories (e.g., `handoff/`, local `.venv/`, or host-side `model/`) are excluded from the image and `model/model.pkl` is guaranteed to be built by `RUN python train_model.py` during the image build.
- **Container run mode:** `README.original.md` (Section 3.7) uses `docker run --rm -p 5000:5000 ds-ml-service`; per Task G3, the container was started detached as `ds-ml-service-container` and left running.

## Anything the Elephant should know
- `ds-ml-service-container` (`b153e457758f`) is running on `http://127.0.0.1:5000` (mapped `0.0.0.0:5000->5000/tcp`) and responding healthy on `/health` for Task G4.
- Note on host daemon lifetime: Docker Desktop was not running when Task G3 started, so it was launched from a daemon background task (`C:\Users\User\AppData\Local\Programs\DockerDesktop\Docker Desktop.exe`) within this Goldfish session. If the agent runner terminates conversation background tasks upon Goldfish exit, Docker Desktop may also stop and need to be running again before Task G4 runs (`ds-ml-service` image is built and `ds-ml-service-container` exists).
