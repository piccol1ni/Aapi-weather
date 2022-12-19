import requests


wttr_articles = ['Лондон', 'Шереметьево', 'Череповец']

for article in wttr_articles:
    url = 'https://wttr.in/{}?nTqM&lang=ru'.format(article)

    response = requests.get(url)
    print(url)


    if not response.ok:
        raise requests.exceptions.HTTPError(response=response)

    print(response.text)
