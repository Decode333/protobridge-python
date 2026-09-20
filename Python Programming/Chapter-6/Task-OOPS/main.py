from account import BankAccount
from upi_payment import UPIPayment
from creditcard_payment import CreditCardPayment
from netbanking_payment import NetBankingPayment


def main():

    account = BankAccount(
        account_holder="Nithin Raj",
        account_number="123456789012",
        balance=50000
    )

    print("=" * 40)
    print("INITIAL BALANCE:", account.get_balance())
    print("=" * 40)

    payments = [
        UPIPayment(
            amount=1000,
            account=account,
            upi_id="nithin@ybl"
        ),
        CreditCardPayment(
            amount=2000,
            account=account,
            card_number="1234567812345678"
        ),
        NetBankingPayment(
            amount=3000,
            account=account,
            bank_name="HDFC Bank"
        )
    ]

    # Polymorphism
    for payment in payments:
        payment.process_payment()

    print("\nRemaining Balance:",
          account.get_balance())


if __name__ == "__main__":
    main()