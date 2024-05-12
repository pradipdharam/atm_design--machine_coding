from abc import ABC, abstractmethod

from data import CardDetails


class CardManager(ABC):
    @abstractmethod
    def validate_card(self, card_details: CardDetails):
        pass

    @abstractmethod
    def validate_withdrawal(self, amount: float, transaction_id: int) -> bool:
        pass

    @abstractmethod
    def execute_withdrawal(self, transaction_id: int) -> bool:
        pass
