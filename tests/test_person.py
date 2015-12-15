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
