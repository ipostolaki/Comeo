    def send_ssl_mail()
    # Define to/from
    sender = 'contact@comeo.org.md'
    recipient = 'ilia.ravemd@gmail.com'
    
    # Create message
    msg = MIMEText("Message text")
    msg['Subject'] = "Sent from python"
    msg['From'] = sender
    msg['To'] = recipient

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login('contact@comeo.org.md', 'Definepass1')
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()