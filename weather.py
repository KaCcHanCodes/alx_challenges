#import the library Requests
import requests

#set endpoint url
url = "http://api.openweathermap.org/data/2.5/weather?q=enugu,566&APPID=281f2855a128338e99f4066b8e175f52"
weather = requests.get(url)

#Extract information
response = weather.json()
#Print the needed information by specifying their respective keys
print(response['name'], response['weather'])