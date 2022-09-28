from flask import Flask
from flask import request
from flask import Response
import requests
 
app = Flask(__name__)
TELEGRAM_API_TOKEN = "5531087741:AAHNuNbYL267FWRBGHrKkblzPVo5PREIPC4"
 
def send_telegram_message(chat_id, text):
 	requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage", json={
 		"chat_id": chat_id,
 		"text":text
 	})

def bot_webhook():
	try :
        payload = request.json
        message = payload["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text","")
        print("Message received ->",text)
    except Exception as e:
        print(e)
    return text, 200

@app.route(f"/{TELEGRAM_API_TOKEN}", methods=["GET","POST"])
to_print, val = bot_webhook()

if __name__ == '__main__':
	app.run(port=5000,debug=True)
