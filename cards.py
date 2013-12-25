import random  # needed for shuffling a Deck

class Card(object):
    #the card has a suit - 's','c','h', 'd'
    # the card has a rank
    
    def __init__(self, r, s):
        self.rank = r
        self.suit = s
        #implement
        #where r is the rank, s is suit
        #return NotImplementedError

    def __str__(self):
        """ Returns the value of the card as a string"""
        return str(self.rank) + "," + str(self.suit)

    def get_rank(self):
        """ Returns the rank of the card"""
        return self.rank

    def get_suit(self):
        """ Return suite of the card"""
        return self.suit


## Note 11-14 is JQK and Ace


class Deck():
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        #correct the code below
        
        self.__deck = []
        
        for i in ("A",2,3,4,5,6,7,8,9,"J","Q","K"):
            #1  is ace
            #11-13 is j,q,k
            
            #heart, spades, clubs, diamond,
            for suit in ("H","S","C","D"):
                self.card = Card(i,suit)
                self.__deck.append(self.card)
                
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        return self.__deck
        
        #for i in range(len(self.deck)):
         #   return self.deck[i] 
        
        #return self.deck
        ##
        #raise NotImplementedError

    def deal(self):
        return self.__deck.pop()
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        #
        #raise NotImplementedError
    
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
        list = []
        for i in range(len(self.__deck)):
            return str(self.__deck[i])
        

       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them 


#object = Card(rank, suit)
