import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
from email.message import EmailMessage


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


email_user = '****************@gmail.com'
email_password = '******************'
email_send = '***************@gmail.com'

subject = 'Print'

# msg = MIMEMultipart()
msg = EmailMessage()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
msg.make_mixed()
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
server.sendmail(email_user, 'aliftiras.v@gmail.com', text)

'''
for i in range(25):
    server.sendmail(email_user, generate(), text)
server.quit()
'''
