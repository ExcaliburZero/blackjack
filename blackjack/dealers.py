"""This module is used to store the classes related to the dealer."""
from .people import Person


class Dealer(Person):
    """
    The class used to represent the dealer.
    """

    def __init__(self):
        """
        The method used to create a dealer and initalize its name and cards.
        """

        # The name of the dealer
        self.name = "Dealer"
        # The cards that the dealer has
        self.cards = []
