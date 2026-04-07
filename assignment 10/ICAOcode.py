import json

from flask import Flask
app = Flask(__name__)


openjson = open('airport.json', "r")
airport = json.load(openjson)


@app.route('/airport/<icaocode>', methods=['GET'])
def getcode(icaocode):
    code = icaocode.upper()
    try:
        inforamtion = airport[code]
        name = inforamtion['name']
        city = inforamtion['city']
        country = inforamtion['country']
        return {"icaocode": icaocode, "name": name, "city": city, "country": country}
    except KeyError:
        print("Airport not found"), 404
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)