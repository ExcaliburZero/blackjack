"""
This module contains the classes associated with the base class of Person,
which is used to create other classes based off of it, such as Dealer and
Player.
"""


class Person(object):
    """
    The class used to serve as a base class for the Player and Dealer classes.
    """

    def __init__(self):
        """
        The method used to create a Person object and declare its name and cards.
        """

        # The name of the person, this should be set using the set_name method
        self.name = ""
        # The cards that the person has
        self.cards = []

    def set_name(self, name):
        """
        The method used to set the name of a person.

        :param str name: The name of the person.
        :raises InvalidPersonName: if the given name is invalid.
        """

        # Make sure that the name is not blank
        if name == "" or name is None:
            raise InvalidPersonName(name)

        # Set the name of the player
        self.name = name

    def add_card(self, card):
        """
        The method used to add a card to the person's cards.

        :param Card card: The card to add to the person's cards.
        :raises IvalidCardAdd: if the given card is invalid.
        """

        # Check to make sure that the card is not invalid
        if card is None:
            raise InvalidCardAdd

        # Add the card to the person's cards
        self.cards.append(card)


class InvalidPersonName(Exception):
    """
    An exception which is raised when a person is attempted to be created with an invalid name.
    """
    pass


class InvalidCardAdd(Exception):
    """
    An exception which is raised when an invalid card is attempted to be added to a person's cards.
    """
    pass
