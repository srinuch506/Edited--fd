import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('srinivasaraoch506@gmail.com','bonupgmwzlgfzvfr')
    msg=EmailMessage()
    msg['From']='srinivasaraoch506@gmail.com.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()