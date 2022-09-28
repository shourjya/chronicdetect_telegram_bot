
import requests

base_url = "https://api.telegram.org/bot5531087741:AAHNuNbYL267FWRBGHrKkblzPVo5PREIPC4"

def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  message = data["message"]
  chat_id = message["chat"]["id"]
  text = message.get("text","")
  print("Message received ->",text)

offset = 0

while True:  
  offset = read_msg(offset)
 
