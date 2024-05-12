# OopCompanion:suppressRename
from data import ATMState


class DBAccessor:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_state(atm_machine_id: str) -> ATMState:
        """Simulated. In reality, this function to connect to db &
        retrieve state & return
        """
        return ATMState.READY
