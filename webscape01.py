from bs4 import BeautifulSoup
import requests

allUserAgents = []

Chrome = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/').text
Firefox = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/firefox/').text
IE = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/internet-explorer/').text
Opera = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/opera-mini/').text
Safari = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/safari/').text
UC = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/uc-browser/').text


Chromesoup = BeautifulSoup(Chrome, 'lxml')
Firefoxsoup = BeautifulSoup(Firefox, 'lxml')
IEsoup = 	 BeautifulSoup(IE, 'lxml')
Operasoup  = BeautifulSoup(Opera, 'lxml')
Safarisoup = BeautifulSoup(Safari, 'lxml')
UCsoup =    BeautifulSoup(UC, 'lxml')



userAgents = []
for match in Chromesoup.find_all('td', class_='useragent'):
	userAgent = match.a.text
	userAgents.append(userAgent)
allUserAgents.extend(userAgents[:4])

for match in Firefoxsoup.find_all('td', class_='useragent'):
	userAgent = match.a.text
	userAgents.append(userAgent)
allUserAgents.extend(userAgents[:4])


print(allUserAgents)




