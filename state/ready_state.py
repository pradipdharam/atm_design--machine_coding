from atm import ATM
from data import ATMState
from db import DBAccessor
from state import State, CardReadingState, CardEjectingState


class ReadyState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self):
        transaction_id = None
        transaction_id = DBAccessor.create_new_transaction(self.__atm.machine_id)
        if transaction_id is None:
            raise RuntimeError("Error creating transaction")
        self.__atm.change_state(CardReadingState(self.__atm))
        return transaction_id

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

    @property
    def state_name(self) -> ATMState:
        return ATMState.READY
