# Proyecto de Infraestructura Automatizada

## 🎯 Resumen

Este proyecto implementa una infraestructura completamente automatizada para desplegar y monitorear un servidor web Nginx. Utiliza **Vagrant** para la virtualización, **Ansible** para la configuración y **Docker** para ejecutar servicios de monitoreo como **Prometheus** y **Grafana**.

---

## ⚙️ Arquitectura

La arquitectura se compone de dos máquinas virtuales principales orquestadas por Vagrant y configuradas por Ansible:

1.  **Servidor Web (`web`)**:
    -   **IP**: `192.168.56.101`
    -   **Software**: Nginx.
    -   **Propósito**: Alojar el sitio web y exponer un endpoint `/nginx_status` para el monitoreo.

2.  **Servidor de Monitoreo (`monitoring`)**:
    -   **IP**: `192.168.56.102`
    -   **Software**: Docker, Prometheus, Grafana, Node Exporter, Nginx Exporter.
    -   **Propósito**: Recolectar, almacenar y visualizar métricas de toda la infraestructura.

El flujo de datos es el siguiente:
- **Nginx Exporter** consulta el endpoint `/nginx_status` en la VM `web`.
- **Prometheus** recolecta métricas de **Nginx Exporter** y **Node Exporter**.
- **Grafana** consulta a **Prometheus** para mostrar los datos en dashboards.

---

## 📂 Estructura del Proyecto

```
/
├── Vagrantfile                # Define las máquinas virtuales.
├── ansible/
│   ├── playbook.yml           # Orquesta los roles de Ansible.
│   └── roles/
│       ├── common/            # Tareas comunes.
│       ├── monitoring/        # Configura el stack de monitoreo.
│       └── nginx/             # Configura Nginx.
└── locustfile.py              # Script para pruebas de carga.
```

---

## 🚀 Cómo Empezar

### Prerrequisitos

- **VirtualBox**
- **Vagrant**
- **Ansible**

### Pasos

1.  Clona el repositorio.
2.  Desde la raíz del proyecto, ejecuta `vagrant up`.
3.  Una vez finalizado, los servicios estarán disponibles en las IPs especificadas.

---

## 🔧 Configuraciones por Defecto

A continuación se listan las configuraciones por defecto extraídas de los archivos del proyecto:

-   **VM `web`**:
    -   **IP**: `192.168.56.101`
    -   **Memoria**: 2048 MB
    -   **CPUs**: 2
-   **VM `monitoring`**:
    -   **IP**: `192.168.56.102`
    -   **Memoria**: 4096 MB
    -   **CPUs**: 2
-   **Grafana**:
    -   **Usuario**: `admin`
    -   **Contraseña**: `admin`
-   **Prometheus Scrape Interval**: `10s`

---

## 🌐 Acceso a los Servicios

-   **Servidor Web Nginx**: [http://192.168.56.101](http://192.168.56.101)
-   **Prometheus UI**: [http://192.168.56.102:9090](http://192.168.56.102:9090)
-   **Grafana UI**: [http://192.168.56.102:3000](http://192.168.56.102:3000)

---

## ✨ Casos de Uso

Este proyecto es ideal para:

-   **Entornos de Desarrollo y Pruebas**: Simula un entorno de producción simple con monitoreo integrado.
-   **Aprendizaje de DevOps**: Sirve como un ejemplo práctico de automatización con Vagrant, Ansible y Docker.
-   **Benchmarking**: Permite realizar pruebas de carga sobre Nginx y visualizar el impacto en tiempo real con Grafana.

---

## 📄 Ejemplo de Código

El corazón del stack de monitoreo se define en el archivo `docker-compose.yml`, que es desplegado por Ansible.

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
    networks:
      - monitoring

  node_exporter:
    image: prom/node-exporter:latest
    container_name: node_exporter
    restart: unless-stopped
    ports:
      - "9100:9100"
    networks:
      - monitoring

  nginx_exporter:
    image: nginx/nginx-prometheus-exporter:latest
    container_name: nginx_exporter
    restart: unless-stopped
    ports:
      - "9113:9113"
    command:
      - -nginx.scrape-uri
      - http://192.168.56.101/nginx_status
    networks:
      - monitoring

networks:
  monitoring:
    driver: bridge
```

---

## ⚙️ Comandos Útiles de Vagrant

-   **Conectarse por SSH**: `vagrant ssh web` o `vagrant ssh monitoring`
-   **Re-aprovisionar**: `vagrant provision`
-   **Apagar**: `vagrant halt`
-   **Destruir**: `vagrant destroy -f`

---

## 📄 Autores y Contribuciones

-   Jose Aguirre
-   Santiago Torralba

