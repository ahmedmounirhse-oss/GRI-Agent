import smtplib
from email.message import EmailMessage
from pathlib import Path

def send_email_smtp(smtp_host, smtp_port, username, password, to, subject, body, attachments=None):
    msg = EmailMessage()
    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    if attachments:
        for path in attachments:
            path = Path(path)
            with open(path, 'rb') as f:
                data = f.read()
            msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=path.name)
    with smtplib.SMTP_SSL(smtp_host, smtp_port) as s:
        s.login(username, password)
        s.send_message(msg)
