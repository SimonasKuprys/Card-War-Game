import csv
import random



class Deck_of_cards:
        
    cards = [{'card': 'ace of spades', 'value': '13'}, {'card': 'king of spades', 'value': '12'},
        {'card': 'queen of spades', 'value': '11'}, {'card': 'jack of spades', 'value': '10'},
        {'card': 'ten of spades', 'value': '9'}, {'card': 'nine of spades', 'value': '8'}, 
        {'card': 'eight of spades', 'value': '7'}, {'card': 'seven of spades', 'value': '6'},
        {'card': 'six of spades', 'value': '5'}, {'card': 'five of spades', 'value': '4'}, 
        {'card': 'four of spades', 'value': '3'}, {'card': 'three of spades', 'value': '2'},
        {'card': 'two of spades', 'value': '1'}, {'card': 'ace of clubs', 'value': '13'}, 
        {'card': 'king of clubs', 'value': '12'}, {'card': 'queen of clubs', 'value': '11'}, 
        {'card': 'jack of clubs', 'value': '10'}, {'card': 'ten of clubs', 'value': '9'}, 
        {'card': 'nine of clubs', 'value': '8'}, {'card': 'eight of clubs', 'value': '7'}, 
        {'card': 'seven of clubs', 'value': '6'}, {'card': 'six of clubs', 'value': '5'},
        {'card': 'five of clubs', 'value': '4'}, {'card': 'four of clubs', 'value': '3'}, 
        {'card': 'three of clubs', 'value': '2'}, {'card': 'two of clubs', 'value': '1'}, 
        {'card': 'ace of diamonds', 'value': '13'}, {'card': 'king of diamonds', 'value': '12'}, 
        {'card': 'queen of diamonds', 'value': '11'}, {'card': 'jack of diamonds', 'value': '10'}, 
        {'card': 'ten of diamonds', 'value': '9'}, {'card': 'nine of diamonds', 'value': '8'}, 
        {'card': 'eight of diamonds', 'value': '7'}, {'card': 'seven of diamonds', 'value': '6'}, 
        {'card': 'six of diamonds', 'value': '5'}, {'card': 'five of diamonds', 'value': '4'}, 
        {'card': 'four of diamonds', 'value': '3'}, {'card': 'three of diamonds', 'value': '2'}, 
        {'card': 'two of diamonds', 'value': '1'}, {'card': 'ace of hearts', 'value': '13'}, 
        {'card': 'king of hearts', 'value': '12'}, {'card': 'queen of hearts', 'value': '11'}, 
        {'card': 'jack of hearts', 'value': '10'}, {'card': 'ten of hearts', 'value': '9'}, 
        {'card': 'nine of hearts', 'value': '8'}, {'card': 'eight of hearts', 'value': '7'},
        {'card': 'seven of hearts', 'value': '6'}, {'card': 'six of hearts', 'value': '5'}, 
        {'card': 'five of hearts', 'value': '4'}, {'card': 'four of hearts', 'value': '3'}, 
        {'card': 'three of hearts', 'value': '2'}, {'card': 'two of hearts', 'value': '1'}]
        
    def random_deck(self):
        shuffled_cards = random.sample(self.cards,len(self.cards))
        return shuffled_cards
        
        
        
def main():
    ...
    c = Deck_of_cards()
    cc = c.random_deck()
    print(cc)
    # read_all_cards()
    


# def random_deck(cards):
#     # x = [1,2,3,4,5,6]
#     # shuffled_cards = random.shuffle(x)
#     # return shuffled_cards
#     x = [1,2,3,4,5,6]
#     shufled = random.sample(cards, len(cards))
#     return shufled



def read_all_cards():
    cards = []
    with open("all_cards.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cards.append(row)
    print(cards)        
        
if __name__ == "__main__":
    main()
