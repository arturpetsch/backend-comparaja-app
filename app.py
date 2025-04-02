from flask import Flask, jsonify, request
from web_scraper import scrape_prices_from_site
from ocr_processor import extract_text_from_image

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend está funcionando!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Certifique-se de que usa 0.0.0.0 e uma porta válida

@app.route('/get-prices', methods=['GET'])
def get_prices():
    try:
        with open('prices.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter preços: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, use_reloader=False)


@app.route("/process-image", methods=["POST"])
def process_image():
    # Para simplicidade, usamos um arquivo local como exemplo
    image_path = "uploaded_image.jpg"  # Substitua pelo caminho da imagem
    extracted_text = extract_text_from_image(image_path)
    return jsonify({"extracted_text": extracted_text})

if __name__ == "__main__":
    app.run(debug=True)