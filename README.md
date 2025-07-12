# 🚀 Flask Web Application with CI/CD Pipeline using Docker, Jenkins, and AWS EC2

This is **Project 1** of my DevOps Project Series. It demonstrates how to build and deploy a simple Flask application using a fully automated CI/CD pipeline with Jenkins, Docker, GitHub, and AWS EC2.

----------------------------------------------------------------------------------------------

## Project Objective

- Develop a Flask web app with custom routes
- Write unit tests with Pytest
- Containerize the app using Docker
- Push Docker image to Docker Hub
- Automate the entire process using Jenkins Freestyle Project
- Deploy on AWS EC2 with auto-run and verify via browser

---

## Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| **Python**  | Programming language             |
| **Flask**   | Web application framework        |
| **Pytest**  | Unit testing framework           |
| **Docker**  | Containerization                 |
| **Jenkins** | CI/CD automation                 |
| **GitHub**  | Version control                  |
| **AWS EC2** | Hosting/Deployment               |

----------------------------------------------------------------------------------------------

## Pre-requisites

Before starting the project, the following were done:

- Created **AWS EC2 instance** using Ubuntu AMI
- Installed **Docker** and **Jenkins**
  - Added Jenkins user to Docker group
  - Restarted services
- Installed **Python3**, Flask, and Pytest (if not available)
- Updated **Security Group** to allow **port 8080 (Jenkins)** and **port 5000 (Flask)**

----------------------------------------------------------------------------------------------

## Project Procedure

### Step 1: GitHub Repository Setup

- Created a new GitHub repository: `flask_web`
- Synced repo to local system using Git Bash on Windows

```bash
mkdir flask_web
cd flask_web
git init
git remote add origin <repo_url>
git pull origin main

### Step 2: Created a Simple Flask App
📄 app.py

from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "i am nitin dhiman and i have run this pipeline"

@app.route("/phone")
def lwphone():
    return "9808580941"

app.run(host="0.0.0.0", port=5000)

### Step 3: Created a Unit Test File
📄 test_app.py

from app import lwphone

def test_lwphone():
    assert lwphone() == "9808580941"

### Step 4: Created a Dockerfile
📄 Dockerfile

FROM redhat/ubi8
RUN yum install python3 -y
RUN pip3 install flask
COPY app.py /app.py
CMD ["python3", "/app.py"]

### Step 5: Git Operations

git add .
git commit -m "Initial commit with app, test and Dockerfile"
git push origin main

### Step 6: Jenkins CI/CD Setup
Accessed Jenkins at http://<EC2-IP>:8080

Created Freestyle Project

Configured:

GitHub project URL

Source Code Management: Git with repo link

Poll SCM trigger: * * * * * (every minute)

Under Build Step → Execute Shell, added:

docker build -t nitindhiman22/myweb:v1 .
docker push nitindhiman22/myweb:v1
docker rm -f myweb || true
docker run -dit --name myweb -p 5000:5000 nitindhiman22/myweb:v1

### Results
Triggered Build Now in Jenkins

Build successfully cloned repo, built image, pushed to Docker Hub, and deployed the container

Accessed the app using browser:

http://<EC2-IP>:5000/info
http://<EC2-IP>:5000/phone

## Output:
/info: "i am nitin dhiman and i have run this pipeline"

/phone: "9808580941"

🖼️ Screenshots
(Add screenshots or link to deployment video if available)

Docker Hub Link
🔗docker push nitindhiman22/myweb:tagname

Key Learnings
Setting up Jenkins on EC2 for pipeline automation

Writing unit tests for Flask routes

Building and pushing Docker images

Deploying applications via Jenkins Freestyle Job

Handling port/security groups on AWS

🙌 Author
Nitin Dhiman
🚀 DevOps Enthusiast | Learner on 60 Days DevOps Challenge
📫 LinkedIn | 🐙 GitHub

⭐️ Support
If you found this project useful, please ⭐️ the repo and follow me on LinkedIn. More DevOps projects coming soon!


