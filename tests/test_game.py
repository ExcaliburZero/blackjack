"""These are tests of the Game class."""
import unittest

from blackjack import Game
from blackjack import InvalidGameMethodOrder
from blackjack import InvalidPackNumber
from blackjack import InvalidGameStartingChips
from blackjack import InvalidGamePlayersNumber
from blackjack import InvalidGamePlayerNames


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

    def test_set_starting_chips(self):
        """The method used to make sure that the number of starting chips for each player can be set."""

        # Setup new game and attempt to set their valid number of starting chips
        valid_chips = [
            1,
            10,
            100,
            9999,
        ]
        for chips in valid_chips:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            game.set_starting_chips(chips)
            self.assertEqual(game.starting_chips, chips, msg="The number of player starting chips was not correctly set with " + str(chips) + " chips.")

            # Make sure that the new game state was correctly set
            self.assertEqual(game.state.name, "get_number_of_players", msg="The game state was not correctly set after setting the number of starting chips.")

        # Try to set invalid chip numbers
        invalid_chips = [
            0,
            -1,
            -100,
            1.5,
            -1.5,
        ]
        for chips in invalid_chips:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            success = False
            try:
                game.set_starting_chips(chips)
            except InvalidGameStartingChips:
                success = True
            self.assertTrue(success, msg="An invalid number of starting chips " + str(chips) + " was able to be set.")

        # Try to reset the number of starting chips to throw an error
        game = Game()
        game.setup_new_game()
        game.set_pack_number(1)
        game.set_starting_chips(100)
        success = False
        try:
            game.set_starting_chips(200)
        except InvalidGameMethodOrder:
            success = True
        self.assertTrue(success, msg="The number of starting chips was incorrectly able to be reset.")

    def test_set_players_number(self):
        """The method used to make sure that the number of players in the game can be set."""

        # Setup new games and attempt to set thier number of players
        valid_players = [
            1,
            2,
            10,
            999,
        ]
        for players in valid_players:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            game.set_starting_chips(100)
            game.set_players_number(players)
            self.assertEqual(game.players_number, players, msg="The number of players was not correctly set with " + str(players) + " players.")

            # Make sure that the new game state is correctly set
            self.assertEqual(game.state.name, "get_player_names", msg="The game state was not correctly set after setting the number of players in the game.")

        # Try to set invalid player numbers
        invalid_players = [
            0,
            -1,
            -100,
            1.5,
        ]
        for players in invalid_players:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            game.set_starting_chips(100)
            success = False
            try:
                game.set_players_number(players)
            except InvalidGamePlayersNumber:
                success = True
            self.assertTrue(success, msg="An invalid number of players " + str(players) + " was able to be set.")

        # Try to reset the number of players to throw an error
        game = Game()
        game.setup_new_game()
        game.set_pack_number(1)
        game.set_starting_chips(100)
        game.set_players_number(3)
        success = False
        try:
            game.set_players_number(2)
        except InvalidGameMethodOrder:
            success = True
        self.assertTrue(success, msg="The number of players was incorrectly able to be reset.")

    def test_set_player_names(self):
        """The method used to make sure that the names of the players in the game can be set."""

        # Setup new games and attempt to set their players' names
        valid_players = [
            ["Bob", "Sam", "Cal", "Kris"],
            ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"],
            ["Bot"],
            ["P1", "P2", "P3"],
        ]
        for players in valid_players:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            game.set_starting_chips(100)
            game.set_players_number(len(players))
            game.set_player_names(players)
            self.assertEqual(game.player_names, players, msg="The game's player names were not correctly set with: " + str(players))

            # Make sure that the new game state is corectly set
            self.assertEqual(game.state.name, "start_game", msg="The game's state was not correctly set after setting the player names.")

        # Try to set invalid players
        invalid_players = [
            None,
            [None, None],
            [123, 456, 789],
            ["Bob", "Sam", 123],
            ["John", ""],
        ]
        for players in invalid_players:
            game = Game()
            game.setup_new_game()
            game.set_pack_number(1)
            game.set_starting_chips(100)
            game.set_players_number(len(players or "1"))
            success = False
            try:
                game.set_player_names(players)
            except InvalidGamePlayerNames:
                success = True
            self.assertTrue(success, msg="The following invalid series of player names was able to be set: " + str(players))

        # Test the case where the number of players given is not the same as the number of names given
        game = Game()
        game.setup_new_game()
        game.set_pack_number(1)
        game.set_starting_chips(100)
        game.set_players_number(2)
        success = False
        try:
            game.set_player_names(["P1", "P2", "P3"])
        except InvalidGamePlayerNames:
            success = True
        self.assertTrue(success, msg="A number of player names unequal to the number to the number of players in the game was able to be set.")

        # Try to reset the names of the players to throw an error
        game = Game()
        game.setup_new_game()
        game.set_pack_number(1)
        game.set_starting_chips(100)
        game.set_players_number(3)
        game.set_player_names(["P1", "P2", "P3"])
        success = False
        try:
            game.set_player_names(["P01", "P02", "P03"])
        except InvalidGameMethodOrder:
            success = True
        self.assertTrue(success, msg="The names of the players was incorrectly able to be reset.")
