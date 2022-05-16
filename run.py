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

playing = True


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


class Hand:
    """Represent a player's hand.
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.card = card
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """Track a player's chaips, bets and winnings.
    """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# User Input - Betting
def take_bet(chips):
    """Get the bet amount from the user

    Args:
        :chips class: An instance of the Chips class

    Raises:
        ValueError: If the bet is greater than the total or less than 1,
                    or the input value cannot be converted into int.
    """
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?\n"))

            if chips.bet > chips.total or chips.bet <= 0:
                raise ValueError(
                    print(f"You have {chips.total} chips."
                      "Please bet between 1 and your chips.")
                )
        except ValueError:
            print("Please try again.\n")
        else:
            break


# Game Play
def hit(deck, hand):
    """Add one card from the deck to a player's hand

    Args:
        :deck class: An instance of the Deck class
        :hand class: An instance of the Hand class
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# User Input - Hit or Stand
def hit_or_stand(deck, hand):
    """Get the player's decision

    Args:
        :deck class: An instance of the Deck class
        :hand class: An instance of the Hand class

    Raises:
        ValueError: If the user enters a character other than H or S.
    """
    global playing

    while True:
        try:
            answer = input("Would you like to HIT or STAND? "
                           "Enter [H] to hit or [S] to stand.\n").upper()

            if not (answer[0] == "H" or answer[0] == "S"):
                raise ValueError(
                    print(f"You have entered {answer}. "
                      "Please enter [H] or [S].")
                )

            if answer[0] == "H":
                hit(deck, hand)
            elif answer[0] == "S":
                print("Player stands. Dealer is playing.")
                playing = False

        except ValueError as val_e:
            print(f"Invalid input: {val_e}")

        else:
            break


# Result
