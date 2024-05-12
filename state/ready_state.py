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
        valid_card = (CardManagerFactory
                      .get_card_manager(CardDetails.card_type)
                      .validate_card(card_details))
        DBAccessor.persist_card_details(card_details, self.__atm.machine_id)
        if valid_card:
            state_withdraw_details_reading = (
                StateFactory().get_state(ATMState.WITHDRAWAL_DETAILS_READING, self.__atm))
            self.__atm.change_state(state_withdraw_details_reading)
        else:
            DBAccessor.disapprove_transaction(self.__atm.machine_id)
            # ENUM would be needed for transaction status, let's define.
            state_ready = StateFactory().get_state(ATMState.READY, self.__atm)
            self.__atm.change_state(state_ready)

    def cancel(self, transaction_id: str) -> bool:
        DBAccessor.cancel_transaction(transaction_id)
        state_ready = StateFactory().get_state(ATMState.READY, self.__atm)
        self.__atm.change_state(state_ready)
        return True

    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        pass

    def despense_cash(self, transaction_id: int) -> bool:
        pass

    def eject_card(self):
        pass

    @property
    def state_name(self) -> ATMState:
        return ATMState.READY
