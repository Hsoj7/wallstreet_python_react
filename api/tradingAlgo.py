import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd

class tradingAlgo:
    def __init__(self, symbol):
        # Variables used by many functions
        self.symbol = symbol
        self.stock = yf.Ticker(self.symbol)
        self.currentPrice = self.stock.history(period='1d')['Close'][0]

        # Variables used by momentum algo
        self.oneYearReturn = 0
        self.sixMonthReturn = 0
        self.threeMonthReturn = 0
        self.oneMonthReturn = 0
        self.fiveDayReturn = 0

        # Variables used by value algo
        self.pe = 0
        self.priceToBook = 0
        self.priceToSales = 0
        self.totalDebt = 0
        self.totalCash = 0
        self.marketCap = ""
        self.ev_to_ebitda = 0
        self.ev_to_grossProfit = 0

        # Variables used by growth Algo


    # Just returns the stock symbol of the given instance
    def getSymbol(self):
        return self.symbol

    # Gives traditional value rating on a stock
    # Above 70% classifies as a decent rating
    def valueAlgo(self):
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

        PePercentile = 0
        PbPercentile = 0
        PsPercentile = 0
        # enterprise value to ebitda
        EVEBITDAPercentile = 0
        # enterprise value to gross profit
        EVGPPercentile = 0

        # P/E is the price-earnings ratio
        # A P/E under 20 is normally considered really good value
        # A P/E in the hundreds is normally a growth stock
        try:
            if self.pe > 200 or self.pe < 0:
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
            elif self.pe > 10:
                PePercentile = 10
            else:
                PePercentile = 5
        except Exception as error:
            print("Price/earnings error: " + str(error))
        # print("PE percentile = " + str(PePercentile))
        if pd.isna(self.pe):
            print("Found NAN")
            PePercentile = 95

        # Price to book compares a company's market value to its book value
        # Price is the market vaule of a company, also known as market cap
        # Book value is the net assets of a company
        # Therefore a good value is a company that is worth it's assets, p/b value = 1
        try:
            if self.priceToBook > 28 or self.priceToBook < 0:
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
        except:
            print("Price/book error")
        # print("Price-Book percentile = " + str(PbPercentile))
        if pd.isna(self.priceToBook):
            PbPercentile = 95

        # Price to sales the company's market cap divided by the most recent year's revenue
        # A value under 2 means the company makes half of its market cap in a year
        try:
            if self.priceToSales > 14 or self.priceToSales < 0:
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
        except:
            print("Price/sales error")
        # print("Price-Sales percentile = " + str(PsPercentile))
        if pd.isna(self.priceToSales):
            PsPercentile = 95


        # print("self.ev_to_ebitda = " + str(self.ev_to_ebitda))
        # Enterprise Value measures the company's total value. Comparable but potentially more accurate to market cap
        # EBITDA is earnings before interest, taxes, depreciation, and amortization. This measures overall financial performance
        # The average of the S&P500 is 11-14. A very good value is under 10
        try:
            if self.ev_to_ebitda > 36 or self.ev_to_ebitda < 0:
                EVEBITDAPercentile = 95
            elif self.ev_to_ebitda > 30:
                EVEBITDAPercentile = 90
            elif self.ev_to_ebitda > 26:
                EVEBITDAPercentile = 85
            elif self.ev_to_ebitda > 22.5:
                EVEBITDAPercentile = 80
            elif self.ev_to_ebitda > 20:
                EVEBITDAPercentile = 75
            elif self.ev_to_ebitda > 18.5:
                EVEBITDAPercentile = 70
            elif self.ev_to_ebitda > 17.8:
                EVEBITDAPercentile = 65
            elif self.ev_to_ebitda > 17:
                EVEBITDAPercentile = 60
            elif self.ev_to_ebitda > 16:
                EVEBITDAPercentile = 55
            elif self.ev_to_ebitda > 15:
                EVEBITDAPercentile = 50
            elif self.ev_to_ebitda > 14:
                EVEBITDAPercentile = 45
            elif self.ev_to_ebitda > 13:
                EVEBITDAPercentile = 40
            elif self.ev_to_ebitda > 12:
                EVEBITDAPercentile = 35
            elif self.ev_to_ebitda > 11:
                EVEBITDAPercentile = 30
            elif self.ev_to_ebitda > 9.9:
                EVEBITDAPercentile = 25
            elif self.ev_to_ebitda > 8.9:
                EVEBITDAPercentile = 20
            elif self.ev_to_ebitda > 7.8:
                EVEBITDAPercentile = 15
            elif self.ev_to_ebitda > 7:
                EVEBITDAPercentile = 10
            else:
                EVEBITDAPercentile = 5
        except:
            print("ev_to_ebitda error")
        # print("EVEBITDAPercentile = " + str(EVEBITDAPercentile))
        if pd.isna(self.ev_to_ebitda):
            EVEBITDAPercentile = 95

        # print("self.ev_to_grossProfit = " + str(self.ev_to_grossProfit))
        # Similar to ev/ebitda, this is over gross profit
        # This demonstrates how many dollars of enterprise value are generated for every dollar of gross profit earned
        try:
            if self.ev_to_grossProfit > 25 or self.ev_to_grossProfit < 0:
                EVGPPercentile = 95
            elif self.ev_to_grossProfit > 22:
                EVGPPercentile = 90
            elif self.ev_to_grossProfit > 19:
                EVGPPercentile = 85
            elif self.ev_to_grossProfit > 16.5:
                EVGPPercentile = 80
            elif self.ev_to_grossProfit > 14:
                EVGPPercentile = 75
            elif self.ev_to_grossProfit > 13:
                EVGPPercentile = 70
            elif self.ev_to_grossProfit > 12.3:
                EVGPPercentile = 65
            elif self.ev_to_grossProfit > 11.9:
                EVGPPercentile = 60
            elif self.ev_to_grossProfit > 11.5:
                EVGPPercentile = 55
            elif self.ev_to_grossProfit > 10.5:
                EVGPPercentile = 50
            elif self.ev_to_grossProfit > 9.6:
                EVGPPercentile = 45
            elif self.ev_to_grossProfit > 8.7:
                EVGPPercentile = 40
            elif self.ev_to_grossProfit > 7.9:
                EVGPPercentile = 35
            elif self.ev_to_grossProfit > 7.2:
                EVGPPercentile = 30
            elif self.ev_to_grossProfit > 6.7:
                EVGPPercentile = 25
            elif self.ev_to_grossProfit > 6:
                EVGPPercentile = 20
            elif self.ev_to_grossProfit > 5.3:
                EVGPPercentile = 15
            elif self.ev_to_grossProfit > 4.5:
                EVGPPercentile = 10
            else:
                EVGPPercentile = 5
        except:
            print("ev_to_grossProfit error")
        # print("EVGPPercentile = " + str(EVGPPercentile))
        if pd.isna(self.ev_to_grossProfit):
            EVGPPercentile = 95

        numberOfMissingValues = 0
        if PePercentile == 0:
            numberOfMissingValues += 1
        if PbPercentile == 0:
            numberOfMissingValues += 1
        if PsPercentile == 0:
            numberOfMissingValues += 1
        if EVEBITDAPercentile == 0:
            numberOfMissingValues += 1
        if EVGPPercentile == 0:
            numberOfMissingValues += 1

        # print("numberOfMissingValues = " + str(numberOfMissingValues))

        # For debugging
        # print("PePercentile = " +str(PePercentile))
        # print("PbPercentile = " + str(PbPercentile))
        # print("PsPercentile = " + str(PsPercentile))
        # print("EVEBITDAPercentile = " + str(EVEBITDAPercentile))
        # print("EVGPPercentile = " + str(EVGPPercentile))

        # calculate the mean percentile
        meanPercentile = (PePercentile + PbPercentile + PsPercentile + EVEBITDAPercentile + EVGPPercentile) / (5 - numberOfMissingValues)
        # subtract from 100 because lower percentile here means better value
        meanPercentile = 100 - meanPercentile

        return meanPercentile

    # Returns the percentile of momentum
    # Low quality momentum stocks (those that are pump and dump) will get a
    # far lower score than those of high quality, large gains over long time
    # Above 70% classifies as a decent rating
    def momentumAlgo(self):
        self.oneYearReturn = ((self.currentPrice / self.stock.history(period='1y')['Close'][0]) - 1) * 100
        self.sixMonthReturn = ((self.currentPrice / self.stock.history(period='180d')['Close'][0]) - 1) * 100
        self.threeMonthReturn = ((self.currentPrice / self.stock.history(period='90d')['Close'][0]) - 1) * 100
        self.oneMonthReturn = ((self.currentPrice / self.stock.history(period='30d')['Close'][0]) - 1) * 100
        self.fiveDayReturn = ((self.currentPrice / self.stock.history(period='5d')['Close'][0]) - 1) * 100
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

    # Returns the percentile of growth quality looking at the stock with a 5-year time frame
    # above 70% classifies as a decent growth stock with 5 year time frame
    # This algo won't work if yahoo finance has poor 5 year growth estimates. They
    # are sometimes abysmal
    def growthAlgo(self):
        # Percent the company is excepted to grow at
        yearlyGrowthRate = 0
        # Estimated current year earnings per share
        estimateCurrYearEPS = 0
        # will hold EPS * sharesOutstanding. Used in calculating future earnings
        yearEarningsEstimate = 0
        # Calcuation of earnings 5 years from now
        fiveYearEarnings = 0
        # used for calculating future P/E
        fiveYearEarningPerShare = 0
        # Holds the future P/E ratio
        fiveYearPE = 0

        fiveYearGrowthPercentile = 0

        sharesOutstanding = self.stock.info['sharesOutstanding']
        # print("sharesOutstanding = " + str(sharesOutstanding))

        # Block to retrieve earnings and growth estimates
        info = si.get_analysts_info(self.symbol)
        for item in info.items():
            # print(item)
            if item[0] == "Earnings Estimate":
                for index, row in item[1].iterrows():
                    if row['Earnings Estimate'] == "Avg. Estimate":
                        try:
                            estimateCurrYearEPS = row["Current Year (2021)"]
                        except:
                            estimateCurrYearEPS = row["Current Year (2022)"]

            if item[0] == "Growth Estimates":
                for index, row in item[1].iterrows():
                    if row['Growth Estimates'] == "Next 5 Years (per annum)":
                        yearlyGrowthRate = row[self.symbol]
                    # print(row['TSLA'])
                    # print(type(row['Growth Estimates']))

        # print("yearlyGrowthRate = " + str(yearlyGrowthRate))
        # print("estimateCurrYearEPS = " + str(estimateCurrYearEPS))

        # gets total earnings for this year
        yearEarningsEstimate = estimateCurrYearEPS * sharesOutstanding
        # To get yearlyGrowthRate into percentage. If it was 50%, its now 0.5
        yearlyGrowthRate = float(yearlyGrowthRate[0:len(yearlyGrowthRate) - 1])
        yearlyGrowthRate = yearlyGrowthRate / 100
        # Calculation for earnings 5 years from now, based on 50% growth
        # if growth is > 0, add it. If negative, subtract it
        if yearlyGrowthRate > 0:
            fiveYearEarnings = yearEarningsEstimate * ((1 + yearlyGrowthRate) ** 5)
        elif yearlyGrowthRate < 0:
            fiveYearEarnings = yearEarningsEstimate * ((1 - yearlyGrowthRate) ** 5)

        # EPS 5 years from now if 50% growth happens
        fiveYearEarningPerShare = fiveYearEarnings / sharesOutstanding
        # Five year from now PE calculation
        fiveYearPE = self.currentPrice / fiveYearEarningPerShare

        try:
            if fiveYearPE > 200 or fiveYearPE < 0:
                fiveYearGrowthPercentile = 95
            elif fiveYearPE > 100:
                fiveYearGrowthPercentile = 90
            elif fiveYearPE > 60:
                fiveYearGrowthPercentile = 85
            elif fiveYearPE > 44:
                fiveYearGrowthPercentile = 80
            elif fiveYearPE > 38:
                fiveYearGrowthPercentile = 75
            elif fiveYearPE > 34:
                fiveYearGrowthPercentile = 70
            elif fiveYearPE > 31:
                fiveYearGrowthPercentile = 65
            elif fiveYearPE > 28:
                fiveYearGrowthPercentile = 60
            elif fiveYearPE > 26:
                fiveYearGrowthPercentile = 55
            elif fiveYearPE > 24:
                fiveYearGrowthPercentile = 50
            elif fiveYearPE > 22:
                fiveYearGrowthPercentile = 45
            elif fiveYearPE > 20:
                fiveYearGrowthPercentile = 40
            elif fiveYearPE > 18:
                fiveYearGrowthPercentile = 35
            elif fiveYearPE > 16:
                fiveYearGrowthPercentile = 30
            elif fiveYearPE > 15:
                fiveYearGrowthPercentile = 25
            elif fiveYearPE > 14:
                fiveYearGrowthPercentile = 20
            elif fiveYearPE > 12:
                fiveYearGrowthPercentile = 15
            elif fiveYearPE > 10:
                fiveYearGrowthPercentile = 10
            else:
                fiveYearGrowthPercentile = 5
        except:
            print("Price/earnings error")

        # we want high percentage meaning good to be consitent with the other algos
        fiveYearGrowthPercentile = 100 - fiveYearGrowthPercentile

        return fiveYearGrowthPercentile


    # Gets the value + momentum of a stock. Adds the % together and divide by 2
    # This returns the % buy if its a value based company. They must have a decent
    # yearly return to get a good rating. This filters out stocks like BABA which
    # are crazy good deals at the moment but have had a poor year.
    def valueComposite(self):
        valuePercentile = self.valueAlgo()
        # print("valuePercentile = " + str(valuePercentile))
        momentumPercentile = self.momentumAlgo()

        composite = (valuePercentile + momentumPercentile) / 2

        return composite

    # Get ths growth + momentum of a stock. Adds the % together and divides by 2
    # Returns the %buy depending how well the stock has performed. A growth company
    # might be shooting for 50% growth YoY, but if the stock isn't moving, there must
    # be a reason why. Maybe create a function in the future that 'needs human attention',
    # in a case like this.
    def growthComposite(self):
        growthPercentile = self.growthAlgo()
        # print("growthPercentile = " + str(growthPercentile))
        momentumPercentile = self.momentumAlgo()

        composite = (growthPercentile + momentumPercentile) / 2

        return composite


    # divides the value of the daily average volume by the market cap
    # This gives a percent of the company trading hands each day
    # The lower the percent, the larger the long-term shareholder base
    # The higher the percent, the smaller the long-term shareholder base
    #  -> AKA, just a day trade stock
    def getStockVolatility(self):

        return 0

    # Return the descrption of a company provided by yahoo finance library
    def getCompanyDescription(self):
        summary = self.stock.info['longBusinessSummary']
        return summary

    # Return the full company name
    def getCompanyFullName(self):
        longName = self.stock.info['longName']
        return longName

    # Returns the 50 day average of the given stock
    def getFiftyDayAvg(self):
        fiftyDayAverage = self.stock.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # Returns the 200day average of the given stock
    def getTwoHundredDayAverage(self):
        twoHundredDayAverage = self.stock.history(period='200d')['Close']
        twoHundredDayAverage = sum(twoHundredDayAverage) / len(twoHundredDayAverage)
        return twoHundredDayAverage

    # Give a rating on how close the stock is to crossing the 200 day moving average
    # Positive means 50day is above the 200day
    # negative means 50day is below the 200day
    def getMovingAverageGap(self):
        # avgFifty = sum(self.fiftyDayAverage) / len(self.fiftyDayAverage)
        # avgtwoHundred = sum(self.twoHundredDayAverage) / len(self.twoHundredDayAverage)

        percentDiff = ((self.getFiftyDayAvg() / self.getTwoHundredDayAverage()) - 1) * 100

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
    print("")

    print("Testing getCompanyDescription:")
    summary = algo.getCompanyDescription()
    print("/getCompanyDescription returned: " + str(summary))
    print("")

    print("Testing getCompanyFullName:")
    fullName = algo.getCompanyFullName()
    print("/getCompanyFullName returned: " + str(fullName))
    print("")

    # print("Testing Mean Reversion:")
    # meanReversion = algo.getMeanReversion()
    # print("/getMeanReversion returned: " + str(meanReversion))

    # print("Testing Momentum Algo:")
    # momentum = algo.momentumAlgo()
    # print("/momentumAlgo returned: " + str(momentum) + "%")
    # print("")

    # print("Testing growthComposite")
    # growth = algo.growthComposite()
    # print("/growthComposite returned: " + str(growth) + "%")
    # print("")

    # print("Testing valueComposite:")
    # value = algo.valueComposite()
    # print("/valueComposite returned: " + str(value) + "%")
    # print("")

    # print("50day = " + str(algo.getFiftyDayAvg()))
    # print("200day = " + str(algo.getTwoHundredDayAverage()))
    # print("Testing 50day / 200day:")
    # fiftyDay = algo.getMovingAverageGap()
    # formatFiftyDay = "{:.5f}".format(fiftyDay)
    # if fiftyDay > 0:
    #     print("/getMovingAverageGap returned: +" + str(formatFiftyDay) +"%")
    # else:
    #     print("/getMovingAverageGap returned: -" + str(formatFiftyDay) +"%")
