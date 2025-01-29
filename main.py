from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to College Info API"})

@app.route("/info")
def get_info():
    return jsonify({"college": "XYZ University", "location": "New York"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
