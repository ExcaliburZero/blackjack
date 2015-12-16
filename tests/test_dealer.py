"""These are tests of the Dealer class."""
import unittest

from blackjack import Dealer


class TestDealer(unittest.TestCase):
    """A class which defines the various tests of the Dealer class."""

    def test_name(self):
        """A test which makes sure that the dealer's name is properly set."""

        # Create a dealer and make sure that its name is "Dealer"
        dealer = Dealer()
        self.assertEqual(dealer.name, "Dealer")

    def test_initial_cards(self):
        """A test which makes sure that the dealer starts out with no cards."""

        # Make sure the dealer does not start with any cards
        dealer = Dealer()
        self.assertEqual(dealer.cards, [])
