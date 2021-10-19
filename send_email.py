from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    # from_email="testudemy57@outlook.com"
    # from_password="Password!24"
    to_email=email

    subject="Height Data"
    message="Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated from the heights of <strong>%s</strong> people" % (height,average_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    outlook=smtplib.SMTP('smtp-mail.outlook.com',587)
    # outlook=smtplib.SMTP('smtp.gmail.com',587)
    outlook.ehlo()
    outlook.starttls()
    outlook.login(from_email,from_password)
    outlook.send_message(msg)
    print("sent email")