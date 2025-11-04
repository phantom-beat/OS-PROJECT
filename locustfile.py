from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Tiempo de espera entre 1 y 5 segundos por cada usuario
    wait_time = between(1, 5)

    # Tarea que el usuario virtual realizará
    @task
    def index_page(self):
        self.client.get("/")
