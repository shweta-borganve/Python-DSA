class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def deposit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    def withdraw(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)

acc1.deposit(500)
print(acc1.get_balance()) 