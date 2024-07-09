# import module
import requests as req
import json
import datetime
from tabulate import tabulate

print("\n\n")
print("\t\t\t\t****** Real Time WEATHER FORECAST Data *******\n")

# Taking input from user
cityName = input("Enter City Name : ")
apiID = "1767682c2e246638576d6bf30305baa1"
# Making Request through Url for weather data 
apiurl = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiID}")
# Gettting response from the Url in JSON formate
responsetxt = apiurl.text
# converting into JSON To Dict:
data = json.loads(responsetxt)

# Declearatin of date
date = datetime.datetime.now().strftime("Date : %A %d %B %Y, Time : %I:%S %p, Day number of year : %j")

# Variable Declearation.
Name = data["name"]
Longitude = data["coord"]["lon"]
Latitude = data["coord"]["lat"]
Main = data["weather"][0]["main"]
Description = data["weather"][0]["description"]
Icon = data["weather"][0]["icon"]
Temperature = float("{:.2f}".format(data["main"]["temp"] - 273.15))
feels_like = data["main"]["feels_like"]
temp_min = float("{:.2f}".format(data["main"]["temp_min"] - 273.15))
temp_max = float("{:.2f}".format(data["main"]["temp_max"] - 273.15))
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
sea_level = data["main"]["sea_level"]
grnd_level = data["main"]["grnd_level"]
grnd_level = data["main"]["grnd_level"]
Base = data["base"]
visibility = data["visibility"]
speed  =  data["wind"]["speed"]
deg = data["wind"]["deg"]
# gust = data["wind"]["gust"]
all = data["clouds"]["all"]
# systype = data["sys"]["type"]
cod = data["cod"]
country = data["sys"]["country"]
sunrise= data["sys"]["sunrise"]
sunset =  data["sys"]["sunset"]
timezone = data["timezone"]

mytb = [
    ["Name", Name, "Feels like", feels_like, "Visibility", visibility, "Icon", Icon], 
    ["Country", country, "Min - Temp.", temp_min, "Speed", speed, "cod", cod], 
    ["Latitude", Latitude, "Max - Temp.", temp_max, "Deg", deg,], 
    ["Longitude", Longitude, "Pressure", pressure, "sunrise", sunrise],
    ["Clouds", Main, "Humidity", humidity, "Clouds", all],
    ["Clouds Description",Description, "Sea Level", sea_level, "sunset", sunset],
    ["Temperature", Temperature, "Ground Level", grnd_level, "timezone", timezone],
]

# creating Table header
# head = ["WEATHER","DATA", "WEATHER", "DATA", "WEATHER", "DATA","WEATHER", "DATA"]
# table = tabulate(mytb, headers=head, tablefmt="rounded_grid") ###### With header
table = tabulate(mytb, tablefmt="rounded_grid") # Without header

# display Date
print(f"\n{date}\n")
# display table
print(table)

print("\n\n")