from twilio.rest import Client
from dotenv import load_dotenv
import os


def send_sms(message):
    load_dotenv()

    # My informatiom from .env
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_NUMBER")
    target_number = os.getenv("TARGET_NUMBER")

    client = Client(account_sid, auth_token)

    # creating and sending the message
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=target_number
    )




