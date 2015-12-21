"""These are tests of the Action class."""
import unittest

from blackjack import Action
from blackjack import InvalidActionMove

class TestAction(unittest.TestCase):
    """A class which defines the various tests of the Action class."""

    def test_valid_moves(self):
        """A test which makes sure that only valid moves can be made as part of actions."""

        # Check all valid moves
        valid_moves = [
            "Hit",
            "Stand",
        ]
        for move in valid_moves:
            action = Action(move)
            self.assertEqual(action.move, move, msg="An action with valid move " + move + " was unable to be created.")

        # Check several invalid moves
        invalid_moves = [
            "Draw",
            "Explode",
            "-0230h2o0r",
            "",
            None,
        ]
        for move in invalid_moves:
            success = False
            try:
                action = Action(move)
            except InvalidActionMove:
                success = True
            self.assertTrue(success, msg="An action with the invalid move " + str(move) + " was able to be created.")
