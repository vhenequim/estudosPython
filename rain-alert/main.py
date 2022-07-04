import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "fa29c8e584b7ebbe6b4e59a22361d421"
MY_LAT = -22.906847
MY_LON = -43.172897
account_sid = "ACf9a2ecb8048415f27dbb54264c60e63d"
auth_token = "0237f6fd4dde6da35ee3f5f01d34e67a"
jason = "+5519999254477"
vini = "+5541991179474"

parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': API_KEY,
    'exclude': "current,minutely,daily"
}

response = requests.get(url=OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="""Repolho roxo: entenda quais as vantagens e beneficios para seu corpo! Acesse no instagram: repolhoroxo""",
        from_='+18455390943',
        to='+556199452558'
    )
    print(message.status)

# hourly_weather = []
# for n in range(7, 19):
#     hourly_weather.append(weather_data["hourly"][n]["weather"][0]["id"])
# print(hourly_weather)
# print(weather_slice)

