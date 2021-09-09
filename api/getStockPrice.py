import yfinance as yf
from datetime import datetime, timedelta

# Function to get current price & intra day highs and lows & % change for a given ticker
def getStockPrice(sym):
    # priceList = []
    # close = []

    # Get info about the current symbol
    try:
        stock = yf.Ticker(sym)
        # Block to get daily high and daily low stock price
        todays_data = stock.history(period='1d')
        formatted_data = "{:.2f}".format(todays_data['Close'][0])
        # formattedLow = "{:.2f}".format(stock.info['dayLow'])
        # formattedHigh = "{:.2f}".format(stock.info['dayHigh'])

        print("DATA: " + formatted_data)

        #Block to get today's date and yesterday's date used to get yesterday's close price below
        # end = datetime.today().strftime('%Y-%m-%d')
        # start = datetime.today() - timedelta(days=1)
        # start = start.strftime('%Y-%m-%d')

        # day = int(end[8:10])
        # day -= 1
        # day = str("%02.0f" % day)
        # print("day = " + day)
        # start = datetime.today().strftime('%Y-%m-%d')
        # start = start[0:8]
        # start = start + day

        return formatted_data

    # Case where the symbol retrieved is not a real stock symbol
    # Opens the commonEnglish words file and appends the bad symbol
    # I wanted to automate this process. I was manually entering the symbols
    #   that weren't real stocks but rather all caps short hands/lingo people say
    except:
        print("Bad ticker symbol " + sym)
        return 0.0
        # fileObj = open("commonEnglish.txt", 'a')
        # fileObj.write(sym+"\n")
        # fileObj.close()

    # Gets yesterday close price
    # print("Start = " + start + ", end = " + end)
    # print(type(start))


    # try:
    #     print("BEFORE CLOSE")
    #     close = stock.history(start=start, end=end, interval='1d')
    #     print("AFTER CLOSE")
    # except:
    #     print("weekend")
    #     # d = datetime.today() - timedelta(days=1)
    #     # print("d = " + str(d))
    #     return 0.0
    #
    # try:
    #     print("finaly block")
    #
    #     temp = float(close['Close'])
    #     formatted_close = "{:.2f}".format(temp)
    #     # Calculate the +/- percentage
    #     difference = ((float(formatted_data) - float(formatted_close)) / float(formatted_data)) * 100
    #     formatted_difference = "{:.2f}".format(difference)
    #
    #     # If statement to print a - or + sign in front of the percentage move
    #     if float(formatted_difference) > 0:
    #         print("    Current: $" + str(formatted_data) + ", Intra-Day Range: $" + str(formattedLow) + "-$" + str(formattedHigh) + ", Daily Difference: +" + formatted_difference + "%")
    #         return formatted_data
    #     else:
    #         print("    Current: $" + str(formatted_data) + ", Intra-Day Range: $" + str(formattedLow) + "-$" + str(formattedHigh) + ", Daily Difference: " + formatted_difference + "%")
    #         return formatted_data
    # except:
    #     print("Something went wrong, fix?")
    #     return 0.0


def getStockPercentChange(sym):

    stock = yf.Ticker(sym)
    todays_data = stock.history(period='1d')
    formatted_data = "{:.2f}".format(todays_data['Close'][0])

    try:
        end = datetime.today().strftime('%Y-%m-%d')
        start = datetime.today() - timedelta(days=1)
        start = start.strftime('%Y-%m-%d')

        day = int(end[8:10])
        day -= 1
        day = str("%02.0f" % day)
        print("day = " + day)
        start = datetime.today().strftime('%Y-%m-%d')
        start = start[0:8]
        start = start + day


        close = stock.history(start=start, end=end, interval='1d')

        temp = float(close['Close'])
        formatted_close = "{:.2f}".format(temp)
        # Calculate the +/- percentage
        difference = ((float(formatted_data) - float(formatted_close)) / float(formatted_data)) * 100
        formatted_difference = "{:.2f}".format(difference)

        if float(formatted_difference) > 0:
            print("    Current: $" + str(formatted_data) + ", Daily Difference: +" + formatted_difference + "%")
            return formatted_difference
        else:
            print("    Current: $" + str(formatted_data) + ", Daily Difference: " + formatted_difference + "%")
            return formatted_difference

    except:
        print("Error, hit except in getStockPercentChange")
        print("If this is printing, its probably a weekend, make a nested loop for start date")
        return 0.0


if __name__ == '__main__':
    #auto generates data[x].txt based on how many files are in the directory
    print("getStockPrice RAN MAIN")
    price = getStockPrice("TSLA")
    print("getStockPrice main Returned: " + str(price))
    percentChange = getStockPercentChange("TSLA")
    print("getStockPercentChange main returned: " + str(percentChange))
