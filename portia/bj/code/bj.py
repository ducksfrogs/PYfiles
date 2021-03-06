
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', "Three", 'Four', 'Five', 'Six','Seven','Eight','Nine','Ten','Jack', 'Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4,'Five':5,'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):

        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()

        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace'
        self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.ace -= 1

class Chips:
    def  __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except :
            print("enter integer")
        else:
            if chips.bet > chips.total:
                print("sorry")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand H or S')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("deares s turn")
            playing = False

        else:
            print("h or s")

def show_shome(player, dealer):
    pass

def player_busts(player, dealer, chips):
    print("BUrst ")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("player wins")
    chips.win_bet()

def dealer_burst(player, dealer, chips):
    print("dealer bursted")
    chips.win_bet()

def dealer_wins(player,dealer, chips):
    print("BURST player")
    chips.lose_bet()

def push(player, dealer):
    print("push")


while True:

    print("BJ")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
