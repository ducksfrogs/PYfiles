values = {'Two':2, 'Three':3, 'Four':4,'Five':5,'Six':6, 'Seven':7, 'Eight':8,
'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



import random

suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', "Three", 'Four', 'Five', 'Six','Seven','Eight','Nine','Ten','Jack', 'Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4,'Five':5,'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit



two_heart = Card("Hearts", "Two")



print(two_heart)


values.get("Two")


values[two_heart.rank]


two_heart.rank


three_of_clubs = Card("Club", 'Three')


three_of_clubs.suit


three_of_clubs.value


two_heart.value



