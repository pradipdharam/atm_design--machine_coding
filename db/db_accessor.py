# OopCompanion:suppressRename
from data import ATMState, CardDetails


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
    def create_new_transaction(self, machine_id: str) -> int:
        """To be implemented
        """
        return 1

    @staticmethod
    def update_atm_state(machine_id: str, state: ATMState):
        pass

    def persist_card_details(self, card_details: CardDetails,
                             machine_id: str):
        pass

    def disapprove_transaction(self, machine_id: str):
        pass
