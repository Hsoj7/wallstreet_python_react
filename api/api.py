from flask import Flask
from Interpreter import runRedditScraper, getCommonNames
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
    stringList = str(symbolList)
    print("getPrices " + stringList)

    jsonStr = json.dumps(symbolList)

    # Now create a new file called getStockData.py and move the getStockData function there.
    # print("IN GET PRICES " + jsonStr)
    return jsonStr

if __name__ == '__main__':
    app.run(debug=True)
