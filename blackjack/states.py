"""This module contains classes related to game states."""
from .players import Player


class State(object):
    """
    This class is used to define game states.
    """

    def __init__(self, name, player):
        """
        The method used to construct a game state.

        :param str name: The name of the game state.
        :param str player: The player related to the game state.
        :raises InvalidStateName: if the given name is invalid.
        :raises InvalidStatePlayer: if the given player is invalid.
        """

        # Check to make sure that the name is valid
        valid_names = [
            "get_number_of_players",
            "get_player_chips",
            "get_player_names",
            "get_player_bets",
            "get_player_action",
        ]
        if name not in valid_names:
            raise InvalidStateName(name)

        # If the name is valid then set it
        self.name = name

        # Check to make sure that the player is valid
        if not isinstance(player, Player):
            raise InvalidStatePlayer

        # If the player is valid then set it
        self.player = player


class InvalidStateName(Exception):
    """
    An exception which is raised whenever a State is attempted to be created with an invalid name.
    """
    pass


class InvalidStatePlayer(Exception):
    """
    An exception which is raised whenever a State is attempted to be created with an invalid player.
    """
    pass
