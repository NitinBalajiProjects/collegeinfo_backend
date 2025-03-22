from flask import Flask, jsonify
from util import ExcelToJsonUtil

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to College Info API"})

@app.route("/info")
def get_info():
    return jsonify({"college": "XYZ University", "location": "New York"})

@app.route("/compsci")
def get_compsci():
    return ExcelToJsonUtil.convert_to_json("data/CompScienceRanking.xlsx")

@app.route("/national")
def get_national():
    return ExcelToJsonUtil.convert_to_json("data/NationalUnivRanking.xlsx")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
