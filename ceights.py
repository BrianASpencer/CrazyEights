# Brian Spencer
# CSC 460
# 2/6/2020

class Game:
    # constructor for our game object
    # attributes include:
    # which game we're on
    # a deck
    # a discard pile
    # each player
    # the current suit and value
    # and starting the game
    def __init__(self, _number):
        self.number = _number
        self.deck = Deck(1)
        self.dPile = Deck(0)
        self.p1 = Player("Player 1", id1)
        self.p2 = Player("Player 2", id2)
        self.currSuite = ""
        self.currValue = ""
        self.startGame()

    def startGame(self):
        #need to make discard pile iwth one faceup card
        #if its an 8, reshuffle it into deck and pick another
        #initialize value for currSuite and currValue
        fCard = self.deck.cards.pop()
        if fCard.value == "8":
            self.deck.cards.append(fCard)
            self.deck.shuffle()
            while True:
                fCard = self.deck.cards.pop()
                if fCard.value != "8":
                    break
        self.dPile.cards.append(fCard)
        self.currValue = self.dPile.topValue()
        self.currSuite = self.dPile.topSuite()

    # checking whether or not a player's move is valid
    # checks agaisnt their hand (if their hand doesn't contian that card, then they didnt make a valid move)
    # also allows them to draw
    # a card that's an 8, matches the current suit, or current value is a valid card to play
    def isValidMove(self, player, move):
        if move.upper() == "D":
            player.hand.append(self.deck.cards.pop())
            return True
        for i in range(0, player.handLength()):
            if player.hand[i] == move:
                #if they play an 8, they must choose a new suit
                if player.hand[i].value == "8":
                    self.dPile.cards.append(hand[i])
                    player.hand.remove(player.hand[i])
                    self.currValue = "8"
                    flag = True
                    # need to get the new suit after a player plays an 8
                    while flag:
                        suits = ["C", "D", "H", "S"]
                        s = input('Enter the new suit (C, D, H, S): ')
                        if len(s) == 1:
                            for i in range(0, len(suits)):
                                if s == suits[i]:
                                    self.currSuite = s
                                    flag = False
                                    break
                #otherwise, the current suit is the suit of the played card
                elif player.hand[i].suit == self.currSuite:
                    self.dPile.cards.append(hand[i])
                    player.hand.remove(player.hand[i])
                    self.currValue = player.hand[i].value
                    return True
                elif player.hand[i].value == self.currValue:
                    self.dPile.cards.append(hand[i])
                    player.hand.remove(player.hand[i])
                    self.currSuite = player.hand[i].suit
                    return True
        return False
        
        

class Player:
    # constructor for a player
    # attributes include:
    # their id (most likely their ip address)
    # their name (player 1, player 2, etc.)
    # their hand
    def __init__(self, _name, _id):
        self.id = _id
        self.name = _name
        self.hand = []

    # returns the length of the players hand
    # the object of the game is to have no cards in hand
    def handLength(self):
        return len(self.hand)

    #this is so we can display to the player their hand
    def showHand(self):
        for card in self.hand:
            card.showCard()

class Deck:
    # constructor for deck
    # allows you to create a deck or initialize a discard pile (deck with no cards at start)
    # attributes include:
    # cards within the deck
    # the type of deck
    def __init__(self, _type):
        self.cards = []
        self.type = _type
        if self.type == 1:
            self.buildDeck()

    # if we have a normal deck, we need to construct it with 52 cards and then shuffle it
    def buildDeck(self):
        for i in ["C", "D", "H", "S"]:
            for j in range(1, 14):
                self.cards.append(Card(str(j), i))
        self.shuffle()

    # shuffle the deck for various situations
    def shuffle(self):
        for i in range(len(deck) -1, 0, -1):
            swap = random.randint(0, i)
            self.deck[i], self.deck[swap] = self.deck[swap], self.deck[i]

    # shuffling cards from discard pile into the deck once our deck is empty
    def recharge(self, dPile):
        for i in range(len(dPile) -1, 0, -1):
            self.cards.append(dPile.cards[i])
            dPile.cards.pop()
    # returns boolean for whether or not our deck is empty
    def isEmpty(self):
        return(len(self.cards)==0)
    # returns top card of a deck (mostly useful for a discard pile, as this is the current play card)
    def topValue(self):
        if not self.isEmpty():
            return self.cards[len(self.cards)-1].value
    # also useful for a discard pile (to set the current suit)
    def topSuite(self):
        if not self.isEmpty():
            return self.cards[len(self.cards)-1].suit
    # draw from deck -- a valid move
    def draw(self, dPile):
        if not isEmpty:
            card = self.cards.pop()
        else:
            self.recharge(dPile)
            card = self.cards.pop()
        return(card)


class Card:
    # constructor for card
    # attributes include:
    # suit of a card
    # value of a card
    def __init__(self, _value, _suit):
        self.suit = _suit
        self.value = _value

    #this is so we can display a players cards in a more explicit way
    def showCard(self):
        dict = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value > 10 | self.value == 1:
            x = dict[self.value]
        else:
            x = self.value
        if self.suit == "C":
            print(x, " of Clubs")
        elif self.suit == "D":
            print(x, " of Diamonds")
        elif self.suit == "H":
            print(x, " of Hearts")
        else:
            print(x, " of Spades")
