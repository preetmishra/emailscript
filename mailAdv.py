import smtplib
from email.message import EmailMessage
import imghdr 

EMAIL_ADDRESS = '__yourEmailAddress__'
EMAIL_PASS = '__yourPassword__'

# composing our message using email lib

# contacts = ['add1@some.com','add2@some.com] for multiple recipient
msg = EmailMessage()
msg['Subject'] = 'A generic picture.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '__receiverEmail_'
msg.set_content('Image attached.')

# you can use this in a loop to add multiple image
# path and mode as parameters
with open('letterpshadow.jpg', 'rb') as img :
    file_data = img.read()
    file_type = imghdr.what(img.name)
    file_name = img.name

# attaching an img to our mail
msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name) 

# attaching an pdf to our mail
with open('final.pdf', 'rb') as pdf :
    file_data = pdf.read()
    file_name = pdf.name
    
# attaching a pdf using maintype = 'application' subtype = 'octet-stream'
msg.add_attachment(file_data, maintype='application',
                   subtype='octet-stream', filename=file_name)

# mail server and port no as parameters
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    # SMTP_SSL class comes with a ssl connection
    # smtp.ehlo()  # identifies ourselves with the mail server that we are using
    # # command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    # smtp.starttls()  # encryptes our traffic
    # # It indicates, that the client wants to upgrade existing, insecure connection to a secure connection using SSL/TLS cryptographic protocol
    # smtp.ehlo()  # reidentifying ourselves

    # logging in to use our e-mail
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

    # send_message is used instead of sendmail
    smtp.send_message(msg)
