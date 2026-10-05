import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reply_email(to_email, subject, body):
    # Simulated email dispatch or configured SMTP server relay
    try:
        msg = MIMEMultipart()
        msg['From'] = "example@gmail.com"
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        # If SMTP config is provided, send via server
        return True
    except Exception:
        return False
