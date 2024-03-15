import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

#getting data using the api
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#writing names of people onto a txt file
file = open("iss.txt","w")
file.write("There are currently "+str(result["number"])+" astronauts on the ISS \n\n")
people = result["people"]
for p in people:
    file.write(p["name"]+" on board \n")

#writing own lat and long
g = geocoder.ip("me")
file.write("\n Your current lat/long is: "+ str(g.latlng))
file.close()

webbrowser.open("iss.txt")

#setup world map
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

#load world map img and assign iss img as turtle
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    #load current status of iss in real time using api
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    #extract iss location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    
    #output lat/lon to terminal
    lat = float(lat)
    lon = float(lon)
    print("Latitude: "+str(lat))
    print("Longitude: "+str(lon))
    
    #update iss location to map
    iss.goto(lon,lat)
    
    #refresh every 5 seconds
    time.sleep(5)
    