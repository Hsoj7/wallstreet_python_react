import pandas as pd
import yfinance as yf
import cryptocompare
from datetime import datetime
from datetime import timedelta
import json

# finds meaning full data about a given crypto curreny
# takes the crypto symbol and a country's currency
# ex: coin = cryptoAlgo('BTC', 'CAD')
# -> for bitcoin in canadian dollars
class cryptoAlgo:
    def __init__(self, coin, currency):
        self.currency = currency
        self.coin = coin

    # Function to get current give cypto price
    def getPrice(self):
        obj = cryptocompare.get_price([self.coin], [self.currency])
        price = 0
        for key, value in obj.items():
            for key1, value1 in value.items():
                price = value1

        return price

    # Function to get the 50 day average of coin's closing price (i think 7pm each day)
    def getMovingAverage(self, limit):
        # API call to get (x) amount of days worth of data
        # returns list of json objects
        hist = cryptocompare.get_historical_price_day(self.coin, self.currency, limit=limit)

        # list that will append all the closing prices of the last (x) amount of days
        averageList = []
        for obj in hist:
            averageList.append(obj['close'])

        # Add each of the 50 day close prices together
        Average = 0
        for close in averageList:
            Average = Average + close

        # Now, divide by 50 to get the average
        Average = Average / limit

        return Average

    # returns the percent difference of the 50/200 day moving average
    # Less than positive 5% is getting dangerous
    def movingAverageDifference(self):
        fiftyDay = self.getMovingAverage(50)
        twoHundredDay = self.getMovingAverage(200)

        percentDiff = ((fiftyDay / twoHundredDay) - 1) * 100

        return percentDiff

    # Returns JSON obj of how much resistance for the given price intervals for a crypto
    def getResistance(self):
        closePriceList = []
        # get 1 year worth of data
        hist = cryptocompare.get_historical_price_day(self.coin, self.currency, limit=365)

        # get list of all the closing prices for the last year
        for obj in hist:
            closePriceList.append(obj['close'])

        # sort the list ascending
        closePriceList.sort()

        # get the range for each resistance. Calculation is 2.5% of the largest value
        largest = closePriceList[len(closePriceList) - 1]
        # get smallest and largest price in the last year
        smallest = closePriceList[0]
        stepAmount = largest * 0.025

        jsonData = {}
        # start at smallest
        current = smallest
        # variables for counting the amount of close in the given interval
        numResistance = 0
        # loop through close prices
        for close in closePriceList:
            # increment the resistance in this stepAmount
            numResistance += 1
            # If the given price is into the next interval, input the # of resistance
            # into the json obj with the given interval
            if close > (current + stepAmount):
                current = current + stepAmount
                current = int(current)
                # create the json interval
                x = {str(current):numResistance}
                # add interval to the main jsondata object
                jsonData.update(x)
                # reset resistance counter, we're into the next interval
                numResistance = 0

        return jsonData


    # This is a technical analysis pattern
    # Bullish engulfing pattern is when a candle stick closes higher than the previous day's
    # opening after opening lower than the previous day's close.
    # Therefore, the day 2 candle stick completely engulfs the day 1 candle stick
    # This function takes in the amount of days to go back and identifies days that have this pattern
    def bullishEngulfingPatternHistorical(self, limit):
        today = datetime.today()

        hist = cryptocompare.get_historical_price_day(self.coin, self.currency, limit=limit)
        # print(hist)

        # for i in range(limit, 0, -1):
        #     print(i)

        # for obj in hist:
        #     print(obj)
        #     unixDate = int(obj['time'])
        #     today = datetime.utcfromtimestamp(unixDate)
        #
        #     # todayStr = str(today)
        #     # todayStr = todayStr[0:10]
        #     # print(todayStr)


        return 0

    # identifies a bullish wedge pattern in the crypto
    def bullishWedgePattern(self):

        return 0



if __name__ == '__main__':
    coin = cryptoAlgo('BTC', 'CAD')

    # print("Testing getPrice:")
    # getPrice = coin.getPrice()
    # print("/getPrice returned: " + str(getPrice))
    # print("")


    # print("Testing bullishEngulfingPatternHistorical:")
    # bullishEngulfingPatternHistorical = coin.bullishEngulfingPatternHistorical(10)
    # print("/bullishEngulfingPatternHistorical returned: " + str(bullishEngulfingPatternHistorical))
    # print("")


    print("Testing getResistance:")
    getResistance = coin.getResistance()
    print("/getResistance returned: " + str(getResistance))
    print("")


    # print("Testing getMovingAverage:")
    # getMovingAverage = coin.getMovingAverage(50)
    # print("/getMovingAverage 50 day returned: " + str(getMovingAverage))
    # print("")

    # print("Testing getMovingAverage:")
    # getMovingAverage = coin.getMovingAverage(200)
    # print("/getMovingAverage 200 day returned: " + str(getMovingAverage))
    # print("")

    # print("Testing movingAverageDifference:")
    # movingAverageDifference = coin.movingAverageDifference()
    # movingAverageDifference = "{:.4f}".format(movingAverageDifference)
    # print("/movingAverageDifference returned: " + str(movingAverageDifference) + "%")
    # print("")
