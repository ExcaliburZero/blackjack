"""These are tests of the Game class."""
import unittest

from blackjack import Game
from blackjack import InvalidGameMethodOrder
from blackjack import InvalidPackNumber


class TestGame(unittest.TestCase):
    """A class which defines the various tests of the Game class."""

    def test_setup_new_game(self):
        """The method used to make sure that a new game can be properly set up."""

        # Create a new game and make sure it has the correct settings
        game = Game()
        game.setup_new_game()
        self.assertTrue(game.dealer is not None, msg="The dealer of the game was not created.")
        self.assertEqual(game.dealer.cards, [])
        self.assertEqual(game.state.name, "get_number_of_packs", msg="The initial game state was not correctly set.")

    def test_set_pack_number(self):
        """The method used to make sure that the number of packs of cards used in the deck can be set."""

        # Setup new games and attempt to set their number of packs
        valid_packs = [
            1,
            2,
            3,
            4,
            5,
            100,
        ]
        for packs in valid_packs:
            game = Game()
            game.setup_new_game()
            self.assertEqual(game.state.name, "get_number_of_packs", msg="The initial game state was not correctly set.")
            game.set_pack_number(packs)
            self.assertEqual(len(game.deck), packs * 52, msg="The number of packs was not correctly set with " + str(packs) + " packs.")

            # Make sure that the new game state was correctly set
            self.assertEqual(game.state.name, "get_player_chips", msg="The game state after setting the number of packs was not correctly set.")

        # Try to set invalid pack numbers
        invalid_packs = [
            -1,
            0,
            -100,
            1.5,
        ]
        for packs in invalid_packs:
            game = Game()
            game.setup_new_game()
            self.assertEqual(game.state.name, "get_number_of_packs", msg="The initial game state was not correctly set.")
            success = False
            try:
                game.set_pack_number(packs)
            except InvalidPackNumber:
                success = True
            self.assertTrue(success, msg="An invalid number of packs " + str(packs) + " was able to be set.")

        # Try to reset the number of packs to throw an error
        game = Game()
        game.setup_new_game()
        self.assertEqual(game.state.name, "get_number_of_packs", msg="The initial game state was not correctly set.")
        game.set_pack_number(1)
        success = False
        try:
            game.set_pack_number(1)
        except InvalidGameMethodOrder:
            success = True
        self.assertTrue(success, msg="The number of packs in a deck was incorrectly able to be reset.")
