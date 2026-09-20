class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    def get_masked_account(self):
        return "XXXXXX" + self.__account_number[-4:]

    def get_balance(self):
        return self.__balance

    def debit(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def credit(self, amount):
        self.__balance += amount