class BankAccount:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def verify_pin(self, pin):
        return self.__pin == pin 

    def get_balance(self):
        return self.__balance   

john_bank_account = BankAccount (balance=20000, pin="0000")

print(john_bank_account.verify_pin("0000"))
print(john_bank_account.get_balance())

        