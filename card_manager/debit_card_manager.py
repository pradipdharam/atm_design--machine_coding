from card_manager import CardManager
from data import CardDetails


class DebitCardManager(CardManager):

    def validate_card(self, card_details: CardDetails):
        pass

    def validate_withdrawal(self, amount: float, transaction_id: int) -> bool:
        pass

    def execute_withdrawal(self, transaction_id: int) -> bool:
        pass
