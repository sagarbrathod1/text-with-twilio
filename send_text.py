import os
from twilio.rest import Client

def send_text_message(destination: str, message: str):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_=twilio_number,
            to=destination
        )

    print(message.sid)

def main():
    number = os.environ['MY_NUMBER']
    send_text_message(number, "Hello, friend!")

if __name__ == "__main__":
    main()