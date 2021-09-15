import yfinance as yf

class tradingAlgo:
    def __init__(self, symbol):
        self.symbol = symbol
        # print("INIT " + )
        self.stock = yf.Ticker(self.symbol)
        self.currentPrice = self.stock.history(period='1d')['Close'][0]
        self.oneYearReturn = ((self.currentPrice / self.stock.history(period='1y')['Close'][0]) - 1) * 100
        self.sixMonthReturn = ((self.currentPrice / self.stock.history(period='180d')['Close'][0]) - 1) * 100
        self.threeMonthReturn = ((self.currentPrice / self.stock.history(period='90d')['Close'][0]) - 1) * 100
        self.oneMonthReturn = ((self.currentPrice / self.stock.history(period='30d')['Close'][0]) - 1) * 100
        self.fiveDayReturn = ((self.currentPrice / self.stock.history(period='5d')['Close'][0]) - 1) * 100
        self.fiftyDayAverage = self.stock.history(period='50d')['Close']
        self.twoHundredDayAverage = self.stock.history(period='200d')['Close']

        # print("oneYearReturn = " + str(self.oneYearReturn))

    def getSymbol(self):
        return self.symbol

    def value(self):
        print("Value based algorithm")

    # get 1 year return, maybe a more recent price return too
    # figure out percentile calculation from the freecodecamp video
    # stock with the best 1 year, 6 month, 3 month and 1 month weighted average
    # should get a better score
    def momentumAlgo(self):
        print("one year = " + str(self.oneYearReturn))
        print("six month = " + str(self.sixMonthReturn))
        print("three month = " + str(self.threeMonthReturn))
        print("one month = " + str(self.oneMonthReturn))
        print("five day = " + str(self.fiveDayReturn))
        return 0.0

    # take into account 10 year tresury
    def growthAlgo(self):
        print("Growth based algorithm")

    def composite(self):
        print("Composite of algorithms")

    # Give a rating on how close the stock is to crossing the 200 day moving average
    def getMovingAverageGap(self):
        avgFifty = sum(self.fiftyDayAverage) / len(self.fiftyDayAverage)
        avgtwoHundred = sum(self.twoHundredDayAverage) / len(self.twoHundredDayAverage)

        percentDiff = ((avgFifty / avgtwoHundred) - 1) * 100

        return percentDiff

    # The mean reversion strategy says highs and lows of a stock are only temporary.
    # They will revert to their mean value from time to time
    def getMeanReversion(self):
        # Block to get daily high and daily low stock price
        yearlyHigh = self.stock.info['fiftyTwoWeekHigh']
        yearlyLow = self.stock.info['fiftyTwoWeekLow']

    #   Just add yearly high and yearly low then divide by 2
        meanReversion = (yearlyHigh + yearlyLow) / 2

        return meanReversion

# Main entry point
if __name__ == '__main__':
    algo = tradingAlgo("TSLA")
    print("TradingAlgo.py main. Testing: " + str(algo.getSymbol()))

    # print("Testing Mean Reversion:")
    # meanReversion = algo.getMeanReversion()
    # print("/getMeanReversion returned: " + str(meanReversion))

    # print("Testing Momentum Algo:")
    # momentum = algo.momentumAlgo()
    # print("/momentumAlgo returned: " + str(momentum))

    print("Testing 50day / 200day:")
    fiftyDay = algo.getMovingAverageGap()
    formatFiftyDay = "{:.5f}".format(fiftyDay)
    if fiftyDay > 0:
        print("/getMovingAverageGap returned: +" + str(formatFiftyDay) +"%")
    else:
        print("/getMovingAverageGap returned: -" + str(formatFiftyDay) +"%")
