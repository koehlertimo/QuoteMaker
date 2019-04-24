#imports
import requests


#GET a Image from Unsplash API
r = requests.get("https://static4.businessinsider.de/image/5a8d786722e6c638008b491f-2400/shutterstock586550951.jpg")

with open('test.png', 'wb') as f:
    f.write(r.content)


#transform it with a black bg

#Resize

#Logo etc.

#GET a random quote

#put Quote on the picture

#save final pictutre