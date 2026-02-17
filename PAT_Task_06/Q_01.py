class BankAccount:
    def __init__(self, acc_no, opening_balance):
        self.acc_no = acc_no
        self.__balance = opening_balance   # balance is private "__"
    def deposit_amount(self, amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            print("Amount deposited:", amt)
        else:
            print("Deposit amount must be positive")
    def withdraw_amount(self, amt):
        if amt <= self.__balance:
            self.__balance = self.__balance - amt
            print("Amount withdrawn:", amt)
        else:
            print("Not enough balance")
    def show_balance(self):
        return self.__balance
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, opening_balance, rate):
        super().__init__(acc_no, opening_balance)
        self.rate = rate
    def add_interest(self):
        interest = (self.show_balance() * self.rate) / 100
        self.deposit_amount(interest)
        print("Interest credited:", interest)
class CurrentAccount(BankAccount):
    def __init__(self, acc_no, opening_balance, min_bal):
        super().__init__(acc_no, opening_balance)
        self.min_bal = min_bal
    def withdraw_amount(self, amt):
        if self.show_balance() - amt >= self.min_bal:
            super().withdraw_amount(amt)
        else:
            print("Withdrawal denied due to minimum balance rule")

sa = SavingsAccount("HEM01", 4000, 4)
sa.deposit_amount(1000)
sa.add_interest()
print("Final balance:", sa.show_balance())


ca = CurrentAccount("Nasi02", 7000, 2000)
ca.withdraw_amount(3000)
print("Final balance:", ca.show_balance())
