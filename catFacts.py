#!/usr/bin/env python3

from urllib.request import urlopen
from smtplib import SMTP
from email.mime.text import MIMEText
from time import sleep

email_username = 'daheadofstate@gmail.com'
email_password = 'testing777'

def getRandomWord():
	with urlopen("http://www.randomlists.com/random-words") as resp:
		for line in resp:
			line = str(line)
			if "crux" in line:
				# + 7 to advance past 'crux' and angle brackets
				wordStartIndex = line.find('crux') + 7
				wordEndIndex = line[wordStartIndex:].find('</span>')
				if wordEndIndex == -1:
					continue
				return line[wordStartIndex:wordStartIndex+wordEndIndex]
				
def getEmailFromPN():
	pass

def sendText(smtp_object, message, phone_number):
	message = MIMEText(message)
	smtp_object.login(email_username, email_password)
	smtp_object.sendmail(email_username, phone_number+'@txt.att.net', message.as_string())

def catFacts(pn):
	s = SMTP('smtp.gmail.com:587')
	s.starttls()
	with open("catfacts.txt", "r") as cf:
		for line in cf:
			sendText(s, "Thanks for signing up for CatFacts! You have elected to receive a fact about cats via text once every minute! Reply '" + getRandomWord() + "' to stop further catfacts!", pn)
			sendText(s, line, pn)
			sleep(60)

catFacts(input("Phone Number: "))
