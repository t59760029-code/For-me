import time
import os
import httpx
import random

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:8000/simulate")

DEVICE_IDS = ["sensor-1", "sensor-2", "sensor-3"]

async def send(client, payload):
    try:
        r = client.post(BACKEND_URL, json=payload, timeout=5)
        # ignore response
    except Exception as e:
        print("publish error:", e)


def main():
    print("Simulator starting, will POST to", BACKEND_URL)
    import requests
    while True:
        device = random.choice(DEVICE_IDS)
        payload = {
            "device_id": device,
            "type": "temperature",
            "value": round(15 + random.random()*10, 2),
            "ts": time.time()
        }
        try:
            requests.post(BACKEND_URL, json=payload, timeout=5)
        except Exception as e:
            print("error sending", e)
        time.sleep(2)

if __name__ == '__main__':
    main()
