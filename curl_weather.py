import requests

r = requests.get('https://api.brightsky.dev/weather?lat=52&lon=7.6&date=2021-02-24')
#r.json()
print(r.json)
info = r.text
print (info)
#print("werte", weather["timestamp"])
for key, value in r.text.items():
    print (key, value)