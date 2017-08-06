"""
practice python calculator
"""
import sys
# from ultra_marine import calc
# Calc = calc.Calc()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class Calc:
    num1 = None
    num2 = None
    oper = None

    def __init__(self, num1, oper, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.oper = oper

    def total(self):
        if self.oper == "+":
            return self.num1 + self.num2
        if self.oper == "-":
            return self.num1 - self.num2
        if self.oper == "x":
            return self.num1 * self.num2
        if self.oper == "/":
            return self.num1 / self.num2

if __name__ == "__main__":

    c = Calc(sys.argv[1], sys.argv[2], sys.argv[3])
    print c.total()
