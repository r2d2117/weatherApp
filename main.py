import requests as rq
from bs4 import BeautifulSoup
import os
from twilio.rest import Client


url = rq.get('https://weather.gc.ca/city/pages/qc-147_metric_e.html')
soup = BeautifulSoup(url.text, 'html.parser')
weather = soup.find("details", class_="panel panel-default hidden-xs")

date = weather.find_all("dd", class_="mrgn-bttm-0")[1].get_text()

state = weather.find_all("dd", class_="mrgn-bttm-0")[2].get_text().lower()
pressure = weather.find_all("dd", class_="mrgn-bttm-0")[3].get_text()
celsius = weather.find_all("dd", class_="mrgn-bttm-0")[6].get_text()
celsius = celsius.strip().replace(celsius[-4],"")
humidity = weather.find_all("dd", class_="mrgn-bttm-0")[10].get_text()
wind = weather.find_all("dd", class_="mrgn-bttm-0")[11].get_text().strip()
humidex = weather.find_all("dd", class_="mrgn-bttm-0")[13].get_text()
visibility = weather.find_all("dd", class_="mrgn-bttm-0")[15].get_text().strip()

print(visibility)


message = "Hey so the date today is "+date+"."+"\nIts gonna be "+state+"\nat around "+celsius+".\nThe humidity is going to be "+humidity+" with a visibility of "+visibility+"."


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



message = client.messages \
    .create(
         body=message,
         from_='16473607775',
         to='+15148242296'
     )

