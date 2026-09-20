from payment import Payment


class UPIPayment(Payment):

    def __init__(self, amount, account, upi_id):
        super().__init__(amount, account)
        self.upi_id = upi_id

    def validate_payment(self):
        if "@" not in self.upi_id:
            raise ValueError("Invalid UPI ID")

    def process_payment(self):
        self.validate_payment()
        self.account.debit(self.amount)

        print("\n=== UPI PAYMENT SUCCESS ===")
        print(f"UPI ID : {self.upi_id}")
        print(f"Amount : ₹{self.amount}")