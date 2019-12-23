import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from twilio.rest import Client

class_code = "CMSC351"
section_num = 2 # 0101 = 1, 0201 = 2, 0301 = 3, ... (based on the order of Testudo)

url = "https://app.testudo.umd.edu/soc/202001/" + class_code[0:4] + "/" + class_code

while True:
    print("Getting data...")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    section_data = soup.findAll("div", {"class": "section delivery-f2f"})[section_num - 1]

    open_seats = section_data.findAll("span", {"class": "open-seats-count"})[0]

    open_seats_num = int(open_seats.text)

    if open_seats_num > 0:
        print("There are open seats! Sending text message...")

        client = Client("x", "y")

        client.messages.create(to = "+12345678912", from_ = "+12345678912",
            body = "A seat has opened up in " + class_code + "!")

        print("Message sent.")

        break

    else:
        print("No open seats.")

    print("Sleeping for a minute...")

    time.sleep(60)
