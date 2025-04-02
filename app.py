from flask import Flask, jsonify, request
from web_scraper import scrape_prices_from_site
from ocr_processor import extract_text_from_image

app = Flask(__name__)

@app.route("/get-prices", methods=["GET"])
def get_prices():
    data = scrape_prices_from_site()
    return jsonify(data)

@app.route("/process-image", methods=["POST"])
def process_image():
    # Para simplicidade, usamos um arquivo local como exemplo
    image_path = "uploaded_image.jpg"  # Substitua pelo caminho da imagem
    extracted_text = extract_text_from_image(image_path)
    return jsonify({"extracted_text": extracted_text})

if __name__ == "__main__":
    app.run(debug=True)