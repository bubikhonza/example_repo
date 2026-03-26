from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

class CreditAccount(Account):
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount
        return amount

class SpecialAccount(Account):
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += amount + 1000

    def withdraw(self, amount: int):
        pass

account1 = SpecialAccount(owner_name="Honza")
account2 = CreditAccount(owner_name="Honza")
account3 = CreditAccount(owner_name="Honza")


accounts = [account1, account2, account3]

for account in accounts:
    account.deposit(1000)


