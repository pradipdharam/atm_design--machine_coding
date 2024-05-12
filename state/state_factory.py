from atm import ATM
from data import ATMState
from state import State, ReadyState, CardReadingState, WithdrawDetailsReadingState, CashDespensingState, \
    CardEjectingState


class StateFactory:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_state(atm_state: ATMState, atm: ATM) -> State:
        state = None
        if atm_state is ATMState.READY:
            state = ReadyState(atm)
        elif atm_state is ATMState.CARD_READING:
            state = CardReadingState(atm)
        elif atm_state is ATMState.WITHDRAWAL_DETAILS_READING:
            state = WithdrawDetailsReadingState(atm)
        elif atm_state is ATMState.CASH_DISPENSING:
            state = CashDespensingState(atm)
        elif atm_state is ATMState.CARD_EJECTING:
            state = CardEjectingState(atm)
        else:
            raise RuntimeError("Invalid ATM state")
        return state
