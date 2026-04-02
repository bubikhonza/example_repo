import pytest
from unittest.mock import MagicMock, patch
from bank_app.src.bank_account import BankAccount
from bank_app.src.currency_converter import CurrencyConverter
from bank_app.src.enums import Currency
from bank_app.src.exchange_client import ExchangeClient


@pytest.fixture
def exchange_client():
    exchange_client_mock = MagicMock(spec=ExchangeClient)
    exchange_client_mock.get_exchange_rate.return_value = 2
    return exchange_client_mock


@pytest.fixture
def currency_converter(exchange_client):
    return CurrencyConverter(
        exchange_client=exchange_client
    )


@pytest.fixture
def bank_acc_czk(currency_converter):
    bank_acc = BankAccount(owner="Test", currency=Currency.CZK, currency_converter=currency_converter)
    return bank_acc


def test_acc_is_0_when_created(bank_acc_czk):
    assert bank_acc_czk.get_balance() == 0


@pytest.mark.parametrize(
    "amount,currency,expected_balance", [
        (10, Currency.CZK, -10),
        (0, Currency.CZK, 0),
        (0, Currency.EUR, 0),
        (10, Currency.EUR, -20),
    ]
)
def test_withdraw(amount, currency, expected_balance, bank_acc_czk):
    bank_acc_czk.withdraw(amount=amount, currency=currency)
    assert bank_acc_czk.get_balance() == expected_balance



@patch.object(ExchangeClient, 'get_exchange_rate', return_value=100)
def test_withdraw_with_patch(mock_method):
    ex_cl = ExchangeClient()
    result = ex_cl.get_exchange_rate(source_currency=Currency.USD, target_currency=Currency.CZK)
    assert result == 100


# co nedelat
# class Blabla:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# def test_blabla():
#     blabla = Blabla(1, 2, 3)
#     assert blabla.x == 1
#     assert blabla.y == 2
#     assert blabla.z == 3