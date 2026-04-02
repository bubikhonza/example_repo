from bank_app.src.enums import Currency
import random


class ExchangeClient:
    def get_exchange_rate(self,
                          source_currency: Currency,
                          target_currency: Currency):
        # requests.get(....)
        return random.uniform(1, 2)
