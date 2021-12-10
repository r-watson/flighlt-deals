from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_text(self, fdata):
        flight_data = fdata
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        my_phone = os.getenv('MY_PHONE_NUMBER')
        twilio_phone = os.getenv('TWILIO_PHONE_NUMBER')
        # print(fdata)
        outbound_date = (fdata['route'][0]['utc_departure'].split("T"))[0]
        inbound_date = (fdata['route'][1]['utc_departure'].split("T"))[0]

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert! Only £{flight_data['price']} to fly from {flight_data['cityFrom']}-"
                 f"{flight_data['cityCodeFrom']} to {flight_data['cityTo']}-{flight_data['cityCodeTo']}, "
                 f"from {outbound_date} to {inbound_date}.",
            from_=twilio_phone,
            to=my_phone,
        )

        print(message.sid)