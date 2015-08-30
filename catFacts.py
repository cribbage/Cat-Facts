#!/usr/bin/env python3

import argparse
import sys

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
				
def getEmailFromPN(pn):
	with open("numtoemail.txt", "r") as numsList:
		print("Checking for number...")
		for line in numsList:
			num, email = line.split()
			if pn == num:
				print("Number found.")
				return email

def sendText(smtp_object, message, email):
	message = MIMEText(message)
	try:
		with open("gmailaccounts.txt", "r") as gmailAccounts:
			for line in gmailAccounts:
				username, password = line.split()
				smtp_object.login(username, password)
	except SMTPAuthenticationError:
		sys.exit("Invalid username/password!")
	print("Sending email...")
	smtp_object.sendmail(email_username, email, message.as_string())

def catFacts(pn):
	victimEmail = getEmailFromPN(pn)
	if not victimEmail:
		sys.exit("Victim number not in text file!")
	s = SMTP('smtp.gmail.com:587')
	s.starttls()
	with open("catfacts.txt", "r") as cf:
		for line in cf:
			sendText(s, "Thanks for signing up for CatFacts! You have elected to receive a fact about cats via text once every minute! Reply '" + getRandomWord() + "' to stop further catfacts!", victimEmail)
			sendText(s, line, victimEmail)
			sleep(3)

catFacts(input("Phone Number: "))
