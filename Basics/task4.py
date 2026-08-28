class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)

acc = BankAccount("Noman", 1000)

acc.show_balance()
acc.deposit(500)
acc.show_balance()
acc.withdraw(200)
acc.show_balance()