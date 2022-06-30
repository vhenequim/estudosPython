import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -22.906847
MY_LON = -43.172897
MY_EMAIL = ""
MY_PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LON - 5 <= iss_longitude <= MY_LON + 5 and MY_LAT - 5 <= iss_latitude <= MY_LON + 5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunrise >= int(time_now.hour) >= sunset:
        return True


while True:
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS is on the sky!\n\nLook outside! ISS is on the sky my man!"
            )
    time.sleep(60)