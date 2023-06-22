import csv
import random

class Player:
    def __init__(self, deck):
        self.deck = deck

    def __str__(self):
        return f'{self.deck}'

    def draw_card(self):
        return self.deck.pop(0)

    def add_card(self, cards):
        for card in cards:
            self.deck.append(card)

class Deck:
    def __init__(self):
        self.deck = []

    def read_file(self):
        all_cards = []
        with open("deck.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_cards.append(row)
        self.deck = all_cards

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def split_two(self):
        split_index = len(self.deck) // 2
        first_deck = self.deck[:split_index]
        second_deck = self.deck[split_index:]
        return first_deck, second_deck

def match_cards(player1, player2):
    while True:
        card1 = player1.draw_card()
        card2 = player2.draw_card()
        cards = [card1, card2]
        print(card1['value'])
        if card1['value'] > card2['value']:
            player1.add_card(cards)
        elif card1['value'] < card2['value']:
            player2.add_card(cards)
        elif len(player1.deck) == 0 or len(player2.deck) == 0:
            break
        # elif card1[1] == card2[1]:
        # print(len(player1.deck))
    if len(player1.deck) == 0:
        winner = 'Player 2'
    else:
        winner = 'Player 1'
    print(f'Game concluded! {winner} won!')

def main():

    deck_all = Deck()
    deck_all.read_file()
    deck_all.shuffle_deck()
    deck1, deck2 = deck_all.split_two()
    player1 = Player(deck1)
    player2 = Player(deck2)
    match_cards(player1, player2)

if __name__ == "__main__":
    main()