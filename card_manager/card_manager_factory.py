from card_manager import CardManager, CreditCardManager, DebitCardManager
from data import CardType


class CardManagerFactory:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_card_manager(self, card_type: CardType) -> CardManager:
        card_manager = None
        if card_type is CardType.CREDIT:
            card_manager = CreditCardManager()
        elif card_type is CardType.DEBIT:
            card_manager = DebitCardManager()
        else:
            raise RuntimeError("Invalid card type")
        return card_manager
