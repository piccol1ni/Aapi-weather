import requests


def main():
    places = ['Лондон', 'Шереметьево', 'Череповец']

    payload = {
        'lang' : 'ru',
        'nTqM' : '',
    }

    for place in places:
        url = 'https://wttr.in/{}'.format(place)

        response = requests.get(url, params=payload)
        response.raise_for_status()

        print(response.text)


if __name__ == '__main__':
    main()
