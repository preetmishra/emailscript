import smtplib 

EMAIL_ADDRESS = '__yourEmailAddress__'
EMAIL_PASS = '__yourPassword__'

# mail server and port no as parameters

with smtplib.SMTP('smtp.gmail.com', 587) as smtp :
    smtp.ehlo() # identifies ourselves with the mail server that we are using
    # command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    smtp.starttls() # encryptes our traffic
    # It indicates, that the client wants to upgrade existing, insecure connection to a secure connection using SSL/TLS cryptographic protocol
    smtp.ehlo() # reidentifying ourselves

    # logging in to use our e-mail
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    
    subject = 'Up for a coffee?'
    body = 'How about a coffee this weekend?'

    msg = f'Subject: {subject}\n\n{body}' # we have to format the message accordingly

    # format for sendmail that we are using here is sendmail(sender, reciever, message)
    smtp.sendmail(EMAIL_ADDRESS, '__receiverEmail__', msg)
    
