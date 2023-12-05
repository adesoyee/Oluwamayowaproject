# 1) Import the "Card" module from the "PlayingCards" package,
# and alias it as "cards"
from PlayingCards import Card as cards

import random as rand

# 2) Take a look at the "Card" class from the "Card" module
# notice the attributes & the methods of this class
# we store the "suit_names" and "rank_names" in a list
# therefore, we can use the indices of this list to select
# the suit and rank.
# we assign the suit and rank from the "__init__" method
# these will simply be integers that we choose
# e.g. index 0 in suit_names is Clubs
# index 4 in rank_names is 4

# create 7 cards and save them into a new list
# use a for-loop to create these 7 cards, and ensure
# that each suit and rank is completely random
# using the 'randint' function from the 'random' package

# https://docs.python.org/3/library/random.html#random.randint
cards_list = []
for _ in range(7):
    suit_index = rand.randint(0, len(cards.suit_names) - 1)
    rank_index = rand.randint(0, len(cards.rank_names) - 1)
    new_card = cards(suit_index, rank_index)
    cards_list.append(new_card)

for card in cards_list:
    print(f"Card: {cards.suit_names[card.suit]} {cards.rank_names[card.rank]}")
