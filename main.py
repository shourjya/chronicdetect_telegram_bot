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
    try :

        payload = request.json
        message = payload["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text","")
        print("Message received",text)

        # if (text != "Y","N") | (status == 8):
        #     answer = "Welcome to Chronic Detect DTx Bot!"
        #     send_telegram_message(chat_id,answer)
        #     answer = "The bot will ask you a set of questions about your medical history and symptoms."
        #     send_telegram_message(chat_id,answer)
        #     answer = "The bot will then give you a risk score for developing heart attack or stroke within the next 10 years."
        #     send_telegram_message(chat_id,answer)

        #     answer = "Do you want to continue? [Y/N]"
        #     send_telegram_message(chat_id,answer)

        if text == "Y":
            print("status 1")

            answer = "What is your age?"
            send_telegram_message(chat_id,answer)

            age = text

            status = 2

        if text == "N":
            print("status 10")

            answer = "Sorry to hear that!"
            send_telegram_message(chat_id,answer)

            status = 8

        if status == 2:
            print("status 2")

            age = text
            send_telegram_message(chat_id,"What is your sex? [M/F]")

            status = 3

        if status == 3:
            print("status 2")

            sex = text
            send_telegram_message(chat_id,"WAre you a smoker? [Smoker/Non-Smoker]")

            status = 4

        if status == 4:
            print("status 2")

            age = text
            send_telegram_message(chat_id,"Do you have diabetes? [No/Type 1/Type 2]")

            status = 5

        if status == 5:
            print("status 2")

            age = text
            send_telegram_message(chat_id,"Do you have high blood cholesterol? [Yes/No]")

            status = 6

        if status == 6:
            print("status 2")

            age = text
            send_telegram_message(chat_id,"Do you have high blood pressure? [Yes/No]")

            status = 7

        if status == 7:
            print("status 2")

            age = text
            send_telegram_message(chat_id,"Do you have take blood pressure medication? [Yes/No]")

            status = 8
    except Exception as e:
        print(e)

    return {}, 200
  	
if __name__ == '__main__':
   app.run(port=5000,debug=True)