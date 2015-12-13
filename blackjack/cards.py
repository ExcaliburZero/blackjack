"""This module contains classes used for cards."""

class Card(object):
    """
    A class which specifies the details of a single playing card.
    """

    # The suit of the card. Can be Clubs, Diamonds, Hearts, or Spades. All are capitalized.
    suit = ""
    # The face of the card. Can be 2-10, Jack, Queen, King, or Ace. All words are capitalized.
    face = ""

    def __init__(self, suit, face):
        """
        The method that is used to construct a card object.

        :param str suit: The suit of the card.
        :param str face: The face of the card.
        :raises InvalidSuit: if the given suit is invalid.
        :raises InvalidFace: if the given face is invalid.
        """
        # Check to make sure that the face and suit are valid
        valid_suits = [
            "Clubs",
            "Diamonds",
            "Hearts",
            "Spades",
        ]
        if suit not in valid_suits:
            raise InvalidSuit(suit)

        valid_faces = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        if face not in valid_faces:
            raise InvalidFace(face)

        # If the suit and face are valid then set them
        self.suit = suit
        self.face = face

class InvalidSuit(Exception):
    """
    An exception which is raised when a card with an invalid suit is attempted to be created.
    """
    pass

class InvalidFace(Exception):
    """
    An exception which is raised when a card with an invalid face is attempted to be created.
    """
    pass
