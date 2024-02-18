from config import authorization
import requests

deck_url = 'https://api.ankipro.net/api/decks/{}'
notes_url = 'https://api.ankipro.net/api/notes?deck_id={}'
headers = {'authorization': authorization}


def get_deck_name(deck_id):
    url = deck_url.format(deck_id)
    res = requests.get(url=url, headers=headers)
    return res.json()['decks'][0]['name']


def get_json_deck(deck_id):
    url = notes_url.format(deck_id)
    res = requests.get(url=url, headers=headers)
    return res.json()


def generate_csv_content_from_json(json_deck):
    content = ''
    for card in json_deck:
        front_side = card['fields']['front_side'].replace(',', '.')
        back_side = 'empty' if not card['fields']['back_side'] else card['fields']['back_side'].replace(
            ',', '.')
        content += '\n' + front_side + ',' + back_side
    return content


if __name__ == '__main__':
    deck_id = input('deck id: ')
    deck_name = get_deck_name(deck_id=deck_id)
    json_deck = get_json_deck(deck_id=deck_id)
    csv = generate_csv_content_from_json(json_deck=json_deck)
    open(f'{deck_name}.csv', 'w+', encoding='utf-8').write(csv)
    print(f'saved as: {deck_name}.csv')
