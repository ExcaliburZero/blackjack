"""These are tests of the Card class."""
import unittest

from blackjack import Card
from blackjack import InvalidSuit
from blackjack import InvalidFace

class TestCard(unittest.TestCase):
    """A class which defines the various tests of the Card class."""

    def test_suits(self):
        """A test which checks to make sure that only valid suits can be created."""

        # Test valid suits
        valid_suits = [
            "Clubs",
            "Diamonds",
            "Hearts",
            "Spades",
        ]
        for suit in valid_suits:
            card = Card(suit, "2")
            self.assertEqual(card.suit, suit)

        # Test some invalid suits
        invalid_suits = [
            "Club",
            "Diamond",
            "Heart",
            "Spade",
            "clubs",
            "diamonds",
            "hearts",
            "spades",
            "",
        ]
        for suit in invalid_suits:
            success = False
            try:
                card = Card(suit, "2")
            except InvalidSuit:
                success = True
            self.assertTrue(success, msg="Invalid suit " + suit + " created.")

    def test_faces(self):
        """A test which checks to make sure that only valid faces can be created."""

        # Test valid faces
        valid_faces = [
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
        for face in valid_faces:
            card = Card("Clubs", face)
            self.assertEqual(card.face, face)

        # Test invalid faces
        invalid_faces = [
            "0",
            "1",
            "11",
            "12",
            "13",
            "jack",
            "queen",
            "king",
            "ace",
            "",
        ]
        for face in invalid_faces:
            sucess = False
            try:
                card = Card("Clubs", face)
            except InvalidFace:
                sucess = True
            self.assertTrue(sucess, msg="Invalid face " + face + " created.")

    def test_get_value(self):
        """A test which checks the get_value method of the Card class."""

        # Test to make sure that all of the faces and values match up
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
        values = [
            [2,],
            [3,],
            [4,],
            [5,],
            [6,],
            [7,],
            [8,],
            [9,],
            [10,],
            [10,],
            [10,],
            [10,],
            [1, 11,],
        ]

        for index in range(len(faces)):
            face = faces[index]
            card = Card("Clubs", face)
            found_value = card.get_value()
            expected_value = values[index]
            self.assertEqual(found_value, expected_value, msg="The value for face " + face + \
                " was incorrectly returned as " + str(found_value[0]) + " when it should have" + \
                " been " + str(expected_value[0]) + ".")
