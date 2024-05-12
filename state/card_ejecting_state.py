from atm import ATM
from data import ATMState
from state import State, ReadyState


class CardEjectingState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self):
        self.__atm.change_state(ReadyState(self.__atm))

    def cancel(self, transaction_id: int) -> bool:
        self.__atm.change_state(ReadyState(self.__atm))
        return True

    def read_card(self, card_type: str,
                  card_num: int, pin: int) -> None:
        pass

    def read_withdrawal_details(self, card_type: str,
                                card_num: int, pin: int):
        pass

    def despense_cash(self, transaction_id: int) -> bool:
        pass

    def eject_card(self):
        pass

    @property
    def state_name(self) -> ATMState:
        return ATMState.CARD_EJECTING
