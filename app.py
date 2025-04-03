from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Backend está funcionando!"

@app.route('/get-prices', methods=['GET'])
def get_prices():
    prices = [
        {"name": "Produto 1", "price": 10.99},
        {"name": "Produto 2", "price": 20.49},
        {"name": "Produto 3", "price": 5.99}
    ]
    return jsonify(prices)

@app.route('/hello', methods=['GET'])
def hello():
    return "Rota de teste funcionando!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)