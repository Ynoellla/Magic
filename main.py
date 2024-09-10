import requests

def get_card_info(card_name):
    # Replace spaces in the card name with "+" for the query
    query_name = card_name.replace(' ', '+')

    url = f'https://api.scryfall.com/cards/named?fuzzy={query_name}'
    response = requests.get(url)

    if response.status_code == 200:
        card_data = response.json()
        card_name = card_data['name']
        card_type = card_data['type_line']
        card_price = card_data['prices']['usd'] or 'Price not available'
        card_oracle_text = card_data.get('oracle_text', 'No oracle text available')
        print(f"Name: {card_name}")
        print(f"Type: {card_type}")
        print(f"Price: ${card_price}")
        print(f"Oracle Text: {card_oracle_text}")
    else:
        print(f"Card not found or API error (Status code: {response.status_code})")

card_name_input = input("Enter the card name: ")
get_card_info(card_name_input)
