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

@app.route(f"/{TELEGRAM_API_TOKEN}", methods=["GET","POST"])
def bot_webhook():
    payload = request.json
    message = payload["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text","")
    print("Message received",text)

    answer = "Welcome to Chronic Detect DTx Bot!"
    send_telegram_message(chat_id,answer)
    answer = "The bot will ask you a set of questions about your medical history and symptoms."
    send_telegram_message(chat_id,answer)
    answer = "The bot will then give you a risk score for developing heart attack or stroke within the next 10 years."
    send_telegram_message(chat_id,answer)

    answer = "Do you want to continue? [Y/N]"
    send_telegram_message(chat_id,answer)

    payload1 = request.json
    message1 = payload1["message"]
    letsgo = message1.get("text","")
    print("User Status",letsgo)


    return {}, 200
  	
if __name__ == '__main__':
   app.run(port=5000,debug=True)