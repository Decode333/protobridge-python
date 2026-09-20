from payment import Payment


class CreditCardPayment(Payment):

    def __init__(self, amount, account, card_number):
        super().__init__(amount, account)
        self.card_number = card_number

    def validate_payment(self):
        if len(self.card_number) != 16:
            raise ValueError("Invalid Card Number")

    def process_payment(self):
        self.validate_payment()
        self.account.debit(self.amount)

        print("\n=== CARD PAYMENT SUCCESS ===")
        print(f"Card Ending : {self.card_number[-4:]}")
        print(f"Amount      : ₹{self.amount}")