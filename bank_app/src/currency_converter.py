from bank_app.src.exchange_client import ExchangeClient
from bank_app.src.enums import Currency


class CurrencyConverter:
    def __init__(self, exchange_client: ExchangeClient) -> None:
        self.exchange_client = exchange_client

    def convert(self,
                amount: float,
                source_currency: Currency,
                target_currency: Currency) -> float:
        rate = self.exchange_client.get_exchange_rate(source_currency, target_currency)
        result = amount * rate
        return result
