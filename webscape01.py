from bs4 import BeautifulSoup
import requests

Chrome = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/').text
Firefox = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/firefox/').text
IE = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/internet-explorer/').text
Opera = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/opera-mini/').text
Safari = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/safari/').text
UC = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/uc-browser/').text

browsers = [
	"Chromesoup = BeautifulSoup(Chrome, 'lxml')",
	"Firefoxsoup = BeautifulSoup(Firefox, 'lxml')", 
	"IEsoup = 	 BeautifulSoup(IE, 'lxml')", 
	"Operasoup  = BeautifulSoup(Opera, 'lxml')", 
	"Safarisoup = BeautifulSoup(Safari, 'lxml')", 
	"UCsoup =    BeautifulSoup(UC, 'lxml')"

	]

# Chromesoup = BeautifulSoup(Chrome, 'lxml')
# Firefoxsoup = BeautifulSoup(Firefox, 'lxml')
# IEsoup = 	 BeautifulSoup(IE, 'lxml')
# Operasoup  = BeautifulSoup(Opera, 'lxml')
# Safarisoup = BeautifulSoup(Safari, 'lxml')
# UCsoup =    BeautifulSoup(UC, 'lxml')



# for browser in browsers:
# 	print(browser)


UserAgents = []

for browser in browsers:
	browserUserAgents = []
	for match in browser.find_all('td', class_='useragent'):
		browserUserAgent = match.a.text
		browserUserAgents.append(browserUserAgent)
	UserAgents.extend(browserUserAgents[:4])





# userAgents = []
# for match in Chromesoup.find_all('td', class_='useragent'):
# 	userAgent = match.a.text
# 	print(userAgent)
# 	# userAgents.append(userAgent)

# print(userAgents[:4])



