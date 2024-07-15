import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('Sender's Email_id','Password')
***
Generate an App Password:
Go to your Google Account's security settings (https://myaccount.google.com/security).
Under "Signing in to Google," find "App passwords."
Select "Mail" as the app and your device type (e.g., "Other (Custom name)").
Generate the password and copy it.
***

server.sendmail('receiver email','hello')
print('mail sent')
