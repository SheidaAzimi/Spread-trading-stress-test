from market import MarketData
from trade import SpreadTrade
from scenario import Scenario
from stress_engine import StressTestEngine

market = MarketData(100, 98)

trade = SpreadTrade(cash_position=1, futures_position=-1)

scenarios = [

    Scenario("Spread Widening", 5, -2),
    Scenario("Spread Tightening", -2, 2),
    Scenario("Cash Leads", 4, 1),
    Scenario("Futures Leads", 1, 4)

]

engine = StressTestEngine(market, trade, scenarios)

results = engine.run()

for name, pnl in results:
    print(name, pnl)
