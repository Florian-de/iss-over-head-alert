import requests
from datetime import datetime

MY_LAT = 48.777111
MY_LONG = 9.180770

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Position is within +5 or -5 degrees of the ISS position.
iss_close = False
if int(MY_LAT) in range(int(iss_latitude)-5, int(iss_latitude)+5) and int(MY_LONG) in range(int(iss_longitude)-5, int(iss_longitude)+5):
    iss_close = True
else:
    iss_close = False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time = int(str(time_now).split(" ")[1].split(":")[0])

dark = False
if time < 24:
    if time > sunset:
        dark = True
else:
    if time < sunrise:
        dark = True

if iss_close and dark:
    print("Look up!")




