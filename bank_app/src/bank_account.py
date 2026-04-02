from bank_app.src.currency_converter import CurrencyConverter
from bank_app.src.enums import Currency


class BankAccount:
    def __init__(self, owner: str, currency: Currency, currency_converter: CurrencyConverter) -> None:
        self.__owner = owner
        self.__currency = currency
        self.__balance = 0
        self.__currency_converter = currency_converter

    def deposit(self, amount: float, currency: Currency) -> None:
        if currency != self.__currency:
            converted_amount = self.__currency_converter.convert(
                amount=amount,
                source_currency=currency,
                target_currency=self.__currency)
        else:
            converted_amount = amount
        self.__balance += converted_amount

    def withdraw(self, amount: float, currency: Currency) -> float:
        if currency != self.__currency:
            converted_amount = self.__currency_converter.convert(
                amount=amount,
                source_currency=self.__currency,
                target_currency=currency)
        else:
            converted_amount = amount
        self.__balance -= converted_amount
        return converted_amount

    def get_balance(self) -> float:
        return self.__balance