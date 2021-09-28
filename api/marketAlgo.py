from datetime import date
from datetime import timedelta
import pandas as pd
import yahoo_fin.stock_info as si
import yfinance as yf

# All seeing algo
# moving averages
# -> 10 year
# -> VIX
# Take into account the various segments performance


# market segment % daily average change (make this a json obj with -> segment : %change)
# take into account overnight reverse repurchase rate. This is the amount of money banks have
# -> Why kevin thinks the market won't dip right now. Looks into this at work
# include the BPI, bullish percent index
# include the high low index
# Figure out oil relation to stocks
# Figure out how the FED affects this. How what they say is important to the macro


class marketAlgo:
    def __init__(self):
        # Class variable so the API call only needs to be called once
        self.vix = 0
        self.tenYear = 0
        self.nasdaq = 0
        self.sp = 0
        self.dow = 0

    # Returns average daily % change based on the five stocks listed:
    # XOM, CVX, SU, EPD, NEE
    def energySegment(self):
        segmentDailyChange = 0

        # ExxonMobil
        XOM = si.get_quote_table("XOM")
        changeXOM = ((XOM['Quote Price'] / XOM['Previous Close']) - 1) * 100
        # Royal Dutch Shell
        CVX = si.get_quote_table("CVX")
        changeCVX = ((CVX['Quote Price'] / CVX['Previous Close']) - 1) * 100
        # Suncor Energy
        SU = si.get_quote_table("SU")
        changeSU = ((SU['Quote Price'] / SU['Previous Close']) - 1) * 100
        # NextEra Energy
        EPD = si.get_quote_table("EPD")
        changeEPD = ((EPD['Quote Price'] / EPD['Previous Close']) - 1) * 100
        # NextEra Energy
        NEE = si.get_quote_table("NEE")
        changeNEE = ((NEE['Quote Price'] / NEE['Previous Close']) - 1) * 100

        segmentDailyChange = (changeXOM + changeCVX + changeSU + changeEPD + changeNEE) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # CE, DD, FCX, NUE, CLF
    def materialsSegment(self):

        return 0

    def industrialsSegment(self):

        return 0

    def utilitiesSegment(self):

        return 0

    def healthcareSegment(self):

        return 0

    def financialsSegment(self):

        return 0

    def consumerDiscretionarySegment(self):

        return 0

    def consumerStaplesSegment(self):

        return 0

    def informationTechnologySegment(self):

        return 0

    def communicationServicesSegment(self):

        return 0

    def realEstateSegment(self):

        return 0

    def jsonMarketSegments(self):

        return 0

