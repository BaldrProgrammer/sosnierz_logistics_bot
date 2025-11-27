import smtplib
from email.message import EmailMessage

def send_email(smtp_host, smtp_port, username, password, sender, to, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)
