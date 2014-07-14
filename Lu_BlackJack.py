# Mini-project #6 - Blackjack

# import simplegui
import random

# define global varables
global in_play, outcome, score
   
in_play = False
outcome = ""
score = 0



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank    

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

#    def draw(self, canvas, pos):
#        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
#                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
#        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
#                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
    def show(self):
        print self.rank + self.suit
        
                
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = 'Hand contains '
        for card in self.cards:
            s += str(card)+' '
        return s
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        
        for card in self.cards:
            
            value += VALUES[card.get_rank()]
        for card in self.cards:
            if 'A' == card.get_rank():
                if value < 12:
                    value += 10
        return value
    
#    def draw(self, canvas, pos):
#        # draw a hand on the canvas, use the draw method for cards
#        for card in self.cards:
#            card.draw(canvas, [pos[0]+ 100 * self.cards.index(card),pos[1]])
    def show(self):
        for card in self.cards:
            card.show()

        
                        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.deck.append(card)
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
        print self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        s = 'Deck contains '
        for card in self.deck:
            s += str(card)+' '
        return s
   

#define event handlers for buttons
def deal():
    global deck, player_hands, dealer_hands, outcome, in_play, score
    if not in_play:
        deck = Deck()
        deck.shuffle()
    
        player_hands = Hand()
        dealer_hands = Hand()
    
        player_hands.add_card(deck.deal_card())
        dealer_hands.add_card(deck.deal_card())
        player_hands.add_card(deck.deal_card())
        dealer_hands.add_card(deck.deal_card())
        outcome = 'Hit or Stand?'  
        in_play = True
        
    else:
        outcome = "player quit the round"
        score -= 1
        in_play = False
        
def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global deck, player_hands, outcome, in_play, score
    if in_play:
        if player_hands.get_value() < 22:
            player_hands.add_card(deck.deal_card())
            if player_hands.get_value() > 21:
                outcome = "You've busted"
                in_play = False
                score -= 1
       
def stand():    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    
    global deck, dealer_hands, player_hands, outcome, in_play, score
    
    if in_play:
        if player_hands.get_value() > 21:
            outcome = "You've busted"
        else: 
            while dealer_hands.get_value() < 17:
                dealer_hands.add_card(deck.deal_card())
        
            if dealer_hands.get_value() > 21:
                outcome = "Dealer\'s busted, YOU WIN"
                score += 1
            
            elif dealer_hands.get_value() < player_hands.get_value():
                outcome = "YOU WIN"
                score += 1
            
            else:
                outcome = "Dealer Win"
                score -= 1
        in_play = False
    
deal()

def show():
    print "score:  " + str(score)  
