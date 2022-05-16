import random

# Visual Representation
print("Welcome to Blackjack!")

# Game Setup - Deck
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
          "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:
    """Represent a single playing card and initialised by passing suit and rank.

    Args:
        :suit str: one of the 4 categories
        :rank str: one of the 13 ranks
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represent a deck of playing cards in order.
    """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        cards = ""
        for card in self.deck:
            cards += f"{card}\n"
        return f"{cards}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# User Input - Betting

# Game Play

# Result
