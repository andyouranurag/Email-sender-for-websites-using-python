# Email API using Python

## Overview
This project provides a simple Python-based email API that allows you to send emails using Gmail's SMTP server securely with environment variables.

## Features
- Uses Gmail's SMTP server
- Secured with environment variables
- Sends emails with subject and message
- Simple and reusable class-based implementation

## Requirements
- Python 3.x
- A Gmail account with App Password enabled
- The following Python packages:
  - `smtplib`
  - `email`
  - `python-dotenv`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/email-api.git
   cd email-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add:
   ```env
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_APP_PASSWORD=your_app_password
   ```

## Usage
1. Import and initialize the API:
   ```python
   from email_api import EmailAPI
   
   email_api = EmailAPI()
   email_api.send_email("receiver@gmail.com", "Test Subject", "Hello, this is a test email.")
   email_api.close_connection()
   ```

## Setting Up Gmail App Password
1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification**.
3. Generate an **App Password** under "Signing in to Google" > "App Passwords".
4. Use the generated password in the `.env` file.
   OR
***
Generate an App Password:
Go to your Google Account's security settings (https://myaccount.google.com/security).
Under "Signing in to Google," find "App passwords."
Select "Mail" as the app and your device type (e.g., "Other (Custom name)").
Generate the password and copy it.
***

## License
This project is licensed under the MIT License.



