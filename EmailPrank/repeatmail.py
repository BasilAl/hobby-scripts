import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
import time

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate():
    temp = ''
    for i in range(2):
        for i in range(3):
            temp += random.choice(digits)
        for i in range(3):
            temp += random.choice(letter)
    temp += '@hpeprint.com'
    return temp


for i in range(80):
    email_user = '******@gmail.com'
    email_password = '*******'

    subject = 'Print'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['Subject'] = subject

    body = ''
    msg.attach(MIMEText(body, 'plain'))

    filename = 'printr.png'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

# print(type(msg))
# print(msg)

    print("Batch : {}...".format(i))
    for _ in range(25):
        server.sendmail(email_user, generate(), text)
    print("Batch : {} sent.".format(i))
    server.quit()
    time.sleep(60)
