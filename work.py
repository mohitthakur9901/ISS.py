import requests
from datetime import datetime
my_lat=28.704060
my_lng=77.102493
parameter={
    "lat":my_lat,
     "lng":my_lng,
     "formatted":0,
}
website=requests.get(url=" https://api.sunrise-sunset.org/json",params=parameter)
website.raise_for_status()
data=website.json()["results"]["sunrise"].split("T")[1].split(":")[0]
data1=website.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(data,data1)










