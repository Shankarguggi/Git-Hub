# ACEest Fitness & Gym

A small Flask API for managing gym members, packaged with automated tests, Docker, GitHub Actions, and a Jenkins build pipeline.

## Features

- `GET /` returns the service health status.
- `GET /members` lists registered members.
- `POST /members` creates a member with a required `name` and optional `plan`.

## Local setup

Prerequisites: Python 3.12+ and Git.

```powershell
git clone <your-repository-url>
cd Git-Hub
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/` after the server starts.

Create a member from PowerShell:

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/members -ContentType application/json -Body '{"name":"Aarav","plan":"premium"}'
```

## Run tests

```powershell
python -m pytest -q
```

## Docker

Prerequisite: Docker Desktop must be running.

```powershell
docker build -t aceest-fitness:local .
docker run --rm -p 5000:5000 aceest-fitness:local
```

## CI/CD

GitHub Actions is configured in `.github/workflows/main.yml`. Every push and pull request installs dependencies, runs Pytest, then builds the Docker image.

`Jenkinsfile` defines the Jenkins BUILD workflow: it checks out the connected GitHub repository, installs dependencies, runs Pytest, and builds a Docker image tagged with the Jenkins build number. Create a Pipeline job in Jenkins, select **Pipeline script from SCM**, connect the repository, and ensure the Jenkins agent has Python 3.12+ and Docker available.

## Suggested Git workflow

Create a branch for each change, for example `feature/member-api` or `ci/add-jenkins-build`. Use clear commits such as `feat: add member API`, `test: cover member validation`, and `ci: add GitHub Actions workflow`, then open a pull request into `main`.
