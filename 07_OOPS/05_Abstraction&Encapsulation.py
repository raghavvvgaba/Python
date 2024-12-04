class Account: 
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    def credit(self, amount):
        self.balance = self.balance + amount
        return
    def debit(self, amount):
        self.balance = self.balance - amount
        return
    def print_balance(self):
        print(self.balance)
        return
Raghav = Account(140000, 1234567890)
Raghav.debit(5000)
Raghav.credit(40)
Raghav.print_balance()