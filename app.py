import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class EmailAPI:
    def __init__(self):
        self.sender_email = os.getenv("EMAIL_SENDER")
        self.app_password = os.getenv("EMAIL_APP_PASSWORD")
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.app_password)

    def send_email(self, receiver_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        self.server.sendmail(self.sender_email, receiver_email, msg.as_string())
        print('Mail sent successfully!')

    def close_connection(self):
        self.server.quit()
        print('SMTP connection closed.')


# Example usage:
if __name__ == "__main__":
    receiver_email = "receiver@gmail.com"  # Replace with the recipient's email
    subject = "Test Email"
    message = "Hello, this is a test email sent from Python!"

    email_api = EmailAPI()
    email_api.send_email(receiver_email, subject, message)
    email_api.close_connection()
