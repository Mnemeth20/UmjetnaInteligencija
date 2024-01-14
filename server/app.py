from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/pocetna_csv', methods=['GET'])
def pocetna():
    return send_file('./novo.csv')

@app.route('/pocetna_json', methods=['GET'])
def prva():
    return send_file('./staro.json')