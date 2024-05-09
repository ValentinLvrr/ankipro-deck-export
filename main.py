from config import authorization
import requests

api = 'https://api.ankipro.net/api'
deck_url = api + '/decks/{}'
notes_url = api + '/notes?deck_id={}'
headers = {'authorization': authorization}


def json_to_csv(json):
    return '\n'.join(f"{c['fields']['front_side'].replace(',', '.')},{c['fields']['back_side'].replace(',', '.')}" for c in json)


class Deck:
    def __init__(self, deck_id) -> None:
        self.name = requests.get(deck_url.format(deck_id),
                                 headers=headers).json()['decks'][0]['name']
        self.csv = json_to_csv(requests.get(notes_url.format(
            deck_id), headers=headers).json())
        pass


if __name__ == '__main__':
    deck_id = input('deck url: ').split('/')[-1]
    deck = Deck(deck_id=deck_id)

    open(f'{deck.name}.csv', 'w+', encoding='utf-8').write(deck.csv)
    print(f'saved as "{deck.name}.csv"')
