"""This module is used to store the classes related to the dealer."""
from .people import Person
from .actions import Action


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

    def get_action(self):
        """
        The method that is used to get the next action of the dealer.

        :returns Action: The next action of the dealer.
        """

        # See if the dealer's cards are certainly over or equal to 17
        any_below = False
        for result in self.card_values():
            if result < 17:
                any_below = True

        # Decide on the action based on whether or not all possibilities are over or equal to 17
        if any_below:
            next_action = Action("Hit")
        else:
            next_action = Action("Stand")

        # Return the action
        return next_action
