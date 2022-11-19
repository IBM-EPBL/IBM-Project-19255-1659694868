import smtplib
import sendgrid as sg
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "personal expense tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    from_email = Email("tour7107@gmail.com") 
    to_email = To(email) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)
    try:
        sg=SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
   