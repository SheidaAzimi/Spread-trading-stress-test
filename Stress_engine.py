from market import MarketData
from trade import SpreadTrade

class StressTestEngine:

    def __init__(self, market, trade, scenarios):
        self.market = market
        self.trade = trade
        self.scenarios = scenarios

    def run(self):

        results = []

        for scenario in self.scenarios:

            new_cash, new_futures = scenario.apply(self.market)

            new_market = MarketData(new_cash, new_futures)

            pnl = self.trade.pnl(self.market, new_market)

            results.append((scenario.name, pnl))

        return results
