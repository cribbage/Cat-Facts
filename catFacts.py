#!/usr/bin/env python
import urllib.request 
from texter import *
import time

def getRandomWord():
	req = urllib.request.Request("https://www.randomlists.com/random-words")
	resp = urllib.request.urlopen(req).read()
	for x in range(0,len(resp)-51,50):
		line = str(resp[x:x+50])
		if "<span class='crux'" in line:
			return line[line.find('crux')+5:line.find('</span>')]

def catFacts(pn):
	cf = open("catfacts.txt", "r")
	lines = cf.readlines()
	for line in lines:
		sendText("Thanks for signing up for CatFacts! You have elected to receive a fact about cats via text once every minute! Reply '" + getRandomWord()+ "' to stop further catfacts!",pn)
		sendText(line,pn)
		time.sleep(60)

catFacts(input("Phone Number: "))
