import yfinance as yf


def value(symbol):
    print("Value based algorithm")

# get 1 year return, maybe a more recent price return too
# figure out percentile calculation from the freecodecamp video
# stock with the best 1 year, 6 month, 3 month and 1 month weighted average
# should get a better score
def momentum(symbol):
    print("Momentum based algorithm")

# take into account 10 year tresury
def growth(symbol):
    print("Growth based algorithm")


def composite(symbol):
    print("Composite of algorithms")

# Give a rating on how close the stock is to crossing the 200 day moving average
def getMovingAverage(symbol):
    print("Moving Average 50 day / 200 day:")

# The mean reversion strategy says highs and lows of a stock are only temporary.
# They will revert to their mean value from time to time
def getMeanReversion(symbol):
    print("Mean Reversion buy point for particular stock")
    stock = yf.Ticker(symbol)
    # Block to get daily high and daily low stock price
    stockData = stock.history(period='1y', interval='1d')
    # yearlyHigh = "{:.2f}".format(stock.info['fiftyTwoWeekHigh'])
    # yearlyLow = "{:.2f}".format(stock.info['fiftyTwoWeekLow'])
    # yearlyHigh = stockData['High']
    # yearlyLow = stockData['Low']
    yearlyHigh = stock.info['fiftyTwoWeekHigh']
    yearlyLow = stock.info['fiftyTwoWeekLow']

#   Just add yearly high and yearly low then divide by 2
    meanReversion = (yearlyHigh + yearlyLow) / 2

    return meanReversion

# Main entry point
if __name__ == '__main__':
    print("TradingAlgo.py main:")
    response = getMeanReversion("TSLA")
    print("/getMeanReversion returned: " + str(response))
