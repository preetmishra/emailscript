import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = '__yourEmailAddress__'
EMAIL_PASS = '__yourPassword__'

# composing our message using email lib

# contacts = ['add1@some.com','add2@some.com] for multiple recipient
msg = EmailMessage()
msg['Subject'] = 'A generic email.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '__receiverEmail_'
msg.set_content('HTML')

# adding HTML

msg.add_alternative('''
<!DOCTYPE html>
<html>
<body>
<h1> This is a HTML email. </h1>
</body>
</html>
''', subtype = 'html')


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


# for adding a HTML file

# with open('my_HTML_file.html', 'rb') as f:
#     file_data = f.read()
# #print(file_data)
# file_string = file_data.decode(encoding='UTF-8')
# #print("\n\n ::: The file decoded into a string ::: \n\n", file_string)
# msg.add_alternative(file_string, subtype='html')
