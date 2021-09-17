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

    # take into account 10 year tresury
    # take into account the % yearly gain the company is shooting for
    def value(self):
        print("Value based algorithm")

    #  Returns the percentile of momentum
    #  Low quality momentum stocks (those that are pump and dump) will get a
    #  far lower score than those of high quality, large gains over long time
    def momentumAlgo(self):
        # print("one year = " + str(self.oneYearReturn))
        # print("six month = " + str(self.sixMonthReturn))
        # print("three month = " + str(self.threeMonthReturn))
        # print("one month = " + str(self.oneMonthReturn))
        # print("five day = " + str(self.fiveDayReturn))
        oneYearPercentile = 0
        sixMonthPercentile = 0
        threeMonthPercentile = 0
        oneMonthPercentile = 0
        fiveDayPercentile = 0

        if self.oneYearReturn > 70:
            oneYearPercentile = 95
        elif self.oneYearReturn > 55:
            oneYearPercentile = 90
        elif self.oneYearReturn > 38:
            oneYearPercentile = 85
        elif self.oneYearReturn > 31:
            oneYearPercentile = 80
        elif self.oneYearReturn > 26:
            oneYearPercentile = 75
        elif self.oneYearReturn > 22:
            oneYearPercentile = 70
        elif self.oneYearReturn > 19:
            oneYearPercentile = 65
        elif self.oneYearReturn > 15:
            oneYearPercentile = 60
        elif self.oneYearReturn > 11:
            oneYearPercentile = 55
        elif self.oneYearReturn > 5:
            oneYearPercentile = 50
        elif self.oneYearReturn > 0:
            oneYearPercentile = 40
        elif self.oneYearReturn > -8:
            oneYearPercentile = 30
        elif self.oneYearReturn > -16:
            oneYearPercentile = 20
        elif self.oneYearReturn > -22:
            oneYearPercentile = 10
        else:
            oneYearPercentile = 5

        # print("oneYearPercentile = " + str(oneYearPercentile))

        if self.sixMonthReturn > 60:
            sixMonthPercentile = 95
        elif self.sixMonthReturn > 42:
            sixMonthPercentile = 90
        elif self.sixMonthReturn > 26:
            sixMonthPercentile = 85
        elif self.sixMonthReturn > 20:
            sixMonthPercentile = 80
        elif self.sixMonthReturn > 15:
            sixMonthPercentile = 75
        elif self.sixMonthReturn > 12:
            sixMonthPercentile = 70
        elif self.sixMonthReturn > 8:
            sixMonthPercentile = 65
        elif self.sixMonthReturn > 4:
            sixMonthPercentile = 60
        elif self.sixMonthReturn > 0:
            sixMonthPercentile = 55
        elif self.sixMonthReturn > -2:
            sixMonthPercentile = 50
        elif self.sixMonthReturn > -5:
            sixMonthPercentile = 40
        elif self.sixMonthReturn > -10:
            sixMonthPercentile = 30
        elif self.sixMonthReturn > -16:
            sixMonthPercentile = 20
        elif self.sixMonthReturn > -23:
            sixMonthPercentile = 10
        else:
            sixMonthPercentile = 5

        # print("sixMonthPercentile = " + str(sixMonthPercentile))

        if self.threeMonthReturn > 50:
            threeMonthPercentile = 95
        elif self.threeMonthReturn > 39:
            threeMonthPercentile = 90
        elif self.threeMonthReturn > 30:
            threeMonthPercentile = 85
        elif self.threeMonthReturn > 22:
            threeMonthPercentile = 80
        elif self.threeMonthReturn > 18:
            threeMonthPercentile = 75
        elif self.threeMonthReturn > 15:
            threeMonthPercentile = 70
        elif self.threeMonthReturn > 12:
            threeMonthPercentile = 65
        elif self.threeMonthReturn > 9:
            threeMonthPercentile = 60
        elif self.threeMonthReturn > 6:
            threeMonthPercentile = 55
        elif self.threeMonthReturn > 3:
            threeMonthPercentile = 50
        elif self.threeMonthReturn > 1:
            threeMonthPercentile = 40
        elif self.threeMonthReturn > 0:
            threeMonthPercentile = 30
        elif self.threeMonthReturn > -5:
            threeMonthPercentile = 20
        elif self.threeMonthReturn > -10:
            threeMonthPercentile = 10
        else:
            threeMonthPercentile = 5

        # print("threeMonthPercentile = " + str(threeMonthPercentile))

        if self.oneMonthReturn > 20:
            oneMonthPercentile = 95
        elif self.oneMonthReturn > 15:
            oneMonthPercentile = 90
        elif self.oneMonthReturn > 13:
            oneMonthPercentile = 85
        elif self.oneMonthReturn > 11:
            oneMonthPercentile = 80
        elif self.oneMonthReturn > 10:
            oneMonthPercentile = 75
        elif self.oneMonthReturn > 9:
            oneMonthPercentile = 70
        elif self.oneMonthReturn > 8:
            oneMonthPercentile = 65
        elif self.oneMonthReturn > 6:
            oneMonthPercentile = 60
        elif self.oneMonthReturn > 4:
            oneMonthPercentile = 55
        elif self.oneMonthReturn > 2:
            oneMonthPercentile = 50
        elif self.oneMonthReturn > 1:
            oneMonthPercentile = 40
        elif self.oneMonthReturn > 0:
            oneMonthPercentile = 30
        elif self.oneMonthReturn > -5:
            oneMonthPercentile = 20
        elif self.oneMonthReturn > -10:
            oneMonthPercentile = 10
        else:
            oneMonthPercentile = 5

        # print("oneMonthPercentile = " + str(oneMonthPercentile))

        if self.fiveDayReturn > 9:
            fiveDayPercentile = 95
        elif self.fiveDayReturn > 7.9:
            fiveDayPercentile = 90
        elif self.fiveDayReturn > 6.4:
            fiveDayPercentile = 85
        elif self.fiveDayReturn > 5.1:
            fiveDayPercentile = 80
        elif self.fiveDayReturn > 4:
            fiveDayPercentile = 75
        elif self.fiveDayReturn > 2.9:
            fiveDayPercentile = 70
        elif self.fiveDayReturn > 2:
            fiveDayPercentile = 65
        elif self.fiveDayReturn > 1.3:
            fiveDayPercentile = 60
        elif self.fiveDayReturn > 0.6:
            fiveDayPercentile = 55
        elif self.fiveDayReturn > 0.3:
            fiveDayPercentile = 50
        elif self.fiveDayReturn > 0:
            fiveDayPercentile = 40
        elif self.fiveDayReturn > -1:
            fiveDayPercentile = 30
        elif self.fiveDayReturn > -3:
            fiveDayPercentile = 20
        elif self.fiveDayReturn > -5:
            fiveDayPercentile = 10
        else:
            fiveDayPercentile = 5

        # print("fiveDayPercentile = " + str(fiveDayPercentile))

        momentumScore = (0.4 * oneYearPercentile) + (0.25 * sixMonthPercentile) + (0.2 * threeMonthPercentile) + (0.1 * oneMonthPercentile) + (0.05 * fiveDayPercentile)

        return momentumScore

    # take into account 10 year tresury
    # take into account the % yearly gain the company is shooting for
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
    algo = tradingAlgo("SQ")
    print("TradingAlgo.py main. Testing: " + str(algo.getSymbol()))

    # print("Testing Mean Reversion:")
    # meanReversion = algo.getMeanReversion()
    # print("/getMeanReversion returned: " + str(meanReversion))

    print("Testing Momentum Algo:")
    momentum = algo.momentumAlgo()
    print("/momentumAlgo returned: " + str(momentum) + "%")

    # print("Testing 50day / 200day:")
    # fiftyDay = algo.getMovingAverageGap()
    # formatFiftyDay = "{:.5f}".format(fiftyDay)
    # if fiftyDay > 0:
    #     print("/getMovingAverageGap returned: +" + str(formatFiftyDay) +"%")
    # else:
    #     print("/getMovingAverageGap returned: -" + str(formatFiftyDay) +"%")
