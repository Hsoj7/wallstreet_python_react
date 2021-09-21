import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd

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

        # This is a different library from the one above. I couldn't get the current PE ratio from yfinance
        # quoteTable['value'][13] gives the PE ratio. IF this ever changes, print(quoteTable) and find the row x column
        quoteTable = si.get_quote_table(self.symbol, dict_result=False)
        # print(quoteTable)
        self.pe = quoteTable['value'][13]

        self.priceToBook = self.stock.info['priceToBook']
        # print("book = " + str(self.priceToBook))
        self.priceToSales = self.stock.info['priceToSalesTrailing12Months']
        # print("priceToSales = " + str(self.priceToSales))

        self.marketCap = quoteTable['value'][11]
        # print("marketCap = " + str(self.marketCap))
        self.totalDebt = self.stock.info['totalDebt']
        # print("totalDebt = " + str(self.totalDebt))
        self.totalCash = self.stock.info['totalCash']
        # print("totalCash = " + str(self.totalCash))

        length = len(self.marketCap)
        char = self.marketCap[length-1:length]
        # print("char = " + char)
        self.marketCap = self.marketCap[0:length-1]
        self.marketCap = float(self.marketCap)
        if char == 'B':
            self.marketCap = self.marketCap * 1000000000
        elif char == 'M':
            self.marketCap = self.marketCap * 1000000
        elif char == 'T':
            self.marketCap = self.marketCap * 1000000000000


        # EV represents a theoretical takeover price if a company were to be bought
        # Can be a better value than pure marketCap
        enterpriseValue = self.marketCap + self.totalDebt - self.totalCash
        # print("enterpriseValue = " + str(enterpriseValue))
        self.ev_to_ebitda = enterpriseValue / (self.stock.info['ebitda'])
        # print("ev_to_ebitda = " + str(self.ev_to_ebitda))

        self.ev_to_grossProfit = enterpriseValue / self.stock.info['grossProfits']
        # print("ev_to_grossProfit = " + str(self.ev_to_grossProfit))


    def getSymbol(self):
        return self.symbol

    # if pe is negative, give it a 0 rating. negative means the company isn't making money yet and
    # from a value perspective, 0 earnings sucks.
    # Also, stocks with pe in the hundreds should get a lower value rating
    def valueAlgo(self):
        PePercentile = 0
        PbPercentile = 0
        PsPercentile = 0
        # enterprise value to ebitda
        EVEBITDAPercentile = 0
        # enterprise value to gross profit
        EVGPPercentile = 0

        if self.pe > 200:
            PePercentile = 95
        elif self.pe > 100:
            PePercentile = 90
        elif self.pe > 60:
            PePercentile = 85
        elif self.pe > 44:
            PePercentile = 80
        elif self.pe > 38:
            PePercentile = 75
        elif self.pe > 34:
            PePercentile = 70
        elif self.pe > 31:
            PePercentile = 65
        elif self.pe > 28:
            PePercentile = 60
        elif self.pe > 26:
            PePercentile = 55
        elif self.pe > 24:
            PePercentile = 50
        elif self.pe > 22:
            PePercentile = 45
        elif self.pe > 20:
            PePercentile = 40
        elif self.pe > 18:
            PePercentile = 35
        elif self.pe > 16:
            PePercentile = 30
        elif self.pe > 15:
            PePercentile = 25
        elif self.pe > 14:
            PePercentile = 20
        elif self.pe > 12:
            PePercentile = 15
        elif self.pe > 0:
            PePercentile = 10
        else:
            PePercentile = 5

        print("PE percentile = " + str(PePercentile))

        if self.priceToBook > 28:
            PbPercentile = 95
        elif self.priceToBook > 22:
            PbPercentile = 90
        elif self.priceToBook > 17:
            PbPercentile = 85
        elif self.priceToBook > 12:
            PbPercentile = 80
        elif self.priceToBook > 7.2:
            PbPercentile = 75
        elif self.priceToBook > 6.2:
            PbPercentile = 70
        elif self.priceToBook > 5.4:
            PbPercentile = 65
        elif self.priceToBook > 4.7:
            PbPercentile = 60
        elif self.priceToBook > 4.0:
            PbPercentile = 55
        elif self.priceToBook > 3.4:
            PbPercentile = 50
        elif self.priceToBook > 2.8:
            PbPercentile = 45
        elif self.priceToBook > 2.3:
            PbPercentile = 40
        elif self.priceToBook > 1.9:
            PbPercentile = 35
        elif self.priceToBook > 1.6:
            PbPercentile = 30
        elif self.priceToBook > 1.3:
            PbPercentile = 25
        elif self.priceToBook > 1.0:
            PbPercentile = 20
        elif self.priceToBook > 0.7:
            PbPercentile = 15
        elif self.priceToBook > 0.4:
            PbPercentile = 10
        else:
            PbPercentile = 5

        print("Price-Book percentile = " + str(PbPercentile))

        if self.priceToSales > 14:
            PsPercentile = 95
        elif self.priceToSales > 11:
            PsPercentile = 90
        elif self.priceToSales > 8:
            PsPercentile = 85
        elif self.priceToSales > 6.2:
            PsPercentile = 80
        elif self.priceToSales > 5.2:
            PsPercentile = 75
        elif self.priceToSales > 4.75:
            PsPercentile = 70
        elif self.priceToSales > 4.5:
            PsPercentile = 65
        elif self.priceToSales > 4.15:
            PsPercentile = 60
        elif self.priceToSales > 3.8:
            PsPercentile = 55
        elif self.priceToSales > 3.4:
            PsPercentile = 50
        elif self.priceToSales > 3.1:
            PsPercentile = 45
        elif self.priceToSales > 2.7:
            PsPercentile = 40
        elif self.priceToSales > 2.3:
            PsPercentile = 35
        elif self.priceToSales > 1.9:
            PsPercentile = 30
        elif self.priceToSales > 1.5:
            PsPercentile = 25
        elif self.priceToSales > 1.1:
            PsPercentile = 20
        elif self.priceToSales > 0.7:
            PsPercentile = 15
        elif self.priceToSales > 0.3:
            PsPercentile = 10
        else:
            PsPercentile = 5

        print("Price-Sales percentile = " + str(PsPercentile))




        # Do the EV percentiles



        return 0

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

        if self.oneYearReturn > 59:
            oneYearPercentile = 95
        elif self.oneYearReturn > 50:
            oneYearPercentile = 90
        elif self.oneYearReturn > 41:
            oneYearPercentile = 85
        elif self.oneYearReturn > 34:
            oneYearPercentile = 80
        elif self.oneYearReturn > 27:
            oneYearPercentile = 75
        elif self.oneYearReturn > 22:
            oneYearPercentile = 70
        elif self.oneYearReturn > 18:
            oneYearPercentile = 65
        elif self.oneYearReturn > 14:
            oneYearPercentile = 60
        elif self.oneYearReturn > 10:
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

        if self.sixMonthReturn > 45:
            sixMonthPercentile = 95
        elif self.sixMonthReturn > 37:
            sixMonthPercentile = 90
        elif self.sixMonthReturn > 28:
            sixMonthPercentile = 85
        elif self.sixMonthReturn > 21:
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

        if self.threeMonthReturn > 38:
            threeMonthPercentile = 95
        elif self.threeMonthReturn > 31:
            threeMonthPercentile = 90
        elif self.threeMonthReturn > 24:
            threeMonthPercentile = 85
        elif self.threeMonthReturn > 18:
            threeMonthPercentile = 80
        elif self.threeMonthReturn > 14:
            threeMonthPercentile = 75
        elif self.threeMonthReturn > 11:
            threeMonthPercentile = 70
        elif self.threeMonthReturn > 8:
            threeMonthPercentile = 65
        elif self.threeMonthReturn > 6:
            threeMonthPercentile = 60
        elif self.threeMonthReturn > 4:
            threeMonthPercentile = 55
        elif self.threeMonthReturn > 2:
            threeMonthPercentile = 50
        elif self.threeMonthReturn > 0:
            threeMonthPercentile = 40
        elif self.threeMonthReturn > -3:
            threeMonthPercentile = 30
        elif self.threeMonthReturn > -6:
            threeMonthPercentile = 20
        elif self.threeMonthReturn > -10:
            threeMonthPercentile = 10
        else:
            threeMonthPercentile = 5

        # print("threeMonthPercentile = " + str(threeMonthPercentile))

        if self.oneMonthReturn > 16:
            oneMonthPercentile = 95
        elif self.oneMonthReturn > 13:
            oneMonthPercentile = 90
        elif self.oneMonthReturn > 11:
            oneMonthPercentile = 85
        elif self.oneMonthReturn > 10:
            oneMonthPercentile = 80
        elif self.oneMonthReturn > 9:
            oneMonthPercentile = 75
        elif self.oneMonthReturn > 8:
            oneMonthPercentile = 70
        elif self.oneMonthReturn > 7:
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

        momentumScore = (0.3 * oneYearPercentile) + (0.25 * sixMonthPercentile) + (0.2 * threeMonthPercentile) + (0.2 * oneMonthPercentile) + (0.05 * fiveDayPercentile)

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
    algo = tradingAlgo("AAP")
    print("TradingAlgo.py main. Testing: " + str(algo.getSymbol()))
    print("")

    # print("Testing Mean Reversion:")
    # meanReversion = algo.getMeanReversion()
    # print("/getMeanReversion returned: " + str(meanReversion))

    # print("Testing Momentum Algo:")
    # momentum = algo.momentumAlgo()
    # print("/momentumAlgo returned: " + str(momentum) + "%" + ". Above 70% calssifies as a good momentum stock")

    print("Testing Value Algo:")
    value = algo.valueAlgo()
    print("/valueAlgo returned: " + str(value) + "%")

    # print("Testing 50day / 200day:")
    # fiftyDay = algo.getMovingAverageGap()
    # formatFiftyDay = "{:.5f}".format(fiftyDay)
    # if fiftyDay > 0:
    #     print("/getMovingAverageGap returned: +" + str(formatFiftyDay) +"%")
    # else:
    #     print("/getMovingAverageGap returned: -" + str(formatFiftyDay) +"%")
