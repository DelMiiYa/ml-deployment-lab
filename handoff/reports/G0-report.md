# Task G0 Report: Preserve Original README and Check Environment

## 1. What Was Done
- Copied `README.md` to `README.original.md` using `Copy-Item -Path .\README.md -Destination .\README.original.md -Force`.
- Verified file existence with `Test-Path .\README.original.md` (returned `True`).
- Verified cryptographic integrity using SHA-256 hash comparison between `README.md` and `README.original.md` (returned `True`, hash: `E17A6439C5733CB7867BBF4D5B89EFF133057D1CC724B9C8A2168832BC0CA22F`).
- Examined the Thai specification in `README.original.md` and extracted all markdown headings and dependency listings.
- Inspected the local environment: Python version, Git status/remote, Docker CLI installation and daemon status.

---

## 2. Command Outputs

### 2.1 File Copy and Hash Verification
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> Copy-Item -Path .\README.md -Destination .\README.original.md -Force
PS E:\Antigravity-Projects\ml-deployment-lab> Test-Path .\README.original.md
True
PS E:\Antigravity-Projects\ml-deployment-lab> (Get-FileHash .\README.md).Hash -eq (Get-FileHash .\README.original.md).Hash
True
PS E:\Antigravity-Projects\ml-deployment-lab> Get-FileHash .\README.md, .\README.original.md
Algorithm  Hash                                                             Path
---------  ----                                                             ----
SHA256     E17A6439C5733CB7867BBF4D5B89EFF133057D1CC724B9C8A2168832BC0CA22F E:\Antigravity-Projects\ml-deployment-lab\README.md
SHA256     E17A6439C5733CB7867BBF4D5B89EFF133057D1CC724B9C8A2168832BC0CA22F E:\Antigravity-Projects\ml-deployment-lab\README.original.md
```

### 2.2 Python Version
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> python --version
Python 3.13.0
```

### 2.3 Docker Version & Daemon Status
Initial check without PATH reload:
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> docker --version
docker : The term 'docker' is not recognized as the name of a cmdlet, function, script file, or operable program.
```
Docker executable location found:
`C:\Users\User\AppData\Local\Programs\DockerDesktop\resources\bin\docker.exe` (present in User registry `Path`).

With PATH updated from registry:
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
PS E:\Antigravity-Projects\ml-deployment-lab> docker --version
Docker version 29.9.3, build 5457199

PS E:\Antigravity-Projects\ml-deployment-lab> docker info
Client:
 Version:    29.9.3
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent, ai, buildx (v0.38.1), compose (v5.7.0), debug, desktop (4.99.0), dhi, extension, init, mcp, model, offload, pass, sandbox, scout

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 29.9.3
 Storage Driver: overlayfs
 Logging Driver: local
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 nvidia runc
 Default Runtime: runc
 Kernel Version: 6.18.58.1-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 12
 Total Memory: 7.421GiB
 Name: docker-desktop
```
Docker daemon is active and running via Docker Desktop on WSL2.

### 2.4 Git Status and Remote
```powershell
PS E:\Antigravity-Projects\ml-deployment-lab> git status -sb
## main...origin/main
?? README.original.md
?? handoff/

PS E:\Antigravity-Projects\ml-deployment-lab> git branch
* main

PS E:\Antigravity-Projects\ml-deployment-lab> git remote -v
origin  https://github.com/DelMiiYa/ml-deployment-lab.git (fetch)
origin  https://github.com/DelMiiYa/ml-deployment-lab.git (push)
```

### 2.5 Markdown Section Headings in `README.original.md`
- `# การสร้าง Model as a Service ด้วย Flask และ Docker`
- `## 1. วัตถุประสงค์`
- `## 2. โครงสร้างโฟลเดอร์ของโปรเจ็ค`
- `## 3. ขั้นตอนการดำเนินงาน`
  - `### 3.1 สร้างโฟลเดอร์โครงการ`
  - `### 3.2 สร้างและฝึกโมเดล`
  - `### 3.3 สร้างแอปพลิเคชัน Flask`
  - `### 3.4 สร้างหน้าเว็บสำหรับทดสอบ`
  - `### 3.5 สร้างไฟล์ requirements.txt`
  - `### 3.6 สร้างไฟล์ Dockerfile`
  - `### 3.7 สร้างและรัน Docker Container`
- `## 4. การตรวจสอบความถูกต้อง`
- `## 5. วิธีส่งงาน`
- `## 6. ปัญหาที่พบบ่อยและแนวทางแก้ไข`
- `## 7. หมายเหตุเพิ่มเติม`

### 2.6 Requirements Block in `README.original.md`
```text
flask==3.1.3
gunicorn==26.2.0
numpy==2.4.6
scikit-learn==1.9.1
joblib==1.6.0
pandas==3.1.1
```

---

## 3. Deviations
1. **Docker CLI PATH in spawned subshells:**
   - Docker Desktop is installed in `%LOCALAPPDATA%\Programs\DockerDesktop\resources\bin`. While present in the user registry `Path`, the active shell session did not inherit it initially.
   - **Fix/Workaround:** Future Goldfish agents running Docker commands should prepend `$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")` or reference `& "$env:LOCALAPPDATA\Programs\DockerDesktop\resources\bin\docker.exe"`.
   - The Docker daemon itself is running and healthy (`Server Version: 29.9.3`).

---

## 4. Anything the Elephant Should Know
1. **Docker execution in subsequent tasks:**
   Tasks G3, G4, and G5 invoke `docker build` and `docker run`. The agent scripts should include the PATH refresh snippet to ensure `docker` command resolution succeeds.
2. **Version numbers in original README:**
   The pinned versions in Section 3.5 (`numpy==2.4.6`, `scikit-learn==1.9.1`, etc.) represent future/placeholder version numbers not yet published on PyPI. Subsequent task G1 must adhere to `SSOT.md` regarding valid package versions.
3. **Repository state:**
   `README.original.md` has been created and preserves the Thai specification verbatim.
