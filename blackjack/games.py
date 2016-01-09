"""This module contains classes related to the game logic."""
from .dealers import Dealer
from .states import State
from .decks import Deck


class Game(object):
    """
    This class is used to control the logic and flow of the game.
    """

    def __init__(self):
        """
        The method used to set the variables used by the game.
        """

        # The state of the game
        self.state = None

        # The deck used in the game
        self.deck = None

        # The players in the game
        self.players = None

        # The dealer in the game
        self.dealer = None

    def setup_new_game(self):
        """
        The method used to setup a new game.
        """

        # Create the Dealer
        self.dealer = Dealer()

        # Set the game state so that the number of packs of cards for the deck is requested
        self.state = State("get_number_of_packs", None)

    def set_pack_number(self, packs):
        """
        The method used to set the number of packs of cards used in the deck for the game.

        :param int packs: The number of packs of cards to use in the deck.
        """

        # Make sure that the game is requesting the number of packs
        if self.state.name != "get_number_of_packs":
            raise InvalidGameMethodOrder(self.state.name)

        # Make sure that the given number of packs is valid
        if packs < 1 or not isinstance(packs, int):
            raise InvalidPackNumber(packs)

        # Create a deck with the given number of packs
        self.deck = Deck(packs)

        # Set the game state so the number of players is requested
        self.state = State("get_player_chips", None)


class InvalidGameMethodOrder(Exception):
    """An exception which is raised whenever an incorrect method is run from the game, based on its current state."""
    pass


class InvalidPackNumber(Exception):
    """An exception which is raised whenever the number of packs the game is set to use is invalid."""
    pass
