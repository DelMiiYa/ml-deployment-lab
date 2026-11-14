# Task G1 Report: Create `.gitignore`, `requirements.txt`, and `train_model.py`

## 1. What Was Done
- **Created `.gitignore`:** Configured to ignore `model/`, `.venv/`, `__pycache__/`, `*.pyc`, and `README.original.md` (as per SSOT decision).
- **Created `requirements.txt`:** Pinned the exact 6 dependencies specified in `README.original.md` (`flask==3.1.3`, `gunicorn==26.2.0`, `numpy==2.4.6`, `scikit-learn==1.9.1`, `joblib==1.6.0`, `pandas==3.1.1`).
- **Set Up Virtual Environment:** Initialized `.venv` using `python -m venv .venv` and upgraded pip to 26.3 (`.\.venv\Scripts\python -m pip install --upgrade pip`).
- **Installed Dependencies:** Installed all packages from `requirements.txt` cleanly with exit code 0.
- **Created `train_model.py`:** Implemented dataset loading (`fetch_california_housing`), train/test split (80/20, `random_state=42`), model fitting (`RandomForestRegressor(n_estimators=100, random_state=42)`), and saving the trained model artifact to `model/model.pkl` via `joblib`.
- **Trained & Verified Model:** Executed `train_model.py` to create `model/model.pkl`, confirmed file existence, and verified sample prediction with the 8 input features.

---

## 2. Command Outputs

### 2.1 Virtual Environment Pip Upgrade
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> .\.venv\Scripts\python -m pip install --upgrade pip
Requirement already satisfied: pip in e:\antigravity-projects\ml-deployment-lab\.venv\lib\site-packages (24.2)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.2
    Uninstalling pip-24.2:
      Successfully uninstalled pip-24.2
Successfully installed pip-26.3
```

### 2.2 `pip install -r requirements.txt`
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> .\.venv\Scripts\pip install -r requirements.txt
Collecting flask==3.1.3 (from -r requirements.txt (line 1))
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting gunicorn==26.2.0 (from -r requirements.txt (line 2))
  Downloading gunicorn-26.2.0-py3-none-any.whl.metadata (5.5 kB)
Collecting numpy==2.4.6 (from -r requirements.txt (line 3))
  Downloading numpy-2.4.6-cp313-cp313-win_amd64.whl.metadata (6.6 kB)
Collecting scikit-learn==1.9.1 (from -r requirements.txt (line 4))
  Using cached scikit_learn-1.9.1-cp313-cp313-win_amd64.whl.metadata (9.3 kB)
Collecting joblib==1.6.0 (from -r requirements.txt (line 5))
  Using cached joblib-1.6.0-py3-none-any.whl.metadata (6.5 kB)
Collecting pandas==3.1.1 (from -r requirements.txt (line 6))
  Downloading pandas-3.1.1-cp313-cp313-win_amd64.whl.metadata (16 kB)
Collecting blinker>=1.9.0 (from flask==3.1.3->-r requirements.txt (line 1))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask==3.1.3->-r requirements.txt (line 1))
  Downloading click-8.5.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask==3.1.3->-r requirements.txt (line 1))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask==3.1.3->-r requirements.txt (line 1))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask==3.1.3->-r requirements.txt (line 1))
  Using cached markupsafe-3.0.4-cp313-cp313-win_amd64.whl.metadata (2.8 kB)
Collecting werkzeug>=3.1.0 (from flask==3.1.3->-r requirements.txt (line 1))
  Downloading werkzeug-3.1.9-py3-none-any.whl.metadata (4.1 kB)
Collecting scipy>=1.10.0 (from scikit-learn==1.9.1->-r requirements.txt (line 4))
  Using cached scipy-1.18.1-cp313-cp313-win_amd64.whl.metadata (61 kB)
Collecting narwhals>=2.0.1 (from scikit-learn==1.9.1->-r requirements.txt (line 4))
  Downloading narwhals-2.28.0-py3-none-any.whl.metadata (15 kB)
Collecting threadpoolctl>=3.5.0 (from scikit-learn==1.9.1->-r requirements.txt (line 4))
  Downloading threadpoolctl-3.8.0-py3-none-any.whl.metadata (29 kB)
Collecting cloudpickle>=3.0 (from joblib==1.6.0->-r requirements.txt (line 5))
  Using cached cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting python-dateutil>=2.9.0 (from pandas==3.1.1->-r requirements.txt (line 6))
  Downloading python_dateutil-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting tzdata (from pandas==3.1.1->-r requirements.txt (line 6))
  Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
Downloading gunicorn-26.2.0-py3-none-any.whl (228 kB)
Downloading numpy-2.4.6-cp313-cp313-win_amd64.whl (12.3 MB)
Using cached scikit_learn-1.9.1-cp313-cp313-win_amd64.whl (8.2 MB)
Using cached joblib-1.6.0-py3-none-any.whl (306 kB)
Downloading pandas-3.1.1-cp313-cp313-win_amd64.whl (10.7 MB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.5.1-py3-none-any.whl (126 kB)
Using cached cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.4-cp313-cp313-win_amd64.whl (14 kB)
Downloading narwhals-2.28.0-py3-none-any.whl (490 kB)
Downloading python_dateutil-4.0.0-py3-none-any.whl (92 kB)
Using cached scipy-1.18.1-cp313-cp313-win_amd64.whl (36.6 MB)
Downloading threadpoolctl-3.8.0-py3-none-any.whl (32 kB)
Downloading werkzeug-3.1.9-py3-none-any.whl (228 kB)
Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, threadpoolctl, numpy, narwhals, markupsafe, itsdangerous, gunicorn, cloudpickle, click, blinker, werkzeug, scipy, python-dateutil, joblib, jinja2, scikit-learn, pandas, flask
Successfully installed blinker-1.9.0 click-8.5.1 cloudpickle-3.1.2 flask-3.1.3 gunicorn-26.2.0 itsdangerous-2.2.0 jinja2-3.1.6 joblib-1.6.0 markupsafe-3.0.4 narwhals-2.28.0 numpy-2.4.6 pandas-3.1.1 python-dateutil-4.0.0 scikit-learn-1.9.1 scipy-1.18.1 threadpoolctl-3.8.0 tzdata-2026.6 werkzeug-3.1.9
```

