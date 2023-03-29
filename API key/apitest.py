import json
import requests

response = (requests.get("https://api.postcodes.io/postcodes/" + "##############    podtcode     #############")).json()
properties = response['result']
country = properties["country"]
city = properties["nuts"]
n = len(city)-1
for i in range(n):
    if city[i] == " ":
        w1 = city[:i]
        w2 = city[i + 1:]
        sp = "-"
        city = (w1 + sp + w2)
urr = "https://api.openweathermap.org/data/2.5/weather?"
apid = "cd28d9c345ee23ecdde5f9ed8d18a388"
url = urr + "appid=" + apid + "&q=" + city
info = requests.get(url).json()
stats = info["weather"]
w_cond = stats[0]
weath = w_cond["description"]
conditions = info["main"]
temp_in_k = conditions["temp"]
feels_like = conditions["feels_like"]