"""These are tests of the Game class."""
import unittest

from blackjack import Game


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
