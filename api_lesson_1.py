import requests

url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
response = requests.get(url)

if not response.ok:
    raise requests.exceptions.HTTPError(response=response)

print(response.text)