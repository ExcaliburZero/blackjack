"""This module contains classes related to actions."""


class Action(object):
    """
    This class is used to define actions taken by people.
    """

    def __init__(self, move):
        """
        The method used to construct an action.

        :param str move: The move that the action is comprised of.
        :raises InvalidActionMove: if the given move is invalid.
        """

        # Check to make sure that the move is valid
        valid_moves = [
            "Hit",
            "Stand",
        ]
        if move not in valid_moves:
            raise InvalidActionMove(move)

        # If the move is valid then set it
        self.move = move

class InvalidActionMove(Exception):
    """
    An exception which is raised whenever an Action is attempted to be created with an invalid move.
    """
    pass
