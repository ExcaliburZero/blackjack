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
        :raises InvalidCardAdd: if the given card is invalid.
        """

        # Check to make sure that the card is not invalid
        if card is None:
            raise InvalidCardAdd

        # Add the card to the person's cards
        self.cards.append(card)

    def card_values(self):
        """
        The method used to get all of the possible values of the total of the values of the person's cards.

        :returns list: The possible values of the total of the values of the user's cards.
        """

        # Find the number of possible totals
        totals = 1
        aces = 0
        for card in self.cards:
            if card.face == "Ace":
                aces += 1
        totals += aces

        # Find each of the possible totals
        values = [0] * totals
        for card in self.cards:
            if card.face != "Ace":
                for index in range(len(values)):
                    values[index] += card.get_value()[0]
        if aces > 0:
            for index in range(len(values)):
                values[index] += 1 * (aces - index) + 11 * index

        # Return the possible totals
        return values

    def has_blackjack(self):
        """
        The method used to tell whether or not the person has blackjack.

        :returns bool: Whether or not the person has blackjack.
        """

        # Check to make sure that the person does not have more than two cards
        if len(self.cards) > 2:
            return False

        # See if the person has a possible card value of 21
        for value in self.card_values():
            if value == 21:
                return True

        # If no possiblity was 21, then the person does not have blackjack
        return False


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
