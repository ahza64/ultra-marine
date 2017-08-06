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
