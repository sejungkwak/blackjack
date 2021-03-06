import random

# Visual Representation
print("\nWelcome to Blackjack!\n")

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
                    print(f"You have {chips.total} chips. "
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
            answer = input("\nWould you like to HIT or STAND? "
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


def show_some(player, dealer):
    """Display the player's cards and one of the dealer's cards
    at the start of the game and after each time the player takes a card.

    Args:
        :player class: An instance of the Hand class
        :dealer class: An instance of the Hand class
    """
    print("\nDealer's Hand:")
    print("First card hidden!")
    print(f"{dealer.cards[1]}")

    print("\nPlayer's Hand:", *player.cards, sep="\n")


def show_all(player, dealer):
    """Display the player and dealer's cards at the end of the game.

    Args:
        :player class: An instance of the Hand class
        :dealer class: An instance of the Hand class
    """
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print(f"Value of Dealer's Hand is: {dealer.value}")
    print("\nPlayer's Hand:", *player.cards, sep="\n")
    print(f"Value of Player's Hand is: {player.value}")


# End of game scenarios
def player_bust(chips):
    """Display the result of the player busted and run the lose_bet method.

    Args:
        :chips class: An instance of the Chips class
    """
    print("\nPLAYER BUSTED! DEALER WINS!\n")
    chips.lose_bet()


def player_win(chips):
    """Display the result of the player winning and run the win_bet method.

    Args:
        :chips class: An instance of the Chips class
    """
    print("\nPLAYER WINS!\n")
    chips.win_bet()


def dealer_bust(chips):
    """Display the result of the dealer busted and run the win_bet method.

    Args:
        :chips class: An instance of the Chips class
    """
    print("\nDEALER BUSTED! PLAYER WINS!\n")
    chips.win_bet()


def dealer_win(chips):
    """Display the result of the dealer winning and run the lose_bet method.

    Args:
        :chips class: An instance of the Chips class
    """
    print("\nDEALER WINS!\n")
    chips.lose_bet()


def push():
    """Display the result of a tie.
    """
    print("\nDEALER and PLAYER TIE! PUSH!\n")


# Set up the Player's chips
player_chips = Chips()

# Game loop
while playing:
    # Print an opening statement
    print("Get as close to 21 as you can without going over!\n"
          "Dealer hits until they reach 17. Aces count as 1 or 11.\n"
          f"You have {player_chips.total} chips.")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_bust(player_chips)
        elif player_hand.value > dealer_hand.value:
            player_win(player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_win(player_chips)
        else:
            push()

    # Inform Player of their chips total
    print(f"Your chips are at {player_chips.total}")

    # Ask to play again
    while True:
        try:
            play_again = input("Do you want to play again?\n"
                               "Enter [Y] for yes or [N] for no.\n").upper()
            if not (play_again == "Y" or play_again == "N"):
                raise ValueError(
                    print(f"You have entered {play_again}")
                )
            if play_again == "Y":
                playing = True
            elif play_again == "N":
                print("Thank you for playing!")
                playing = False
        except ValueError as val_e:
            print(f"Invalid input: {val_e}")
        else:
            break
