import csv
import random



class Deck_of_cards:
    def __init__(self,deck):
        self.deck = deck
        
    def random_deck(self):
        shuffled_cards = random.sample(self.deck,len(self.deck))
        split = (shuffled_cards[:26],shuffled_cards[26:])
        return split

class Hand:
    def __init__(self,cards):
        self.cards = cards
        
    def add(self,card_to_add):
        self.cards.append(card_to_add)
        
        
    def remove(self):
        card = self.cards.pop(0)
        return card

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def __str__(self):
        return f"{self.name}({self.hand})"
    
    def playing_card(self):
        card = self.hand.remove()
        return card
    def war_declared(self):
        war_cards = []
        if len(self.hand.cards) <2:
            return self.hand.cards
        else:    
            for x in range(2):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        
    def has_cards(self):
        if bool(self.hand.cards):
            return bool(self.hand.cards)
        else:
            print("End of the game")
    
        
        
        
def main():
    deck = Deck_of_cards(all_cards())
    half1,half2 = deck.random_deck()
    name1 = "Player one"
    player1 = Player(name1,Hand(half1))
    name2 = "Player two"
    player2 = Player(name2,Hand(half2))

    while player1.has_cards() and player2.has_cards():
        table = []
        
        p1_card = player1.playing_card()
        p2_card = player2.playing_card()
        
        table.append(p1_card)
        table.append(p2_card)
        print(f"Player one card is {p1_card['card']}.")
        print(f"Player two card is {p2_card['card']}.\n")
        
        
        if int(p1_card["value"]) == int(p2_card["value"]):
            war_war_war(table,player1,player2)
                    

        elif int(p1_card["value"]) > int(p2_card["value"]):
            print("Player one won")
            player1.hand.add(p1_card)
            player1.hand.add(p2_card)
            
        elif int(p1_card["value"]) < int(p2_card["value"]):
            print("Player two won")
            player2.hand.add(p2_card)
            player2.hand.add(p1_card)
            

def war_war_war(table,player1,player2):
    while True:
        table.extend(player1.war_declared())
        table.extend(player2.war_declared())
        p1_war_card = table[-3]
        p2_war_card = table[-1]

        if int(p1_war_card["value"]) > int(p2_war_card["value"]):
            player1.hand.cards.extend(table)
            break
        elif int(p1_war_card["value"]) < int(p2_war_card["value"]):
            player2.hand.cards.extend(table)
            break
        else:
            p1_war_card = table[-3]
            p2_war_card = table[-1]


def all_cards():
    cards = []
    with open("deck.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cards.append(row)
    return cards        
if __name__ == "__main__":
    main()
