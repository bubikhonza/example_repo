from bank_app.src.bank_account import BankAccount
from bank_app.src.currency_converter import CurrencyConverter
from bank_app.src.enums import Currency
from bank_app.src.exchange_client import ExchangeClient


exchange_client = ExchangeClient()
currency_converter = CurrencyConverter(
    exchange_client=exchange_client
)
bank_acc = BankAccount(owner="Honza",
                       currency=Currency.CZK,
                       currency_converter=currency_converter)

print(bank_acc.get_balance())

bank_acc.deposit(amount=5, currency=Currency.USD)
print(bank_acc.get_balance())


bank_acc.withdraw(amount=5, currency=Currency.CZK)
print(bank_acc.get_balance())
