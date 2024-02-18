from config import authorization
import requests

api = 'https://api.ankipro.net/api'
deck_url = api + '/decks/{}'
notes_url = api + '/notes?deck_id={}'
headers = {'authorization': authorization}


def get_deck_name(deck_id):
    return requests.get(url=deck_url.format(deck_id),
                        headers=headers).json()['decks'][0]['name']


def get_json_deck(deck_id):
    return requests.get(url=notes_url.format(deck_id), headers=headers).json()


def get_csv_from_json(json_deck):
    return '\n'.join(f"{c['fields']['front_side'].replace(',', '.')},{c['fields']['back_side'].replace(',', '.')}" for c in json_deck)


if __name__ == '__main__':
    deck_id = input('deck id: ')

    deck_name = get_deck_name(deck_id=deck_id)
    json_deck = get_json_deck(deck_id=deck_id)
    csv_deck = get_csv_from_json(json_deck=json_deck)

    open(f'{deck_name}.csv', 'w+', encoding='utf-8').write(csv_deck)
    print(f'saved as: {deck_name}.csv')
