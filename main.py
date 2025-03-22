import os
from flask import Flask, jsonify
from util import ExcelToJsonUtil

app = Flask(__name__)

# Get the absolute path of the current script (main.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return jsonify({"message": "Welcome to College Info API"})

@app.route("/info")
def get_info():
    return jsonify({"college": "XYZ University", "location": "New York"})

@app.route("/compsci")
def get_compsci():
    file_path = os.path.join(BASE_DIR, "data", "CompScienceRanking.xlsx")
    return ExcelToJsonUtil.convert_to_json(file_path)

@app.route("/national")
def get_national():
    file_path = os.path.join(BASE_DIR, "data", "NationalUnivRanking.xlsx")
    return ExcelToJsonUtil.convert_to_json(file_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)