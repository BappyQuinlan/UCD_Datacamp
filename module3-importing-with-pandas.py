import requests

#request=requests.get('http://api.open-notify.org/iss-now.json')
request=requests.get('http://api.open-notify.org/astros.json')

print(request.status_code)

print(request.text)

data=request.json()

print(data['number'])


for p in data['people']:
    print(p['name'])