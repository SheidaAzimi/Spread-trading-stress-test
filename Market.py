class MarketData:

    def __init__(self, cash_price, futures_price):
        self.cash_price = cash_price
        self.futures_price = futures_price

    def spread(self):
        return self.cash_price - self.futures_price
      
