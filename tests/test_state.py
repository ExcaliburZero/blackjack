"""These are tests of the State class."""
import unittest

from blackjack import State
from blackjack import InvalidStateName
from blackjack import InvalidStatePlayer
from blackjack import Player
from blackjack import Person
from blackjack import Dealer

class TestState(unittest.TestCase):
    """A class which defines the various tests of the State class."""

    def test_valid_names(self):
        """A test which makes sure that only valid name can be made as part of states."""

        # Check all valid names
        valid_names = [
            "get_number_of_packs",
            "get_number_of_players",
            "get_player_chips",
            "get_player_names",
            "get_player_bets",
            "get_player_action",
        ]
        for name in valid_names:
            state = State(name, Player(100))
            self.assertEqual(state.name, name, msg="A state with valid name " + name + " was unable to be created.")

        # Check several invalid names
        invalid_names = [
            "Hit",
            "Stand",
            "Draw",
            "Explode",
            "-0230h2o0r",
            "",
            None,
        ]
        for name in invalid_names:
            success = False
            try:
                state = State(name, Player(100))
            except InvalidStateName:
                success = True
            self.assertTrue(success, msg="A state with the invalid name " + str(name) + " was able to be created.")

    def test_valid_players(self):
        """A test which makes sure that only vaild players can be made as part of states."""

        # Check valid players
        valid_players = [
            Player(100),
            Player(1000),
        ]
        for index in range(len(valid_players)):
            state = State("get_player_action", valid_players[index])
            self.assertEqual(state.player, valid_players[index], msg="A state with valid player test index " + str(index) + " was unable to be created.")

        # Check invalid players
        invalid_players = [
            Person(),
            Dealer(),
            "Player 1",
            1,
        ]
        for index in range(len(invalid_players)):
            success = False
            try:
                state = State("get_player_action", invalid_players[index])
            except InvalidStatePlayer:
                success = True
            self.assertTrue(success, msg="A state with invalid player test index " + str(index) + " was able to be created.")
