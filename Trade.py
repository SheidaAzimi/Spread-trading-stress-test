class SpreadTrade:

    def __init__(self, cash_position, futures_position):
        self.cash_position = cash_position
        self.futures_position = futures_position

    def pnl(self, old_market, new_market):

        cash_pnl = (new_market.cash_price - old_market.cash_price) * self.cash_position
        futures_pnl = (new_market.futures_price - old_market.futures_price) * self.futures_position

        return cash_pnl + futures_pnl
