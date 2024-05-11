from atm import ATM
from state import State, CardReadingState, CardEjectingState


class ReadyState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self) -> int:
        self.__atm.change_state(CardReadingState(self.__atm))

    def cancel(self, transaction_id: int) -> bool:
        self.__atm.change_state(CardEjectingState(self.__atm))
        return True

    def read_card(self, card_type: str, card_num: int, pin: int) -> None:
        pass

    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        pass

    def despense_cash(self, transaction_id: int) -> bool:
        pass

    def eject_card(self):
        pass
