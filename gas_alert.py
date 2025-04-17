import requests
import time
import os

ETH_GAS_API = "https://api.etherscan.io/api"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 80))  # gwei

def get_gas_price():
    params = {
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": "YourEtherscanApiKey"
    }
    response = requests.get(ETH_GAS_API, params=params).json()
    try:
        return int(response["result"]["ProposeGasPrice"])
    except:
        return None

def send_telegram_alert(price):
    message = f"⚠️ Ethereum gas price alert: {price} GWEI"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        price = get_gas_price()
        if price:
            print(f"[INFO] Current gas price: {price} GWEI")
            if price >= ALERT_THRESHOLD:
                send_telegram_alert(price)
        else:
            print("[ERROR] Failed to fetch gas price")
        time.sleep(60)
