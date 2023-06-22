import csv
import random

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
        


def main():
    
    deck_all = Deck()
    deck_all.read_file()
    deck_all.shuffle_deck()
    
    print(deck_all.deck)
    
    
    
    



    
if __name__ == "__main__":
    main()