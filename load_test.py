import threading
import urllib.request

def make_request():
    try:
        with urllib.request.urlopen("http://192.168.56.101/", timeout=10) as response:
            response.read()
    except Exception as e:
        # This will print errors if the web server is not reachable
        print(f"Request failed: {e}")

threads = []
print("Starting to send 100 requests...")
for i in range(100):
    thread = threading.Thread(target=make_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Load test finished. 100 requests were sent.")
