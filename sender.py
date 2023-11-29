from dotenv import load_dotenv
import os
import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Get email credentials from environment variables
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
default_email = "sureshfizzy0503@gmail.com"

# Set up SMTP server
smtp_server = "smtpout.secureserver.net"
smtp_port = 587
sender_email = email_user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        recipient_email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Compose email
        email_body = MIMEMultipart()
        email_body['From'] = sender_email
        email_body['To'] = recipient_email
        email_body['Bcc'] = default_email
        email_body['Subject'] = subject

        # Iterate over all form fields dynamically
        for field_name, field_value in request.form.items():
            if field_name not in ['email', 'subject', 'message']:
                # Exclude specific fields (e.g., email, subject, message)
                label = field_name.capitalize()  # Use field name as label
                email_body.attach(MIMEText(f"{label}: {field_value}\n", 'plain'))

        # Add the main message
        email_body.attach(MIMEText(f"\nMessage:\n{message}\n", 'plain'))
        # Connect to SMTP server with TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Log in to the email account
            server.login(email_user, email_password)
            # Send email
            server.sendmail(sender_email, [recipient_email , default_email], email_body.as_string())

        return render_template('thank_you.html')

    return "error sending email"

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)

