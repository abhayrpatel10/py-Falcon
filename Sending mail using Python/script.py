import smtplib

sender=''#sender's mail id
reciever=''#reciever's mail id
msg='Hello, World'

username=''
password=''

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()

server.login(username,password)
server.sendmail(sender,reciever,msg)
print("message sent successfully")



