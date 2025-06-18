from abc import ABC, abstractmethod

# ✅ Abstract Base Class for Bank Accounts
class BankAccount(ABC):
    def __init__(self, amount, holder):
        # Set initial balance and account holder name
        self.amount = amount
        self.holder = holder

    def deposite(self, x):
        # Increase balance by x amount
        self.amount += x

    @abstractmethod
    def withdraw(self, x):
        # Abstract method to enforce custom withdrawal rules in child classes
        pass

    def print_details(self):
        # Print current balance and holder name
        print("Amount:", self.amount)
        print("Holder:", self.holder)


# ✅ Current Account Class
class CurrAccount(BankAccount):
    def __init__(self, amount, owner, overdraft):
        # Initialize parent class
        super().__init__(amount, owner)
        # Set overdraft limit for the account
        self.overdraft = overdraft

    def withdraw(self, x):
        # Allow withdrawal within balance + overdraft
        if x < self.amount + self.overdraft:
            self.amount -= x
        else:
            raise ValueError("Withdrawal exceeds overdraft limit")


# ✅ Savings Account Class
class SavingsAccount(BankAccount):
    def __init__(self, amount, owner, interest_rate):
        # Initialize parent class
        super().__init__(amount, owner)
        # Store interest rate for savings
        self.interest_rate = interest_rate

    def add_interest(self):
        # Calculate interest and add to balance
        interest = self.amount * self.interest_rate / 100
        self.amount += interest

    def withdraw(self, x):
        # Prevent overdraft: allow only if balance is enough
        if x > self.amount:
            raise ValueError("Not enough balance in savings account")
        self.amount -= x

    def __str__(self):
        # String representation of the savings account
        return f"SavingsAccount(holder={self.holder}, amount={self.amount}, interest_rate={self.interest_rate}%)"


# ✅ Demo of SavingsAccount
sa = SavingsAccount(70, "Prince", 5)

sa.print_details()     # Prints: 70
sa.deposite(30)        # Deposit 30 → total: 100
sa.print_details()
sa.add_interest()      # Add 5% interest → total: 105.0
sa.print_details()

# ✅ Demo of CurrAccount
ca = CurrAccount(100, "Prince", 50)

ca.print_details()     # Prints: 100
ca.withdraw(130)       # Withdraw 130 (within overdraft limit)
ca.print_details()     # Prints: -30


