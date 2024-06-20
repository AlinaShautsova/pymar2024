"""Module contains a solution to the (card deck) task."""
import random


class Card:
    """About card with number and suit."""

    def __init__(self, number, suit):
        """Upon initialization, creates a deck of cards."""
        self.number = number
        self.suit = suit

    def __str__(self):
        """Return information about card (as str)."""
        return f"{self.suit} {self.number}"


class DeckCards:
    """About cards in deck."""
    def __init__(self):
        """Function of initialization."""
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Fills the deck with regular cards and two jokers."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        numbers = list(range(1, 14))

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(number, suit))

        self.cards.append(Card(14, "Joker"))
        self.cards.append(Card(15, "Joker"))

    def mix(self):
        """Mix deck."""
        random.shuffle(self.cards)

    def get(self, card_number):
        """Return number of card from 1 to 54."""
        if 1 <= card_number <= 54:
            return self.cards[card_number - 1]
        return None


deck = DeckCards()
deck.mix()

card_number1 = int(input('Enter the card number from the deck(from 1 to 54): '))
card = deck.get(card_number1)
print(f'Your card is: {card}')
