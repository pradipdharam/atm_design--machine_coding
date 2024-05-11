from typing import Final

from data import ATMState


class ATM:
    """No two transactions should be initiated at a same time on one ATM.
    Translations should be initiated one after another
    This can be achieved using assigning a state to the specific machine.
    Depending on what state the APM machine is in, there needs to be
    access modifier for each of the method
    """

    __machine_id: Final[str]
    __atm_state: ATMState

    def init(self) -> int:
        """Returns transaction number.
        Transaction to be initiated only when ATM state is READY
        """
        transaction_id = 0
        # logic to generate the unique translation id,
        # after connecting to db etc. then persist in db for future reference etc.

        if self.__atm_state == ATMState.CARD_READING:
            raise RuntimeError("New transaction cannot be initiated. Please wait to complete previous transaction")
        if self.__atm_state == ATMState.WITHDRAWAL_DETAILS_READING:
            raise RuntimeError("New transaction cannot be initiated. Please wait to complete previous transaction")
        if self.__atm_state == ATMState.CASH_DISPENSING:
            raise RuntimeError("New transaction cannot be initiated. Please wait to complete previous transaction")

        # Code here looks bulky, not a good idea.
        # For each state, there is separate method, as defined below.
        return transaction_id

    def cancel(self, transaction_id: int) -> bool:
        """ Sets the ATM in card ejecting state from any state
        Once the card is ejected, ATM goes to ready state.
        """

        return True

    def read_card(self, card_type: str,
                  card_num: int, pin: int) -> None:
        return True

    def read_withdrawal_details(self, card_type: str,
                                card_num: int, pin: int):
        return True

    def despense_cash(self, transaction_id: int) -> bool:
        return True

    def eject_card(self):
        pass
