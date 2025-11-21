# OS Project -- README

## 📌 Overview

This project implements a fully automated infrastructure stack using
**Vagrant**, **Ansible**, **Docker**, **Prometheus**, **Node Exporter**,
**Nginx**, and **Locust** for benchmarking.\
It provisions a virtual machine, installs required services, configures
monitoring, and deploys load‑testing tools.

The objective is to deliver a reproducible environment where services
are deployed automatically and monitored in real time.

------------------------------------------------------------------------

## 🚀 Project Structure

    OS-PROJECT-main/
    │── Vagrantfile
    │── ansible/
    │   ├── playbook.yml
    │   └── roles/
    │       ├── docker/
    │       │   ├── tasks/
    │       │   └── templates/
    │       ├── nginx/
    │       ├── prometheus/
    │       └── node_exporter/
    │── locust/
    │   ├── locustfile1.py
    │   └── locustfile2.py
    │── docker-compose.yml
    │── prometheus.yml

------------------------------------------------------------------------

## 🛠 How the Project Was Developed

### 1. Virtualization (Vagrant)

A **Vagrantfile** defines a base Ubuntu VM and provisions it using
Ansible automatically.

Main commands used:

``` bash
vagrant up
vagrant ssh
vagrant destroy -f
```

------------------------------------------------------------------------

### 2. Automation (Ansible)

The main playbook:

    ansible/playbook.yml

Runs roles in order: 1. **Docker installation** 2. **Prometheus setup**
3. **Node Exporter setup** 4. **Nginx deployment**

Run with:

``` bash
ansible-playbook -i inventory ansible/playbook.yml
```

------------------------------------------------------------------------

### 3. Docker Deployment

The Ansible role installs Docker and deploys containers automatically
using:

    docker-compose up -d

Based on the file:

    docker-compose.yml

Which includes services such as: - Nginx - Prometheus - Node Exporter

------------------------------------------------------------------------

### 4. Monitoring Setup

**prometheus.yml** configures scraping:

``` yaml
scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node_exporter"
    static_configs:
      - targets: ["localhost:9100"]
```

------------------------------------------------------------------------

### 5. Web Server (Nginx)

The Ansible role:

    ansible/roles/nginx

Deploys configuration templates and ensures the service is running.

Commands used during development:

``` bash
systemctl restart nginx
systemctl enable nginx
```

------------------------------------------------------------------------

### 6. Load Testing (Locust)

Two load‑testing scripts:

    locustfile1.py
    locustfile2.py

Executed with:

``` bash
locust -f locustfile1.py
```

Provide benchmarking for the Nginx service.

------------------------------------------------------------------------

## 🧪 Testing The Stack

After deployment:

### Access Prometheus:

    http://localhost:9090

### Access Node Exporter:

    http://localhost:9100/metrics

### Access NGINX:

    http://localhost:80

### Run Locust UI:

    http://localhost:8089

------------------------------------------------------------------------

## 📁 Key Configuration Files Included

✔ `docker-compose.yml`\
✔ `prometheus.yml`\
✔ All Ansible roles and tasks\
✔ Locust benchmark scripts\
✔ Nginx templates

All files were analyzed to build this documentation.

------------------------------------------------------------------------

## 📄 Author & Contributions

Santiago Torralba
Jose David Aguirre Salinas