# COMPLETED





    # Returns the current quote for the DOW Jones index
    def getCurrentDOW(self):
        currentDOW = si.get_quote_table("^DJI")

        return currentDOW['Quote Price']

    # returns 50 day moving averge of DOW Jones index
    def fiftyDayDOW(self):
        if self.dow == 0:
            self.dow = yf.Ticker("^DJI")

        fiftyDayAverage = self.dow.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of DOW Jones index
    def twoHundredDayDOW(self):
        if self.dow == 0:
            self.dow = yf.Ticker("^DJI")

        twoHundredDay = self.dow.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundDOW(self):
        fifty = self.fiftyDayDOW()
        twoHund = self.twoHundredDayDOW()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the SP500 index
    def getCurrentSP(self):
        currentSP = si.get_quote_table("^GSPC")

        return currentSP['Quote Price']

    # returns 50 day moving averge of SP500
    def fiftyDaySP(self):
        if self.sp == 0:
            self.sp = yf.Ticker("^GSPC")

        fiftyDayAverage = self.sp.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of SP500
    def twoHundredDaySP(self):
        if self.sp == 0:
            self.sp = yf.Ticker("^GSPC")

        twoHundredDay = self.sp.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundSP(self):
        fifty = self.fiftyDaySP()
        twoHund = self.twoHundredDaySP()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the NASDAQ index
    def getCurrentNASDAQ(self):
        currentNASDAQ = si.get_quote_table("^IXIC")

        return currentNASDAQ['Quote Price']

    # returns 50 day moving averge of nasdaq
    def fiftyDayNASDAQ(self):
        if self.nasdaq == 0:
            self.nasdaq = yf.Ticker("^IXIC")

        fiftyDayAverage = self.nasdaq.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of nasdaq
    def twoHundredDayNASDAQ(self):
        if self.nasdaq == 0:
            self.nasdaq = yf.Ticker("^IXIC")

        twoHundredDay = self.nasdaq.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundNASDAQ(self):
        fifty = self.fiftyDayNASDAQ()
        twoHund = self.twoHundredDayNASDAQ()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the 10 year treasury
    def getTenYear(self):
        if self.tenYear == 0:
            self.tenYear = si.get_quote_table("^TNX")

        # print(self.tenYear)
        return self.tenYear['Quote Price']

    # Returns the daily change for the 10 year
    def getTenYearDailyChange(self):
        if self.tenYear == 0:
            self.tenYear = si.get_quote_table("^TNX")

        prevClose = self.tenYear['Previous Close']
        current = self.tenYear['Quote Price']

        change = (current / prevClose)

        # Determining if - percent of + percent
        if change < 1:
            change = (1 - change) * 100
            change = change * (-1)
        elif change > 1:
            change = (change - 1) * 100
        elif change == 1:
            change = 0

        # print("change = " + str(change))
        return change

    # Returns the percentile based on the last 5 years of where the 10year is sitting
    def tenYearPercentile(self):
        tenYearPercentile = 0

        currentPrice = self.getTenYear()

        try:
            if currentPrice > 3.1:
                tenYearPercentile = 100
            elif currentPrice > 2.9:
                tenYearPercentile = 95
            elif currentPrice > 2.7:
                tenYearPercentile = 90
            elif currentPrice > 2.5:
                tenYearPercentile = 85
            elif currentPrice > 2.4:
                tenYearPercentile = 80
            elif currentPrice > 2.3:
                tenYearPercentile = 75
            elif currentPrice > 2.2:
                tenYearPercentile = 70
            elif currentPrice > 2.1:
                tenYearPercentile = 65
            elif currentPrice > 2.0:
                tenYearPercentile = 60
            elif currentPrice > 1.9:
                tenYearPercentile = 55
            elif currentPrice > 1.8:
                tenYearPercentile = 50
            elif currentPrice > 1.7:
                tenYearPercentile = 45
            elif currentPrice > 1.6:
                tenYearPercentile = 40
            elif currentPrice > 1.5:
                tenYearPercentile = 35
            elif currentPrice > 1.4:
                tenYearPercentile = 30
            elif currentPrice > 1.3:
                tenYearPercentile = 25
            elif currentPrice > 1.2:
                tenYearPercentile = 20
            elif currentPrice > 1.1:
                tenYearPercentile = 15
            elif currentPrice > 0.9:
                tenYearPercentile = 10
            else:
                tenYearPercentile = 5
        except:
            print("tenYearPercentile error")

        return tenYearPercentile



    # Returns the current (or close if after hours) quote of the CBOE volatility index ^VIX
    def getVIX(self):
        if self.vix == 0:
            # This returns a JSON object of all the info needed about the VIX
            self.vix = si.get_quote_table("^VIX")

        return self.vix['Quote Price']

    # Returns the percent daily change of the VIX
    def getVIXDailyChange(self):
        if self.vix == 0:
            self.vix = si.get_quote_table("^VIX")

        prevClose = self.vix['Previous Close']
        current = self.vix['Quote Price']

        change = (current / prevClose)

        # If the VIX is down, make sure the percent is negative
        # If the VIX is up, make sure the percent is positive
        # Else, it just happens to be 0, return 0
        if change < 1:
            change = (1 - change) * 100
            change = change * (-1)
        elif change > 1:
            change = (change - 1) * 100
        elif change == 1:
            change = 0

        # print("change = " + str(change))
        return change

    # Returns the percentile of panic on the given day
    # 0-30% is fairly low
    # 30%-50% is moderate
    # Above 50% is getting high
    # Above 80% is pure panic
    def VIXPanicPercentile(self):
        panicPercent = 0

        if self.vix == 0:
            self.vix = si.get_quote_table("^VIX")

        current = self.vix['Quote Price']
        # print("current = " + str(current))

        try:
            if current > 50:
                panicPercent = 100
            elif current > 47:
                panicPercent = 95
            elif current > 44:
                panicPercent = 90
            elif current > 41:
                panicPercent = 85
            elif current > 38:
                panicPercent = 80
            elif current > 36:
                panicPercent = 75
            elif current > 34:
                panicPercent = 70
            elif current > 32:
                panicPercent = 65
            elif current > 30:
                panicPercent = 60
            elif current > 28:
                panicPercent = 55
            elif current > 26:
                panicPercent = 50
            elif current > 24:
                panicPercent = 45
            elif current > 22:
                panicPercent = 40
            elif current > 20:
                panicPercent = 35
            elif current > 18:
                panicPercent = 30
            elif current > 16:
                panicPercent = 25
            elif current > 14:
                panicPercent = 20
            elif current > 12.5:
                panicPercent = 15
            elif current > 11:
                panicPercent = 10
            else:
                panicPercent = 5
        except:
            print("panicPercent error")

        return panicPercent



