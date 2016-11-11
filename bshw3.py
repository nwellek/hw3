# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#basic beatiful soup format wiht baseurl
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
f = open('bshw3.html', "w")
soup = BeautifulSoup(r.text, "lxml")


#finds all items that are "students and then replaces it with AMAZING student"
for item in soup.find_all(text = re.compile("student")):
	word = str(item)
	word = word.replace("student", "AMAZING student")
	item.replaceWith(word)

for img in soup.findAll('img'):
	if img['src'] == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg": #specific current jpg that in then changed to the image of myself
		img['src'] = "Nate.png"
	else:
		img['src'] = "media/logo.png" #all other images changed to picture(logo.png)


my_string = str(soup)


f.write(str(soup)) #writes and completes the soup, saving it to html in the same directory
f.close()