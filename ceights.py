from random import randint

class Game:
    # constructor
    def __init__(self, _number, id1, id2):
        self.number = _number
        self.deck = Deck(1)
        self.dPile = Deck(0)
        p = random.randint(0, 1)
        if p == 1:
            self.p1 = Player("Player 1", id1)
            self.p2 = Player("Player 2", id2)
        else:
            self.p1 = Player("Player 1", id2)
            self.p2 = Player("Player 2", id1)
        self.startGame()

    def startGame(self):
        
        

class Player:
    # constructor
    def __init__(self, _name, _id):
        self.id = _id
        self.name = _name
        self.hand = []

    def handLength(self):
        return len(self.hand)

    def draw(self, deck):
        self.hand.append(deck.drawCard())

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
                self.cards.append(Card(j, i))
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



while True:
    openingCard = deck.pop()
    if openingCard.startswith('8'):
        deck.append(openingCard)
    else:
        break


discardPile.append(openingCard)

print(deck)
print(discardPile)

turn = r = random.randint(0, 1)

if turn == 0:
    p1 = Player()
    p1.turn = True
    p2 = Player()
else:
    p2 = Player()
    p2.turn = True
    p1 = Player()


if p1.turn:
    while True:
        if move == "DC":
            draw = deck.pop()
            p1.hand.append(draw)
        elif validMove(p1.hand[move], openingCard[len(openingCard)-1]):
            openingCard.append(p1.hand[move])
            p1.hand.remove(p1.hand[move])
            break
elif p2.turn:
    while True:
        if len(deck) == 0:
        if move == "DC":
            draw = deck.pop()
            p2.hand.append(draw)
        elif validMove(p1.hand[move], openingCard[len(openingCard)-1]):
            openingCard.append(p2.hand[move])
            p2.hand.remove(p2.hand[move])
            break





