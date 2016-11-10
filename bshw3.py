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


base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
f = open('bshw3.html', "w")
soup = BeautifulSoup(r.text, "lxml")

student = soup.findAll(text = "student")

for item in student:
	txt = re.sub("student", "AMAZING student", item)
	item.replace_with(txt)

for img in soup.findAll('img'):
	if img.get('alt') == None:
		img['src'] = "Nate.png"

for img in soup.find_all("img"):
	img['src'] = "logo.png"

f.write(soup.encode("ascii", "ignore").decode("utf-8"))
f.close()