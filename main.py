import requests
import time

TOKEN = "462178880:y1BGm7sEdatcL3sVZquick6U07Vzd7xLLmk"

def send_message(chat_id, text):
    url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })

offset = 0

while True:
    url = f"https://tapi.bale.ai/bot{TOKEN}/getUpdates?offset={offset}"
    response = requests.get(url)
    data = response.json()

    for item in data.get("result", []):
        offset = item["update_id"] + 1

        message = item.get("message")
        if message:
            chat_id = message["chat"]["id"]
            send_message(chat_id, "سلام 👋 ربات من فعاله")

    time.sleep(2)