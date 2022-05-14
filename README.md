# Blackjack

This is a mini Python project from a Udemy Python course\*

\*2022 Complete Python Bootcamp From Zero to Hero in Python(Instructor: Jose Portilla)

## Language

- Python

## Requirements

- I need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- I need to keep track of the player's total money.
- I need to alert the player of wins, losses, or busts, etc...
- I must use OOP and classes in some portion of the game. Use classes for the Deck and the Player's hand.

# Game Play

- To play a hand of Blackjack the following steps must be followed:

  1. Create a deck of 52 cards
  2. Shuffle the deck
  3. Ask the Player for their bet
  4. Make sure that the Player's bet does not exceed their available chips
  5. Deal two cards to the Dealer and two cards to the Player
  6. Show only one of the Dealer's cards, the other remains hidden
  7. Show both of the Player's cards
  8. Ask the Player if they wish to Hit, and take another card
  9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
  10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
  11. Determine the winner and adjust the Player's chips accordingly
  12. Ask the Player if they'd like to play again

## Structure

- Visual Representation

  > Welcome to Blackjack!

- Game Setup

  - Deck
    - Face cards = 10
    - Ace = 1 or 11 preferable to the player
  - Shuffle

- User Input

  > How much do you want to bet?

  - The player's bet does not exceed their available chips

  - Two cards to each player
    - Show one of the dealer's card
    - Show both of the player's cards

  > Do you want to Hit or Stand? Enter [H] for Hit or [S] for stand.

  - The dealer will always hit until their value meets or exceeds 17
  - Calculate the player's chips
    - If the dealer busts, the player gets double their bet

- Display result
  > Congratulations! You have won the game!
  > Dealer wins!
  > Push!
  > Do you want to play again? Enter [Y]es / [N]o
