import yfinance as yf
from datetime import datetime

# Function to get current price & intra day highs and lows & % change for a given ticker
def getStockPrice(sym):
    priceList = []

    # Get info about the current symbol
    stock = yf.Ticker(sym)
    try:
        # Block to get daily high and daily low stock price
        todays_data = stock.history(period='1d')
        formatted_data = "{:.2f}".format(todays_data['Close'][0])
        formattedLow = "{:.2f}".format(stock.info['dayLow'])
        formattedHigh = "{:.2f}".format(stock.info['dayHigh'])

        #Block to get today's date and yesterday's date used to get yesterday's close price below
        end = datetime.today().strftime('%Y-%m-%d')
        day = int(end[8:10])
        day -= 1
        day = str("%02.0f" % day)
        start = datetime.today().strftime('%Y-%m-%d')
        start = start[0:8]
        start = start + day

    # Case where the symbol retrieved is not a real stock symbol
    # Opens the commonEnglish words file and appends the bad symbol
    # I wanted to automate this process. I was manually entering the symbols
    #   that weren't real stocks but rather all caps short hands/lingo people say
    except:
        print("Bad ticker symbol " + sym)
        # fileObj = open("commonEnglish.txt", 'a')
        # fileObj.write(sym+"\n")
        # fileObj.close()

    try:
        # Gets yesterday close price
        close = stock.history(start=start, end=end, interval='1d')
        temp = float(close['Close'])
        formatted_close = "{:.2f}".format(temp)
        # Calculate the +/- percentage
        difference = ((float(formatted_data) - float(formatted_close)) / float(formatted_data)) * 100
        formatted_difference = "{:.2f}".format(difference)

        # If statement to print a - or + sign in front of the percentage move
        if float(formatted_difference) > 0:
            print("    Current: $" + str(formatted_data) + ", Intra-Day Range: $" + str(formattedLow) + "-$" + str(formattedHigh) + ", Daily Difference: +" + formatted_difference + "%")
        else:
            print("    Current: $" + str(formatted_data) + ", Intra-Day Range: $" + str(formattedLow) + "-$" + str(formattedHigh) + ", Daily Difference: " + formatted_difference + "%")
    except:
        print("Mondays may cause error. No market data for Sundays.")

if __name__ == '__main__':
    #auto generates data[x].txt based on how many files are in the directory
    print("RAN MAIN")
