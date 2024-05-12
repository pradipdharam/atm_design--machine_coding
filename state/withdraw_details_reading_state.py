from atm import ATM
from card_manager import CardManagerFactory
from data import ATMState, CardDetails, TransactionStatus
from db import DBAccessor
from state import State, StateFactory


class WithdrawDetailsReadingState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self):
        raise ValueError("Invalid operation. Illegal state exception")

    def cancel_transaction(self, transaction_id: str) -> bool:
        DBAccessor.cancel_transaction(transaction_id)
        state_card_ejecting = StateFactory.get_state(ATMState.CARD_EJECTING, self.__atm)
        self.__atm.change_state(state_card_ejecting)
        return True

    def read_card(self, card_details: CardDetails) -> None:
        raise ValueError("Invalid operation. Illegal state exception")

    def read_withdrawal_details(self, card_details: CardDetails,
                                amount: float, transaction_id: str):
        valid_withdrawal = (CardManagerFactory
                            .get_card_manager(CardDetails.card_type)
                            .validate_withdrawal(amount, transaction_id))
        if valid_withdrawal:
            state_cash_dispensing = StateFactory.get_state(ATMState.CASH_DISPENSING, self.__atm)
            self.__atm.change_state(state_cash_dispensing)
            DBAccessor.persist_withdrawal_details(transaction_id, amount,
                                                  TransactionStatus.APPROVED)
            return True
        else:
            DBAccessor.disapprove_transaction(self.__atm.machine_id)
            state_ready = StateFactory.get_state(ATMState.READY, self.__atm)
            self.__atm.change_state(state_ready)
            DBAccessor.persist_withdrawal_details(transaction_id, amount,
                                                  TransactionStatus.NOT_APPROVED)
            return False


    def dispense_cash(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def eject_card(self):
        raise ValueError("Invalid operation. Illegal state exception")

    @property
    def state_name(self) -> ATMState:
        return ATMState.WITHDRAWAL_DETAILS_READING
