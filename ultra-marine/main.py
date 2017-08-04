"""
practice python calculator
"""
import sys

class Calc:
    num1 = None
    num2 = None
    oper = None

    def __init__(self, num1, oper, num2):
        self.num1 = num1
        self.num2 = num2
        self.oper = oper
        print "Hello"

    def Total(self):
        if self.oper == "+":
            return self.num1 + self.num2

if __name__ == "__main__":

    c = Calc(2, "+", 2)
    print c.Total()
