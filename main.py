import tkinter as tk
from tkinter import messagebox
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

def search_card():
    card_name = card_entry.get()
    if card_name:
        get_card_info(card_name)
    else:
        messagebox.showwarning("Input Error", "Please enter a card name.")

root = tk.Tk()
root.title("Scryfall Card Search")
root.geometry("300.150")

card_label = tk.Label(root, width=30)
card_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_card)
search_button.pack(pady=10)

root.mainloop()
