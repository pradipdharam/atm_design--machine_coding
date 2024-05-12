from enum import Enum, auto


class TransactionStatus(Enum):
    APPROVED = auto()
    NOT_APPROVED = auto()
    EXECUTED = auto()
    CANCELLED = auto()
