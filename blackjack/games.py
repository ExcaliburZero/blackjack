"""This module contains classes related to the game logic."""
from .dealers import Dealer
from .states import State


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