### 2.3 `python train_model.py`
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> .\.venv\Scripts\python train_model.py
บันทึกโมเดลเรียบร้อยที่ model/model.pkl
```

### 2.4 `Test-Path .\model\model.pkl`
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> Test-Path .\model\model.pkl
True
```

### 2.5 Sample Prediction Command
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> .\.venv\Scripts\python -c "import joblib, numpy as np; m = joblib.load('model/model.pkl'); pred = float(m.predict(np.array([[8.3,25.0,6.0,1.0,1200,3.0,34.2,-118.3]]))[0]); print('Sample prediction:', round(pred, 4))"
Sample prediction: 4.0295
```

---

## 3. Deviations
- **No deviations:** All 6 package versions pinned in `README.original.md` (`flask==3.1.3`, `gunicorn==26.2.0`, `numpy==2.4.6`, `scikit-learn==1.9.1`, `joblib==1.6.0`, `pandas==3.1.1`) exist on PyPI and installed cleanly with exit code 0. No versions needed adjustment.

---

## 4. Anything the Elephant Should Know
1. **Installed Versions:**
   - `Flask==3.1.3`
   - `gunicorn==26.2.0`
   - `numpy==2.4.6`
   - `scikit-learn==1.9.1`
   - `joblib==1.6.0`
   - `pandas==3.1.1`
2. **Sample Prediction Value:**
   - The sample feature array `[[8.3, 25.0, 6.0, 1.0, 1200, 3.0, 34.2, -118.3]]` yielded `4.0295` (~4.03 as expected).
3. **Repository State:**
   - `.gitignore` is in place ignoring `model/`, `.venv/`, `__pycache__/`, `*.pyc`, and `README.original.md`.
   - `model/model.pkl` is verified present on disk and ignored by Git.
