from abc import ABC, abstractmethod

from atm import ATM
from data import ATMState


class State(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def cancel(self, transaction_id: int) -> bool:
        pass

    @abstractmethod
    def read_card(self, card_type: str, card_num: int, pin: int) -> None:
        pass

    @abstractmethod
    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        pass

    @abstractmethod
    def despense_cash(self, transaction_id: int) -> bool:
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    @property
    def state_name(self) -> ATMState:
        pass
