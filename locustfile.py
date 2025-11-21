from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Especifica el host del servidor web a probar
    host = "http://192.168.56.101"

    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get("/")
