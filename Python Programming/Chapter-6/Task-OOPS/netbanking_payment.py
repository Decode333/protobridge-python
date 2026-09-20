from payment import Payment


class NetBankingPayment(Payment):

    def __init__(self, amount, account, bank_name):
        super().__init__(amount, account)
        self.bank_name = bank_name

    def validate_payment(self):
        if not self.bank_name.strip():
            raise ValueError("Bank Name Required")

    def process_payment(self):
        self.validate_payment()
        self.account.debit(self.amount)

        print("\n=== NET BANKING SUCCESS ===")
        print(f"Bank   : {self.bank_name}")
        print(f"Amount : ₹{self.amount}")