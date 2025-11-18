import threading
import requests

URL = "http://192.168.56.101/"
HEADERS = {
    "User-Agent": "SimpleLoadTester/1.0"
}

def make_request():
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()  # Lanza una excepción para respuestas de error (4xx o 5xx)

threads = []
print("Starting to send 100 requests...")
for i in range(100):
    thread = threading.Thread(target=make_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Load test finished. 100 requests were sent.")
