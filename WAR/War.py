#CARD CLASS
#SUIT,RANK,VALUE
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.values = values[rank]

	def __str__(self):
		return self.rank + " of " +self.suit
'''

two_hearts = Card("Hearts", "Two")

print(two_hearts.values)

three_of_clubs = Card("Clubs","Three")
print(three_of_clubs.values)
'''
#DECK CLASS
class Deck:
    
    def __init__(self):
        self.all_cards = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
    	return self.all_cards.pop()    
   
'''
new_deck = Deck()
new_deck.shuffle()
my_card = new_deck.deal_one()

print(my_card)
print(len(new_deck.all_cards))
for card_object in new_deck.all_cards:
	print(card_object)
'''
#PLAYER CLASS
class Player:
	def __init__(self,name):
		self.name = name
		self.all_cards = []

	def	remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type ([]):
			#List of multiple card objects
			self.all_cards.extend(new_cards)
		else:
			#single card object
			self.all_cards.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards.'
'''
new_player = Player('jose')
new_player.add_cards([my_card,my_card,my_card])		
print(my_card)
new_player.remove_one()
print(new_player)
'''
#GAME SETUP













