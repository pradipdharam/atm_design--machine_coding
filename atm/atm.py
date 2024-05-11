from typing import Final

from data import ATMState
from state import State, ReadyState, CardReadingState


class ATM:
    """No two transactions should be initiated at a same time on one ATM.
    Translations should be initiated one after another
    This can be achieved using assigning a state to the specific machine.
    Depending on what state the APM machine is in, there needs to be
    access modifier for each of the method
    """

    __machine_id: Final[str]
    __state: State

    def __init__(self, machine_id):
        self.__machine_id = machine_id
        self.__state = ReadyState(__class__(self))

    def init(self) -> int:
        """ Moving this logc to respective concreate classes of State
        state1 --> init --> state2
        state3 --> init --> state4
        when __state.init() is called, it's not necessary that
        ATM goes to one specific state CardReadingState
        """
        return self.__state.init()


    def cancel(self, transaction_id: int) -> bool:
        """ Sets the ATM in card ejecting state from any state
        Once the card is ejected, ATM goes to ready state.
        """
        self.__state.cancel(transaction_id)

    def read_card(self, card_type: str,
                  card_num: int, pin: int) -> None:
        if self.__atm_state == ATMState.CARD_READING:
            pass
        if self.__atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            pass
        if self.__atm_state == ATMState.CASH_DISPENSING:
            pass
        if self.__atm_state == ATMState.READY:
            pass

        return True

    def read_withdrawal_details(self, card_type: str,
                                card_num: int, pin: int):
        if self.__atm_state == ATMState.CARD_READING:
            pass
        if self.__atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            pass
        if self.__atm_state == ATMState.CASH_DISPENSING:
            pass
        if self.__atm_state == ATMState.READY:
            pass
        return True

    def despense_cash(self, transaction_id: int) -> bool:
        if self.__atm_state == ATMState.CARD_READING:
            pass
        if self.__atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            pass
        if self.__atm_state == ATMState.CASH_DISPENSING:
            pass
        if self.__atm_state == ATMState.READY:
            pass
        return True

    def eject_card(self):
        if self.__atm_state == ATMState.CARD_READING:
            pass
        if self.__atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            pass
        if self.__atm_state == ATMState.CASH_DISPENSING:
            pass
        if self.__atm_state == ATMState.READY:
            pass
        pass

    def change_state(self, new_state: State):
        self.__state = new_state
