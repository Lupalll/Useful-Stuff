import requests
from bs4 import BeautifulSoup



### Buld query ###

URL = input("bitte url angeben: ")

htmlPage = requests.get(URL)

BeautifulSoup = BeautifulSoup(htmlPage.content, "html.parser")



### parse the results ###

results = BeautifulSoup.find(id = "cnt-with-location-attributes")

currentLocation = results.find("h2", class_ = "delta text--white mb--")

currentTemp = results.find("div", class_="delta rtw_temp")

currentConditions = results.find("span", class_ = "text--small rtw_weather_txt mb--")


### Printing out the results ###
#print(currentTemp)

print("Stadt: " + currentLocation.text)
print("Temparatur: " + currentTemp.text)
print("Jetztige Wetterlage: " + currentConditions.text)
