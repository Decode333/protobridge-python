from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass