import smtplib

from email.message import EmailMessage
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


message = MIMEMultipart()
message["from"] = "name"
message["to"] = "email of recever"
message["subject"] = "whatever"


def emailsender(filename):
    with open(filename, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(filename)
            )
        # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
    message.attach(part)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email", "password")
        smtp.send_message(message)
        print("all done!")


emailsender("some file name")