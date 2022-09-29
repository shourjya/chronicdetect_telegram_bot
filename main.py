from flask import Flask
from flask import request
from flask import Response
import requests
import json
 
app = Flask(__name__)
TELEGRAM_API_TOKEN = "5531087741:AAHNuNbYL267FWRBGHrKkblzPVo5PREIPC4"
 
def send_telegram_message(chat_id, text):
 	requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage", json={
 		"chat_id": chat_id,
        "text":text
 	})

def ask_age(chat_id):
    print("******** ->")
    r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "What is your age",
        "options": json.dumps(["Above 40-65","Below 65-79"])
    })
    print("******** ->")

def ask_gender(chat_id):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "What is your gender",
        "options": json.dumps(["Male","Female"])
    })

def ask_smoker(chat_id):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "Are you a smoker",
        "options": json.dumps(["Current","Former","Never"])
    })
    
def ask_diabetes(chat_id):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "History of Diabetes? ",
        "options": json.dumps(["No","Type 1","Type 2"])
    })
    
def ask_hypertension(chat_id):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "History of Hyperternsion? ",
        "options": json.dumps(["Yes","No"])
    })
    
def ask_hypertension_dx(chat_id):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendPoll", json={
        "chat_id": chat_id,
        "question": "Do you take medication for Hyperternsion? ",
        "options": json.dumps(["Yes","No"])
    })

@app.route(f"/{TELEGRAM_API_TOKEN}", methods=['POST','GET'])
def bot_webhook():
    try :

        payload = request.json
        message = payload["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text","")
        print("Message received ->",text)
        print("Message received ->",payload)

        if (text == '/start'):
            answer = "Welcome to Chronic Detect DTx Bot!"
            send_telegram_message(chat_id,answer)
            answer = "The bot will ask you a set of questions about your medical history and symptoms."
            send_telegram_message(chat_id,answer)
            answer = "The bot will then give you a risk score for developing heart attack or stroke within the next 10 years."
            send_telegram_message(chat_id,answer)
            answer = "Do you want to start [Y/N]"
            send_telegram_message(chat_id,answer)

        if (text == 'Y'):
            ask_age(chat_id)
            ask_gender(chat_id)
            ask_smoker(chat_id)
            ask_diabetes(chat_id)
            ask_hypertension(chat_id)
            ask_hypertension_dx(chat_id)

    except Exception as e:
        print(e)

    return {}, 200
  	
if __name__ == '__main__':
   app.run(port=5000,debug=True)
