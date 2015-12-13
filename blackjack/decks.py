"""This module contains classes used for decks."""
import random

from .cards import Card

class Deck(object):
    """
    A class which specifies the details of the deck of playing cards.
    """

    def __init__(self, packs):
        """
        The method used to construct a deck using a given number of packs of playing cards.

        :param int packs: The number of packs of 52 playing cards to place in the deck.
        :raises InvalidDeckSize: if the number of packs given is lesser than 1.
        """
        # The cards contained in the deck
        self.cards = []

        # Check to make sure that the number of packs given is valid
        if packs < 1:
            raise InvalidDeckSize(packs)

        # Fill the deck with cards
        suits = [
            "Clubs",
            "Diamonds",
            "Hearts",
            "Spades",
        ]
        faces = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        for x in range(packs):
            for suit in suits:
                for face in faces:
                    self.cards.append(Card(suit, face))

    def __len__(self):
        """
        The method used to get the number of cards in the deck. Overrides the len function output.

        :returns int: The number of cards in the deck.
        """
        return len(self.cards)

    def draw(self):
        """
        The method used to draw a random card from the deck.

        :returns Card: The card drawn from the deck.
        :raises InvalidDeckDraw: if the deck is empty.
        """
        # Make sure that the deck is not empty
        if len(self.cards) == 0:
            raise InvalidDeckDraw

        # Draw the card from the deck
        card_number = random.randrange(len(self.cards))
        return self.cards.pop(card_number)

class InvalidDeckSize(Exception):
    """
    An exception which is raised whenever an invalid number
    """

class InvalidDeckDraw(Exception):
    """
    An exception which is raised whenever a card is attempted to be drawn from the deck, but the
    deck is empty.
    """
