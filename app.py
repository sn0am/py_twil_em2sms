import smtpd
import asyncore
from email.parser import BytesParser
from twilio.rest import Client
import time
from dotenv import load_dotenv
import os
import shutup

shutup.please()
# Load ENV file.
folder = os.getcwd()
load_dotenv(f'{folder}/.env')


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        try:
            # Env Variables
            twil_sid = os.environ.get("account_sid")
            twil_auth = os.environ.get("auth_token")
            twil_num = os.environ.get("from_num")
            # Extract phone number from "To" header.
            number = rcpttos[0].split('@')[0]
            # Parse Email
            parse = BytesParser()
            email_data = parse.parsebytes(data)
            email_subject = email_data.get('Subject')
            print(f"Data type received is: {email_data.get_content_type()}")
            for part in email_data.walk():
                if part.get_content_type() != 'text/plain':
                    print(f"Only forwarding 'text/plain' portion of the email.")
                if part.get_content_type() == 'text/plain':
                    raw_body = part.get_payload(decode=True)
                    email_body = str(raw_body)
                    email_body = email_body[2:-1].replace("\\n", "\n")
                    email_body = email_body.replace("\\r", "")

            time.sleep(5)
            # Initialize Twilio client.
            client = Client(twil_sid, twil_auth)
            # Send SMS.
            client.messages.create(
                to=f"+1{number}",
                from_=twil_num,
                body=f"{email_subject}:\n\n{email_body}")
            print(f"'The following message was sent to: {number}")
            print(f"{email_subject}:\n\n{email_body}'")
            print("----------------")
        except:
            print("pass")
            # Print if error occurs.
            print(f"'Error occurred while sending message to: {number}")
            print(f"{email_subject}:\n\n{email_body}'")
            print("----------------")


server = CustomSMTPServer(('0.0.0.0', 25), None)
print("email2sms is listening on port 25")

asyncore.loop()
