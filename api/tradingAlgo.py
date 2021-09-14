

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

def getTradingRange(symbol):
    print("Trading range for particular stock")
    # for value, doing bottom price within the last year + top price within the last year / 2 should be accurate
    # for growth, doing bottom price within the last year + top price within the last year * 0.66 should be accurate?

# Main entry point
if __name__ == '__main__':
    print("TradingAlgo.py main:")
    print("Testing Growth")
