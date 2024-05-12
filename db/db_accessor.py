# OopCompanion:suppressRename
from data import ATMState, CardDetails, TransactionStatus


class DBAccessor:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_state(atm_machine_id: str) -> ATMState:
        """Simulated. In reality, this function to connect to db &
        retrieve state & return
        """
        return ATMState.READY

    @staticmethod
    def create_new_transaction(machine_id: str) -> int:
        """To be implemented
        """
        return 1

    @staticmethod
    def update_atm_state(machine_id: str, state: ATMState):
        pass

    @staticmethod
    def persist_card_details(card_details: CardDetails,
                             machine_id: str):
        pass

    @staticmethod
    def disapprove_transaction(machine_id: str):
        pass

    @staticmethod
    def cancel_transaction(transaction_id: str):
        pass

    @staticmethod
    def persist_withdrawal_details(transaction_id: str,
                                   amount: float,
                                   transaction_status: TransactionStatus):
        pass

    @staticmethod
    def mark_as_executed(transaction_id: str) -> float:
        pass
