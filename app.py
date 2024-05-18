from flask import Flask, jsonify
from main import fetch_all_data, process_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_citations():
    data = fetch_all_data()
    results = process_data(data)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
