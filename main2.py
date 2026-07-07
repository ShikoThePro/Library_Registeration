from bs4 import BeautifulSoup as BS
import requests
from time import sleep
import datetime
import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"  # Enables bold (*text*) or italics (_text_)
    }
    
    response = requests.post(url, data=payload)
    return response.json()

# Configuration
TOKEN = "8948777131:AAHBXkrfBaUpHEnBNSxxw2xy3X459bckSiY"
CHAT_ID = "6460367199"
msg = "Register has just opened, Check it!"


while True:
  page = requests.get("https://www.bibalex.org/Libraries/Presentation/YP_Course/16Details.aspx?id=3491")
  parsed_page = BS(page.text, "html.parser")
  # avaliable_places = parsed_page.find("span", attrs={"id": "ctl00_ContentPlaceHolder1_lblAvailablePlaces"}).text[0:2].strip()
  reg_btn = parsed_page.find("input", attrs={"id": "ctl00_ContentPlaceHolder1_btnRegister"})
  # total_places = parsed_page.find("span", attrs={"id": "ctl00_ContentPlaceHolder1_lblAvailablePlaces"}).text[-2:].strip()
  # time_now = datetime.datetime.now()
  # print(f"{avaliable_places} out of {total_places} ===> {time_now.strftime("%H:%M:%S.%f")[:-3]}")
  if reg_btn:
    # send_telegram_message(TOKEN, CHAT_ID, msg)
    print("Found")
  else:
     print("Nothing")
  sleep(0.3)