"""These are tests of the Person class."""
import unittest

from blackjack import Card
from blackjack import Person
from blackjack import InvalidPersonName
from blackjack import InvalidCardAdd


class TestPerson(unittest.TestCase):
    """A class which defines the various tests of the Person class."""

    def test_name(self):
        """A test which makes sure that the person's name can be properly set."""

        # Check valid names
        valid_names = [
            "Player 1",
            "Bob",
            "Dealer",
        ]
        for name in valid_names:
            person = Person()
            self.assertEqual(person.name, "", msg="A person initially had the name of " + person.name + ".")
            person.set_name(name)
            self.assertEqual(person.name, name, msg="A person with the valid name " + name + " was unable to be created.")

        # Check invalid names
        invalid_names = [
            "",
            None,
        ]
        success = False
        for name in invalid_names:
            try:
                person = Person()
                person.set_name(name)
            except InvalidPersonName:
                success = True
            self.assertTrue(success, msg="A person with the invalid name \"" + str(name) + "\" was created.")

    def test_add_card(self):
        """A test which makes sure that the add_card method of the Person class functions correctly."""

        # Add some cards and make sure that they are correctly added to the person's cards
        person = Person()
        self.assertEqual(person.cards, [])
        card = Card("Clubs", "2")
        person.add_card(card)
        self.assertEqual(person.cards, [card,])
        card2 = Card("Clubs", "3")
        person.add_card(card2)
        self.assertEqual(person.cards, [card, card2,])

        # Attempt to add an invalid card
        person = Person()
        self.assertEqual(person.cards, [])
        card = None
        success = False
        try:
            person.add_card(card)
        except InvalidCardAdd:
            success = True
        self.assertTrue(success, msg="A None card was added to the person's cards.")

    def test_card_values(self):
        """A test which makes sure the card_values method of the Person class functions correctly."""

        # Compare some expected card values with their cards
        cards_set = [
            [
                Card("Clubs", "2"),
                Card("Clubs", "3"),
            ],
            [
                Card("Clubs", "2"),
                Card("Clubs", "Jack"),
            ],
            [
                Card("Clubs", "Queen"),
                Card("Clubs", "King"),
            ],
            [
                Card("Clubs", "2"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "2"),
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "2"),
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
            ],
            [
            ],
            [
                Card("Clubs", "Ace"),
            ],
        ]
        values_set = [
            [5,],
            [12,],
            [20,],
            [3,13,],
            [4,14,24,],
            [5,15,25,35,],
            [0,],
            [1,11,],
        ]
        for index in range(len(cards_set)):
            person = Person()
            for card in cards_set[index]:
                person.add_card(card)
            expected_values = values_set[index]
            calculated_values = person.card_values()
            self.assertEqual(calculated_values, expected_values, msg="A card values test failed at index " + str(index) + ".")

    def test_has_blackjack(self):
        """A test which makes sure the has_blackjack method of the Person class functions correctly."""

        # Test cases where there is blackjack
        blackjack_cases = [
            [
                Card("Clubs", "10"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "Jack"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "Queen"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "King"),
                Card("Clubs", "Ace"),
            ],
        ]
        for index in range(len(blackjack_cases)):
            cards = blackjack_cases[index]
            person = Person()
            for card in cards:
                person.add_card(card)
            result = person.has_blackjack()
            self.assertTrue(result, msg="A person that should have had blackjack did not at index " + str(index) + ".")

        # Test cases where there is not blackjack
        non_blackjack_cases = [
            [
                Card("Clubs", "9"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "10"),
                Card("Clubs", "10"),
            ],
            [
                Card("Clubs", "10"),
                Card("Clubs", "5"),
            ],
            [
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "10"),
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
                Card("Clubs", "Ace"),
            ],
            [
                Card("Clubs", "2"),
                Card("Clubs", "8"),
                Card("Clubs", "Ace"),
            ],
            [
            ],
        ]
        for index in range(len(non_blackjack_cases)):
            cards = non_blackjack_cases[index]
            person = Person()
            for card in cards:
                person.add_card(card)
            result = person.has_blackjack()
            self.assertFalse(result, msg="A person that should have had blackjack did not at index " + str(index) + ".")
