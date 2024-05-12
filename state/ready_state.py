from atm import ATM
from card_manager.card_manager_factory import CardManagerFactory
from data import ATMState, CardDetails
from db import DBAccessor
from state import State, CardReadingState, CardEjectingState, StateFactory


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

    def read_card(self, card_details: CardDetails) -> None:
        raise ValueError("Invalid operation. Illegal state exception")

    def cancel_transaction(self, transaction_id: str) -> bool:
        DBAccessor.cancel_transaction(transaction_id)
        state_ready = StateFactory.get_state(ATMState.READY, self.__atm)
        self.__atm.change_state(state_ready)
        return True

    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        raise ValueError("Invalid operation. Illegal state exception")

    def dispense_cash(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def eject_card(self):
        raise ValueError("Invalid operation. Illegal state exception")

    @property
    def state_name(self) -> ATMState:
        return ATMState.READY
