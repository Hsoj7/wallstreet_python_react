from flask import Flask
from Interpreter import runRedditScraper, getCommonNames
from getStockPrice import getStockPrice, getStockPercentChange
import json

app = Flask(__name__)

runRedditScraper()
symbolList = getCommonNames()

@app.route('/getSymbols', methods=['GET'])
def index():
    print("getSymbols")

    jsonStr = json.dumps(symbolList)

    return jsonStr

@app.route('/getPrices', methods=['GET'])
def index1():
    priceList = []

    for symbol in symbolList:
        # print("Getting price for: " + symbol)
        price = getStockPrice(symbol)
        priceList.append(price)

    jsonStr = json.dumps(priceList)

    # print("IN GET PRICES " + jsonStr)
    return jsonStr

@app.route('/getPercentChange', methods=['GET'])
def index2():
    percentList = []

    for symbol in symbolList:
        print("Getting percentChange for: " + symbol)
        try:
            percent = getStockPercentChange(symbol)
            percentList.append(percent)
        except:
            percentList.append("0.0")

    jsonStr = json.dumps(percentList)

    # Now create a new file called getStockData.py and move the getStockData function there.
    print("IN /getPercentChange " + jsonStr)
    return jsonStr

if __name__ == '__main__':
    app.run(debug=True)
