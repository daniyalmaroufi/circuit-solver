from flask import Flask, render_template, url_for, request, jsonify
from Core.Circuit import Circuit
from Core.Ui import getInput
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

app = Flask(__name__, template_folder='Templates', static_folder='static',  static_url_path='/static')

flask_debug = False

global_circuit = [Circuit()]

@app.route('/', methods = ['GET'])
def page():
    global global_circuit
    del global_circuit[0]
    global_circuit.append(Circuit())
    return render_template('index.html')

@app.route('/state/<string:statement>', methods = ['POST'])
def handle_statement(statement):
    statement = statement.replace('#', ' ')
    ans = getInput(circuit=global_circuit, statement=statement)
    if ans is not None:
        return ans
    return 'ok'


if __name__ == '__main__':
    app.run(port=8000, debug=flask_debug)
