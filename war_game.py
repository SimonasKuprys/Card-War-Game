import csv

class Deck_of_cards:
    def __init__(self, cards):
        self.cards = cards
        
def main():
    read_all_cards()




def read_all_cards():
    cards = []
    with open("all_cards.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cards.append(row["card"])
    print(cards)        
        
if __name__ == "__main__":
    main()
