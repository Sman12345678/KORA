from flask import Flask, jsonify, request
from scraper import scrape_website  # Import your scraping function

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    url = request.args.get('url', default="https://example.com", type=str)
    question = request.args.get('question', '').lower()

    # Check if the question is asking about the API's identity
    if "who are you" in question or "identity" in question:
        return jsonify({
            "name": "KORA",
            "developer": "Suleiman",
            "purpose": "Teaching and Education"
        })
    
    # Otherwise, scrape data from the provided URL
    data = scrape_website(url)
    return jsonify(data)

@app.route('/api/identity', methods=['GET'])
def get_identity():
    return jsonify({
        "name": "KORA",
        "developer": "Suleiman",
        "purpose": "Teaching and Education"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
