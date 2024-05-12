from typing import Final

from data import CardType


class CardDetails:
    __card_type: Final[CardType]
    __card_number: Final[int]
    __pin: Final[int]
    __name: Final[str]

    def __init__(self, card_type: CardType, card_number: int, pin: int, name: str):
        self.__card_type = card_type
        self.__card_number = card_number
        self.__pin = pin
        self.__name = name

    @property
    def card_type(self):
        return self.__card_type

    @property
    def card_number(self):
        return self.__card_number

    @property
    def pin(self):
        return self.__pin

    @property
    def name(self):
        return self.__name
