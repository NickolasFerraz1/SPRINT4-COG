from flask import Flask, request, jsonify
from flask_cors import CORS
from reg_linear import regressao_linear
app = Flask(__name__)

CORS(app)

# Endpoint da API para prever
@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json  # Recebe os dados em formato JSON
    x1 = data.get('x1', 0)  # Valor de x1 recebido
    x2 = data.get('x2', 0)  # Valor de x2 recebido

    # Realiza a previsão usando o algoritmo de regressão linear
    resultado = regressao_linear(x1, x2)

    return jsonify({'previsao': resultado})  # Retorna o resultado em formato JSON

@app.route('/', methods = ['GET'])
def home():
    return("API funcionando!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
