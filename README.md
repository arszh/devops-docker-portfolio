# DevOps Docker  Project  
**Flask + PostgreSQL + Nginx + Docker Compose**

This repository demonstrates a **production-ready, multi-service environment** using Docker.  
It is intended as a **portfolio project for DevOps / Cloud / Platform Engineers**, especially on platforms like **Upwork**, where clients want to see real, deployable infrastructure skills.

This project shows the ability to:

- Containerize applications  
- Configure reverse proxies  
- Work with databases  
- Build multi-service systems  
- Structure production-like Docker environments  
- Use environment-based configuration  
- Build clear, reproducible developer infrastructure  

---

# 🧱 Project Overview

This stack includes:

- **Flask web application** running via Gunicorn  
- **PostgreSQL database** with persistent storage  
- **Nginx reverse proxy** forwarding external HTTP traffic  
- **Docker Compose** orchestrating all components  
- **Healthcheck route** for monitoring  
- Automatic database initialization on startup  
- Clean service separation and readable infrastructure layout  

---

# 🔥 Features

✔ Multi-container architecture  
✔ Environment variables support  
✔ Database-backed API  
✔ Reverse proxy with Nginx  
✔ Health/Readiness checks  
✔ Persistent volumes  

---



# 🚀 Getting Started

## 1. Clone the repo
```bash
git clone https://github.com/arsenzh/devops-docker-portfolio.git
cd devops-docker-portfolio
```

## 2. Create environment file
```bash
cp .env.example .env
```

## 3. Build and run the stack
```bash
docker compose up --build
```

---

# 📫 Author
GitHub: https://github.com/arsenzh
