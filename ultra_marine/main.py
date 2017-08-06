"""
practice python calculator
"""
import sys
import foo

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/calculator', methods=['POST'])
def calculator():
    n1 = int(request.get_json()['n1'])
    n2 = int(request.get_json()['n2'])
    op = request.get_json()['op']
    ab = foo.Calc(n1, op, n2)
    totalNum = {
        "total": ab.total()
    }
    return jsonify(totalNum)

if __name__ == "__main__":

    c = foo.Calc(sys.argv[1], sys.argv[2], sys.argv[3])
    print c.total()
