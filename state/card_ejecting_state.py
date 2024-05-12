from atm import ATM
from data import ATMState, CardDetails
from state import State, ReadyState, StateFactory


class CardEjectingState(State):
    __atm: ATM

    def __init__(self, atm):
        self.__atm = atm

    def init(self):
        raise ValueError("Invalid operation. Illegal state exception")

    def cancel_transaction(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def read_card(self, card_details: CardDetails) -> None:
        raise ValueError("Invalid operation. Illegal state exception")

    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        raise ValueError("Invalid operation. Illegal state exception")

    def dispense_cash(self, transaction_id: int) -> bool:
        raise ValueError("Invalid operation. Illegal state exception")

    def eject_card(self):
        state_ready = StateFactory.get_state(ATMState.READY, self.__atm)
        self.__atm.change_state(state_ready)

    @property
    def state_name(self) -> ATMState:
        return ATMState.CARD_EJECTING
