"""This module is used to store the classes related to players."""
from .people import Person


class Player(Person):
    """
    The class used to represent the players.
    """

    def __init__(self, chips):
        """
        The method used to create a player and initalize its name and cards.

        :param int chips: The number of chips which the player starts out with.
        :raises InvalidStartingChips: if the number of starting chips is invalid.
        """

        # The name of the player
        self.name = "Player"
        # The cards that the player has
        self.cards = []
        # The number of chips that the player has
        self.chips = 0

        # Make sure that the number of starting chips is valid
        if not isinstance(chips, int) or chips < 0:
            raise InvalidStartingChips(chips)

        # Set the number of chips that the player starts with
        self.chips = chips

    def change_chips(self, chips):
        """
        The method that is used to change the number of chips that the player has.

        Positive amounts increase the player's chips, and negative amounts decrease the player's chips.

        This method does not allow for chip changes of 0, as such an input would cause no actual change in the player's chips.

        :param int chips: The change in the player's chips.
        :raises InvalidChipsChange: if the amount of change in the player's chips is invalid.
        """

        # Make sure that the number of chips change is not invalid
        if not isinstance(chips, int) or chips == 0:
            raise InvalidChipsChange(chips)

        # Change the player's chips by the specified amount
        self.chips = self.chips + chips


class InvalidStartingChips(Exception):
    """
    An exception which is raised whenever a player is attempted to be created wiht an invalid number of starting chips.
    """
    pass


class InvalidChipsChange(Exception):
    """
    An exception which is raised whenever the amount of chips a player has player is attempted to be changed by an invalid number of chips.
    """
    pass
