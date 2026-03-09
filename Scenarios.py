class Scenario:

    def __init__(self, name, cash_change, futures_change):
        self.name = name
        self.cash_change = cash_change
        self.futures_change = futures_change

    def apply(self, market):

        new_cash = market.cash_price + self.cash_change
        new_futures = market.futures_price + self.futures_change

        return new_cash, new_futures
