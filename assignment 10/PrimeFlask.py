from flask import Flask, request, jsonify
app = Flask(__name__)
def PrimeCheck(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
@app.route('/prime_number/<int:number>', methods=['GET'])
def index(number):
    status = PrimeCheck(number)
    responses = {
        "Number": number,
        "Status": status,
    }
    return jsonify(responses)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

