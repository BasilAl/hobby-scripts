import random
import os  # Required for clearScreen


def clearScreen():
    """Clears Screen to enable dynamic views. """
    os.system('cls' if os.name == 'nt' else 'clear')


def newDeck():
    """Creates a new ordered deck of cards listed by value in [sign,colour]
    pairs."""
    nfylla = []
    for i in range(10, 1, -1):
        nfylla.append(i)
    sfylla = ["K", "Q", "J", "A"]
    xrwma = [" Clubs  ", " Spades ", "Diamonds", " Hearts "]
    cards = []
    for i in (sfylla+nfylla):
        for j in xrwma:
            cards.append([i, j])
    return cards


def cardView(card):
    """Represents [sign,colour] card pairs with ASCII Art
    Used by handView. Changes to one should reflect on the other.
    Uses different sizes to accomodate 10s(length:2)"""
    if len(str(card[0])) == 1:
        c = """     ___________
    |"""+str(card[0])+"""        """+str(card[0])+"""|
    |          |
    |    """+str(card[0])+"""     |
    |<"""+str(card[1])+""">|
    |          |
    |"""+str(card[0])+"""        """+str(card[0])+"""|
    |__________|"""
    else:
        c = """     ___________
    |"""+str(card[0])+"""      """+str(card[0])+"""|
    |          |
    |   """+str(card[0])+"""     |
    |<"""+str(card[1])+""">|
    |          |
    |"""+str(card[0])+"""      """+str(card[0])+"""|
    |__________|"""
    return c


def handView(hand):
    """Prints the cards in hand using the cardView function
    Changes to one should also reflect on the other."""
    buf = ["", "", "", "", "", "", "", ""]
    if len(hand) == 0:
        return ""
    else:
        for i in range(8):
            for j in range(len(hand)):
                buf[i] += " "+(cardView(hand[j]).splitlines()[i])
    for l in buf:
        print(l)


def evaluateHand(hand):
    """Evaluates Hand Value by adding standard values and handling As depending
    on result"""
# And/Or tables don't allow for much compactness here. There should be a more compact way to write this but I'd rather get going.
    if (len(hand) == 2) and (("A" in hand[0]) or ("A" in hand[1])) and (("K" in hand[0]) or ("K" in hand[1]) or ("Q" in hand[0]) or ("Q" in hand[1]) or ("J" in hand[0]) or ("J" in hand[1])):
        return "Blackjack!"
    value = 0
    htype = "soft"
    for card in hand:
        if type(card[0]) == int:
            value += card[0]
        if card[0] in ["J", "Q", "K"]:
            value += 10
        if value > 21:
            return "Bust!"
        if value > 10:
            htype = "hard"
    # acount for Aces(pun intended):
    acount = 0
    for card in hand:
        if "A" in card:
            acount += 1
    if acount > 1:
        value += (acount-1)
        if value > 10:
            return (value+1)
        else:
            return (value+11)
    if acount == 1:
        if value > 10:
            value += 1
        else:
            value += 11
    if value > 21:
        return "Bust!"
    else:
        return value


class player:
    """Creates instances of a player.
    A player has a name and a hand holding cards drawn from the deckself.
    (Might be useful to create a new instance of a player every round like
    playerName=player(playerName.name,playerName.cash) to reset the hand?)"""

    def __init__(self, name, cash=100):
        self.name = name
        self.handValue = 0
        self.hand = []
        self.cash = cash
        self.state = "play"  # states will be "play","stand","bust"
        self.bet = 0

    def draw(self, deck):
        """Dealer deals a card to player. Technically not a draw."""
        self.hand.append(deck.pop())
        self.handValue = evaluateHand(self.hand)


class dealer:
    """Main Player dealing cards. New instance resets hand(dealer=dealer())"""

    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.handValue = 0
        self.playerList = [self]

    def draw(self, deck):
        """Dealer deals a card to himself"""
        card = deck.pop()
        self.hand.append(card)
        self.handValue = evaluateHand(self.hand)

    def deal(self, player, deck):
        """Deal 2 cards to each player. First card is dealt face-up and the
        second face down. Evaluates hand after second card, since there's no
        point evaluating with 1 card."""
        for pl in self.playerList[::-1]:
            t = deck.pop()
            pl.hand.append(t)
            print(str(pl.name)+" Is dealt a "+str(t[0])+" of "+str(t[1]))
        for pl in self.playerList[::-1]:
            t = deck.pop()
            pl.hand.append(t)
            evaluateHand(pl.hand)


"""



WIP BELOW







"""
''' WiP AREA '''
"""





"""

'''Quick Test of how it runs'''

if __name__ == "__main__":

    deck = newDeck()
    random.shuffle(deck)
    Deal = dealer()

    name = input("Let's play some Blackjack! What's your name?\n")
    P1 = player(name, 200)
    Deal.playerList.append(P1)
    Deal.deal(P1, deck)
    dv = pv = 0
    handView(P1.hand)
    n = int(input("Want any more cards? 1-9, 0 for pass\n"))
    if n > 0:
        for i in range(n):
            P1.draw(deck)
        if P1.handValue == "Bust!":
            print("You lost!")
        elif P1.handValue == "Blackjack!":
            print("You Won!")
        else:
            pv = P1.handValue
    if n == 0:
        while type(Deal.handValue) == int and Deal.handValue < 17:
            Deal.draw(deck)
        if type(Deal.handValue) == str:
            if Deal.handValue == "Blackjack!":
                print("House Wins with a Blackjack!")
            else:
                print("Player Wins")
        else:
            dv = Deal.handValue

    handView(P1.hand)

    if dv > 0 and pv > 0:
        if dv > pv:
            print("House wins")
        else:
            print("Player Wins!!")

    input("Press any key to exit...")

    """
    hand = [['J', 'D'], ['Q', 'D'], ['J', 'S'], ['J', 'H'], [2, 'H'], [5, 'D']]
    print(type(hand))
    asdf=evaluateHand(hand)
    print(asdf)



    deck=newDeck()
    random.shuffle(deck)
    hand1=[]
    for i in range(2):
        hand1.append(deck.pop())
    hand2=[["A","Spades"],["K","Hearts"]]





    c=evaluateHand(hand1)
    d=evaluateHand(hand2)
    print(c,d)
    handView(hand1)






    deck=newDeck()
    for c in deck:
        view=cardView(c)
        print(view)
    """
