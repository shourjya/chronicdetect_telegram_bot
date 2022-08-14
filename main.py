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

   	try:	

   		if answer == 'Y'
    	
    		send_telegram_message(chat_id,"What is your age")
    		payload = request.json
    		message = payload["message"]
    		age = message.get("text","")
	    	
    		send_telegram_message(chat_id,"What is your sex [M/F]")
    		payload = request.json
    		message = payload["message"]
    		sex = message.get("text","")

    		send_telegram_message(chat_id,"Are you a smoker [Smoker/Non-Smoker]")
    		payload = request.json
    		message = payload["message"]
    		sex = message.get("text","")

    		send_telegram_message(chat_id,"Do you have diabetes [No/Type 1/Type 2]")
    		payload = request.json
    		message = payload["message"]
    		Diabetes = message.get("text","")

    		send_telegram_message(chat_id,"Do you have high blood cholesterol [Yes/No]")
    		payload = request.json
    		message = payload["message"]
    		blood_cholesterol = message.get("text","")

    		send_telegram_message(chat_id,"Do you have high blood pressure [Yes/No]")
    		payload = request.json
    		message = payload["message"]
    		BP = message.get("text","")

    		send_telegram_message(chat_id,"Do you have take blood pressure medication [Yes/No]")
    		payload = request.json
    		message = payload["message"]
    		BP_medication = message.get("text","")

    	elif answer == 'N'
    		send_telegram_message(chat_id,'Thanks. Hope to see you soon.')

    except Exception as e:
    	send_telegram_message(chat_id,"Something went wrong! Restart App")

    return {}, 200 
 
if __name__ == '__main__':
   app.run(port=5000,debug=True)
