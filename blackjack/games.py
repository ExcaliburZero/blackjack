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

        # The number of chips each player starts with
        self.starting_chips = None

        # The number of players in the game
        self.players_number = None

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

    def set_starting_chips(self, chips):
        """
        The method used to set the number of chips that each player starts with.

        :param int chips: The number of chips each player starts with.
        """

        # Make sure that the game is requesting the number of starting chips
        if self.state.name != "get_player_chips":
            raise InvalidGameMethodOrder(self.state.name)

        # Make sure that the given number of starting chips is valid
        if chips < 1 or not isinstance(chips, int):
            raise InvalidGameStartingChips(chips)

        # Set the number of starting chips
        self.starting_chips = chips

        # Set the game state so that the number of players is requested
        self.state = State("get_number_of_players", None)

    def set_players_number(self, players):
        """
        The method used to set the number of players in the game.

        :param int players: The number of players in the game.
        """

        # Make sure that the game is requesting the number of players
        if self.state.name != "get_number_of_players":
            raise InvalidGameMethodOrder(self.state.name)

        # Make sure that the given number of players is valid
        if players < 1 or not isinstance(players, int):
            raise InvalidGamePlayersNumber(players)

        # Set the number of players
        self.players_number = players

        # Set the game state so that the names of the players are requested
        self.state = State("get_player_names", None)


class InvalidGameMethodOrder(Exception):
    """An exception which is raised whenever an incorrect method is run from the game, based on its current state."""
    pass


class InvalidPackNumber(Exception):
    """An exception which is raised whenever the number of packs the game is set to use is invalid."""
    pass


class InvalidGameStartingChips(Exception):
    """An exception which is raised whenever the number of starting chips the game is set to use is invalid."""
    pass


class InvalidGamePlayersNumber(Exception):
    """An exception which is raised whenever the number of players that the game is set to have is invalid."""
    pass
