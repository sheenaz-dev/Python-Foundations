from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "<h1>ISA Sentinel Backend is Running!</h1><p>Ready for AI Analysis.</p>"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "").lower()
    
    # Your Safety Logic
    safety_words = ["bomb", "suicide", "attack"]
    found = [word for word in safety_words if word in text]
    
    status = "flagged" if found else "clear"
    return jsonify({"status": status, "found": found})

if __name__ == '__main__':
    app.run(port=5000)