from atm import ATM
from data import ATMState, CardDetails
from state import State, CardEjectingState, ReadyState


class CardReadingState(State):
    __atm: ATM

    def __init__(self, atm: ATM):
        self.__atm = atm

    def init(self):
        self.__atm.change_state(ReadyState(self.__atm))

    def cancel_transaction(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def read_card(self, card_details: CardDetails) -> None:
        pass

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