if __name__ == '__main__':
    algo = marketAlgo()

    energy = algo.energySegment()
    print("/energySegment returned: " + str(energy))
    print("")


    # print("Testing getCurrentDOW():")
    # currentDOW = algo.getCurrentDOW()
    # print("/getCurrentDOW returned: " + str(currentDOW))
    # print("")

    # print("Testing fiftyDayDOW():")
    # fiftyDOW = algo.fiftyDayDOW()
    # print("/fiftyDayDOW returned: " + str(fiftyDOW))
    # print("")

    # print("Testing twoHundredDayDOW():")
    # twoHundredDOW = algo.twoHundredDayDOW()
    # print("/twoHundredDayDOW returned: " + str(twoHundredDOW))
    # print("")

    # print("Testing fiftyOverTwoHundDOW():")
    # fiftyOverTwoHundDOW = algo.fiftyOverTwoHundDOW()
    # fiftyOverTwoHundDOW = "{:.4f}".format(fiftyOverTwoHundDOW)
    # print("/fiftyOverTwoHundDOW returned: " + str(fiftyOverTwoHundDOW))
    # print("")


    # print("Testing getCurrentSP():")
    # currentSP = algo.getCurrentSP()
    # print("/getCurrentSP returned: " + str(currentSP))
    # print("")

    # print("Testing fiftyDaySP():")
    # fiftySP = algo.fiftyDaySP()
    # print("/fiftyDaySP returned: " + str(fiftySP))
    # print("")

    # print("Testing twoHundredDaySP():")
    # twoHundredSP = algo.twoHundredDaySP()
    # print("/twoHundredDaySP returned: " + str(twoHundredSP))
    # print("")

    # print("Testing fiftyOverTwoHundSP():")
    # fiftyOverTwoHundSP = algo.fiftyOverTwoHundSP()
    # fiftyOverTwoHundSP = "{:.4f}".format(fiftyOverTwoHundSP)
    # print("/fiftyOverTwoHundSP returned: " + str(fiftyOverTwoHundSP))
    # print("")



    # print("Testing getCurrentNASDAQ():")
    # currentNas = algo.getCurrentNASDAQ()
    # print("/getCurrentNASDAQ returned: " + str(currentNas))
    # print("")

    # print("Testing fiftyDayNASDAQ():")
    # fiftyNas = algo.fiftyDayNASDAQ()
    # print("/fiftyDayNASDAQ returned: " + str(fiftyNas))
    # print("")

    # print("Testing twoHundredDayNASDAQ():")
    # twoHundredNas = algo.twoHundredDayNASDAQ()
    # print("/twoHundredDayNASDAQ returned: " + str(twoHundredNas))
    # print("")

    # print("Testing fiftyOverTwoHundNASDAQ():")
    # fiftyOverTwoHundNas = algo.fiftyOverTwoHundNASDAQ()
    # fiftyOverTwoHundNas = "{:.4f}".format(fiftyOverTwoHundNas)
    # print("/fiftyOverTwoHundNASDAQ returned: " + str(fiftyOverTwoHundNas))
    # print("")



    # print("Testing getTenYear():")
    # tenYear = algo.getTenYear()
    # print("/getTenYear returned: " + str(tenYear))
    # print("")

    # print("Testing getTenYearDailyChange():")
    # tenYearChange = algo.getTenYearDailyChange()
    # print("/getTenYearDailyChange returned: " + str(tenYearChange))
    # print("")

    # print("Testing tenYearPercentile():")
    # tenYearPercentile = algo.tenYearPercentile()
    # print("/tenYearPercentile returned: " + str(tenYearPercentile))
    # print("")



    # print("Testing getVIX():")
    # vix = algo.getVIX()
    # print("/getVIX returned: " + str(vix))
    # print("")

    # print("Testing getVIXDailyChange():")
    # vixChange = algo.getVIXDailyChange()
    # vixChange = "{:.2f}".format(vixChange)
    # print("/getVIXDailyChange returned: " + str(vixChange) + "%")
    # print("")

    # print("Testing VIXPanicPercentile():")
    # vixPanic = algo.VIXPanicPercentile()
    # print("/VIXPanicPercentile returned: " + str(vixPanic))
    # print("")
