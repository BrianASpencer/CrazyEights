from random import randint

class Game:
    # constructor
    def __init__(self, _number):
        self.number = _number
        self.deck = Deck(1)
        self.dPile = Deck(0)
        p = random.randint(0, 1)
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
    # constructor
    def __init__(self, _name, _id):
        self.id = _id
        self.name = _name
        self.hand = []

    def handLength(self):
        return len(self.hand)

    def showHand(self):
        for card in self.hand:
            card.showCard()

class Deck:
    # constructor
    def __init__(self, _type):
        self.cards = []
        self.type = _type
        if self.type == 1:
            self.buildDeck()

    def buildDeck(self):
        for i in ["C", "D", "H", "S"]:
            for j in range(1, 14):
                self.cards.append(Card(str(j), i))
        self.shuffle()

    def shuffle(self):
        for i in range(len(deck) -1, 0, -1):
            swap = random.randint(0, i)
            self.deck[i], self.deck[swap] = self.deck[swap], self.deck[i]

    def recharge(self, dPile):
        for i in range(len(dPile) -1, 0, -1):
            self.cards.append(dPile.cards[i])
            dPile.cards.pop()

    def isEmpty(self):
        return(len(self.cards)==0)

    def topValue(self):
        if not self.isEmpty():
            return self.cards[len(self.cards)-1].value
    def topSuite(self):
        if not self.isEmpty():
            return self.cards[len(self.cards)-1].suit

    def draw(self, dPile):
        if not isEmpty:
            card = self.cards.pop()
        else:
            self.recharge(dPile)
            card = self.cards.pop()
        return(card)


class Card:
    # constructor
    def __init__(self, _value, _suit):
        self.suit = _suit
        self.value = _value

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
