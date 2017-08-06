"""
practice python calculator
"""
import sys
import foo

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/calculator')
def calculator():
    return "these aren't the droids you're looking for"

if __name__ == "__main__":

    c = foo.Calc(sys.argv[1], sys.argv[2], sys.argv[3])
    print c.total()
