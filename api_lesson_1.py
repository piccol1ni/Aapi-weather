import requests


places = ['Лондон', 'Шереметьево', 'Череповец']

def main():
    payloads = {
        'lang' : 'ru',
        'nTqM' : '',
    }

    for place in places:
        url = 'https://wttr.in/{}'.format(place)

        response = requests.get(url, params=payloads)
        response.raise_for_status()

        print(response.text)

if __name__ == '__main__':
    main()
