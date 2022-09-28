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

@app.route(f"/{TELEGRAM_API_TOKEN}", methods=["POST"])

def bot_webhook():
    try :

        payload = request.json
        message = payload["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text","")
        print("Message received ->",text)

    except Exception as e:
        print(e)

    return text

text = bot_webhook()
if (text = "/start") | (status == 10):
    answer = "Welcome to Chronic Detect DTx Bot!"
    send_telegram_message(chat_id,answer)
    answer = "The bot will ask you a set of questions about your medical history and symptoms."
    send_telegram_message(chat_id,answer)
    answer = "The bot will then give you a risk score for developing heart attack or stroke within the next 10 years."
    send_telegram_message(chat_id,answer)

    answer = "Do you want to continue? [Y/N]"
    send_telegram_message(chat_id,answer)
    text = bot_webhook()
    

if __name__ == '__main__':
   app.run(port=5000,debug=True)
