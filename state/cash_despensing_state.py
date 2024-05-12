from atm import ATM
from card_manager import CardManagerFactory
from data import ATMState, CardDetails
from db import DBAccessor
from state import State, StateFactory


class CashDespensingState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self):
        raise ValueError("Invalid operation")

    def cancel(self, transaction_id: str) -> bool:
        DBAccessor.cancel_transaction(transaction_id)
        state_card_ejecting = StateFactory.get_state(ATMState.CARD_EJECTING, self.__atm)
        self.__atm.change_state(state_card_ejecting)
        return True

    def read_card(self, card_details: CardDetails) -> None:
        raise ValueError("Invalid operation")

    def read_withdrawal_details(self, card_type: str,
                                card_num: int, pin: int):
        raise ValueError("Invalid operation")

    def dispense_cash(self, transaction_id: str) -> float:
        # retrieve the card type based on may be transaction id
        card_type = None
        #
        CardManagerFactory.get_card_manager(card_type).execute_withdrawal(transaction_id)
        state_cash_dispensing = StateFactory.get_state(ATMState.CASH_DISPENSING, self.__atm)
        self.__atm.change_state(state_cash_dispensing)
        return DBAccessor.mark_as_executed(transaction_id)

    def eject_card(self):
        raise ValueError("Invalid operation")

    @property
    def state_name(self) -> ATMState:
        return ATMState.CASH_DISPENSING
