import requests
from datetime import datetime
import smtplib
import time
MY_LAT =28.704060
MY_LONG = 77.102493
# my_email="mohitthakur9901@gmail.com"
# password="iizjbdphnbiuqybj"
def _iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -2 <= iss_latitude <= MY_LAT +2 and  MY_LONG -2 <= iss_longitude <= MY_LONG +2:
        return True
def night():
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

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(600)
    if _iss_overhead and night:
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:LOOK UP IN THE SKY\n\n you can see the international space station now"
                            )


