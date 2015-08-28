import smtplib
from email.mime.text import MIMEText

email_username = 'whatev@gmail.com'
email_password = 'pass'
phone_number = 'phonenumber@txt.att.net'
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

def sendText(message,pn=phone_number,user=email_username,pw=email_password,smtp=s):
	message = MIMEText(message)	
	s.login(user, pw)
	s.sendmail(user, pn, message.as_string())
	

