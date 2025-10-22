class BankAccount:
    def __init__(self, account_number, account_holder, balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self. account_type = account_type


account1= BankAccount(12345678, "Krista", 5000, "Savings")
account2= BankAccount(987654321, "Mira", 12000, "Current")

print(account1.account_holder)