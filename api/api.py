from flask import Flask
from Interpreter import runRedditScraper, getCommonNames
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    print("api.Py")
    runRedditScraper()
    symbolList = getCommonNames()
    jsonStr = json.dumps(symbolList)
    # str = convert(symbolList)
    # print("Type:")
    # print(type(jsonStr))
    # jsonObj = json.loads(jsonStr)

    return jsonStr
    # return {
    #     'name': ['orange, apple']
    # }

if __name__ == '__main__':
    app.run(debug=True)
