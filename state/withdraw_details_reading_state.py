from state import State


class WithdrawDetailsReadingState(State):
    def init(self) -> int:
        pass

    def cancel(self, transaction_id: int) -> bool:
        pass

    def read_card(self, card_type: str, card_num: int, pin: int) -> None:
        pass

    def read_withdrawal_details(self, card_type: str, card_num: int, pin: int):
        pass

    def despense_cash(self, transaction_id: int) -> bool:
        pass

    def eject_card(self):
        pass