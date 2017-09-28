import interface
import pickle
import requests
from bs4 import BeautifulSoup
from datetime import date

def checkupdate(version, day): 
    #if date.today() > day && importversion() > version:
    	pass

    	
def importversion():
	response = requests.get('https://raw.githubusercontent.com/BrandonChupe/onelinergui/master/version.txt')
	html = response.content

	soup = BeautifulSoup(html, 'html.parser')
	return soup.prettify()

def importdate():
    day = pickle.load( open( "lastupdate.p", "rb"))

    return day

def exportdate(day):
    pickle.dump( day, open ( "lastupdate.p", "wb"))


version = .1

checkupdate(version, importdate())

interface.guiloop()
