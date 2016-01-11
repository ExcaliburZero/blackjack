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
            "get_number_of_packs",
            "get_number_of_players",
            "get_player_chips",
            "get_player_names",
            "get_player_bets",
            "get_player_action",
            "start_game",
        ]
        if name not in valid_names:
            raise InvalidStateName(name)

        # If the name is valid then set it
        self.name = name

        # Check to make sure that the player is valid, None is valid, as it is possible for a state to have no associated player
        if not isinstance(player, Player) and player is not None:
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
