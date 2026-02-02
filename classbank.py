class BankAccount:
    def __init__(self, account_no, balance=0.0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited:{amount}. New balance:{self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw:{amount}. updated amount:{self.balance}")
        elif amount > self.balance:
            print("insufficient balance")
        else:
            print("withdraw amount must be positive")

    def check_balance(self):
        print(f"Account:{self.account_no}")
        print(f"Balance:{self.balance}")

account = BankAccount("123456", 10000)
account.deposit(500)
account.withdraw(100)
account.check_balance()