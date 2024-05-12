from atm import ATM
from card_manager import CardManagerFactory
from data import ATMState, CardDetails
from db import DBAccessor
from state import State, StateFactory


class CardReadingState(State):
    __atm: ATM

    def __init__(self, atm: ATM):
        self.__atm = atm

    def init(self):
        raise ValueError("Invalid operation. Illegal state exception")

    def cancel_transaction(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def read_card(self, card_details: CardDetails) -> None:
        valid_card = (CardManagerFactory
                      .get_card_manager(CardDetails.card_type)
                      .validate_card(card_details))
        DBAccessor.persist_card_details(card_details, self.__atm.machine_id)
        if valid_card:
            state_withdraw_details_reading = (
                StateFactory.get_state(ATMState.WITHDRAWAL_DETAILS_READING, self.__atm))
            self.__atm.change_state(state_withdraw_details_reading)
        else:
            DBAccessor.disapprove_transaction(self.__atm.machine_id)
            # ENUM would be needed for transaction status, let's define.
            state_ready = StateFactory.get_state(ATMState.READY, self.__atm)
            self.__atm.change_state(state_ready)

    def read_withdrawal_details(self, card_type: str,
                                card_num: int, pin: int):
        raise ValueError("Invalid operation. Illegal state exception")

    def dispense_cash(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def eject_card(self):
        raise ValueError("Invalid operation. Illegal state exception")

    @property
    def state_name(self) -> ATMState:
        return ATMState.CARD_READING
