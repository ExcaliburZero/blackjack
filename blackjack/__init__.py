"""The init file for the blackjack package."""
from .cards import Card
from .cards import InvalidSuit
from .cards import InvalidFace
from .decks import Deck
from .decks import InvalidDeckSize
from .decks import InvalidDeckDraw
from .people import Person
from .people import InvalidPersonName
from .people import InvalidCardAdd

__author__ = 'Christopher Randall Wells'
__copyright__ = 'Copyright 2015 Christopher Randall Wells'
__license__ = 'MIT'
__title__ = 'blackjack'
__version__ = '0.1'

__all__ = (
    # Classes
    'Card',
    'Deck',
    'Person',

    # Exceptions
    'InvalidSuit',
    'InvalidFace',
    'InvalidDeckSize',
    'InvalidDeckDraw',
    'InvalidPersonName',
    'InvalidCard',
)
