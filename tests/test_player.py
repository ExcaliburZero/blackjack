"""These are tests of the Player class."""
import unittest

from blackjack import Player
from blackjack import InvalidStartingChips
from blackjack import InvalidChipsChange


class TestPlayer(unittest.TestCase):
    """A class which defines the various tests of the Player class."""

    def test_name(self):
        """A test which makes sure that the player's default name is properly set."""

        # Create a player and make sure that its name is "Player"
        player = Player(100)
        self.assertEqual(player.name, "Player")

    def test_initial_cards(self):
        """A test which makes sure that the player starts out with no cards."""

        # Make sure the dealer does not start with any cards
        player = Player(100)
        self.assertEqual(player.cards, [])

    def test_initial_chips(self):
        """A test which makes sure that the player starts out with the correct number of chips."""

        # Check valid chip amounts
        valid_chips = [
            0,
            1,
            100,
            9999,
        ]
        for chips in valid_chips:
            player = Player(chips)
            self.assertEqual(player.chips, chips, msg="A player was unable to be created with the valid number of chips " + str(chips) + ".")

        # Check invalid chip amounts
        invalid_chips = [
            -1,
            -100,
            "100",
            1.5,
            None,
        ]
        for chips in invalid_chips:
            success = False
            try:
                player = Player(chips)
            except InvalidStartingChips:
                success = True
            self.assertTrue(success, msg="A player was able to be created with the invalid number of chips " + str(chips) + ".")

    def test_change_chips(self):
        """A test which makes sure that the change_chips method of the Player class functions properly."""

        # Check valid chip changes
        valid_chip_changes = [
            1,
            100,
            -1,
            -100,
        ]
        for chip_change in valid_chip_changes:
            player = Player(200)
            self.assertEqual(player.chips, 200, msg="The starting chips of the player was not correctly set.")
            player.change_chips(chip_change)
            self.assertEqual(player.chips, 200 + chip_change, msg="A player chip change of " + str(chip_change) + " chips did not work correctly.")

        # Check for invalid chip changes
        invalid_chip_changes = [
            0,
            1.1,
            "1",
            None,
        ]
        for chip_change in invalid_chip_changes:
            player = Player(200)
            success = False
            try:
                player.change_chips(chip_change)
            except InvalidChipsChange:
                success = True
            self.assertTrue(success, msg="An invalid player chips change of " + str(chip_change) + " was able to be made.")
