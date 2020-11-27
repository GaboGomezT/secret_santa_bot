from twilio.rest import Client
from random import choice
import json

with open("config.json") as f:
    config = json.load(f)
with open("contacts.json") as f:
    contacts = json.load(f)

account_sid = config.get("account_sid")
auth_token = config.get("auth_token")
twilio_number = config.get("twilio_number")
country_code = config.get("country_code")

client = Client(account_sid, auth_token)


def reset_contacts():
    for k, v in contacts.items():
        contacts[k]["taken"] = False


def take_name():
    for name, value in contacts.items():
        filtered_contacts = {k: v for k, v in contacts.items() if v["taken"] is False}
        random_choice = choice(list(filtered_contacts.items()))
        contacts[name]["pair"] = random_choice[0]
        contacts[random_choice[0]]["taken"] = True
        if random_choice[0] == name:
            return True
    return False


def send_messages():
    for name, value in contacts.items():
        # Feel free to customize this default message
        message = f"Hello {name}! Your are {value['pair']}'s secret santa! Make sure to give them a thoughtful gift!'"
        client.messages.create(
            to=f"{country_code}{value['number']}", from_=twilio_number, body=message
        )
    print("\033[92mSecret Santas Sucessfully Launched!\033[0m")


def secret_santa_sort():
    print(f"\033[92mChoosing secret santas...\033[0m")
    start_over = take_name()
    while start_over:
        reset_contacts()
        start_over = take_name()
    send_messages()


secret_santa_sort()
