"""These are tests of the Dealer class."""
import unittest

from blackjack import Dealer
from blackjack import Card


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

    def test_get_action(self):
        """A test which makes sure that the get_action method of the Dealer class functions properly."""

        # Try several test cases
        test_cases = [
            [Card("Clubs", "2"), Card("Clubs", "2"), "Hit", ],
            [Card("Clubs", "10"), Card("Clubs", "10"), "Stand", ],
            [Card("Clubs", "10"), Card("Clubs", "7"), "Stand", ],
            [Card("Clubs", "10"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "Ace"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "Ace"), Card("Clubs", "6"), Card("Clubs", "10"), "Stand", ],
            [Card("Clubs", "Jack"), Card("Clubs", "7"), "Stand", ],
            [Card("Clubs", "Queen"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "King"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "Ace"), Card("Clubs", "Ace"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "Ace"), Card("Clubs", "Ace"), Card("Clubs", "6"), "Hit", ],
            [Card("Clubs", "7"), Card("Clubs", "8"), "Hit", ],
            [Card("Clubs", "7"), Card("Clubs", "8"), Card("Clubs", "Ace"), "Hit", ],
            [Card("Clubs", "7"), Card("Clubs", "8"), Card("Clubs", "2"), "Stand", ],
            [Card("Clubs", "Jack"), Card("Clubs", "Queen"), "Stand", ],
        ]
        for case in test_cases:
            dealer = Dealer()
            cards = len(case) - 1
            for index in range(cards):
                dealer.add_card(case[index])
            action = dealer.get_action()
            self.assertEqual(action.move, case[-1], msg="The test of the get_action method with the index of " + str(test_cases.index(case)) + " failed.")
