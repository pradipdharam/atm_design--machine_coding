from enum import Enum, auto


# OopCompanion:suppressRename


class ATMState(Enum):
    """Based on ATM State diagram drawn.
    """
    READY = auto()
    CARD_READING = auto()
    WITHDRAWAL_DETAILS_READING = auto()
    CASH_DISPENSING = auto()
    CARD_EJECTING = auto()
