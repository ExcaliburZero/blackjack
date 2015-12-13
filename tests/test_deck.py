"""These are tests of the Deck class."""
import unittest

from blackjack import Deck
from blackjack import Card
from blackjack import InvalidDeckSize
from blackjack import InvalidDeckDraw

class TestDeck(unittest.TestCase):
    """A class which defines the various tests of the Deck class."""

    def test_deck_size(self):
        """
        A test which checks to make sure that the deck is created with the correct number of cards.
        """
        # Test valid number of packs of cards
        valid_packs = [
            1,
            2,
            3,
        ]
        for packs in valid_packs:
            deck = Deck(packs)
            self.assertEqual(len(deck), 52 * packs, msg="Incorrect number of cards " + \
                str(len(deck)) + " in deck of " + str(packs) + " packs.")

        # Test invalid numbers of packs of cards
        invalid_packs = [
            0,
            -1,
        ]
        for packs in invalid_packs:
            success = False
            try:
                deck = Deck(packs)
            except InvalidDeckSize:
                success = True
            self.assertTrue(success, msg="Invalid number of packs of cards created: " + \
                str(packs) + ".")

    def test_deck_draw(self):
        """A test which checks the draw method of the deck class."""
        deck = Deck(1)
        self.assertEqual(len(deck), 52, msg="Incorrect number of inital cards in deck.")
        card = deck.draw()
        self.assertEqual(len(deck), 51, msg="Incorrect number of cards in deck after draw.")

        # Make sure that the card object drawn is actually a card
        self.assertTrue(isinstance(card, Card), msg="The card returned by the draw method of " + \
            "Deck is not a Card object.")

        # Make sure that all cards can be drawn
        deck = Deck(1)
        for x in range(52):
            deck.draw()
        self.assertEqual(len(deck), 0)

        # Make sure that an error is raised when the deck is empty
        success = False
        try:
            deck.draw()
        except InvalidDeckDraw:
            success = True
        self.assertTrue(success, msg="Deck does not raise error when drawing from an empty deck.")
