from functools import reduce


def operate(sign, *args):
    def add():
        return reduce(lambda a, b: a + b, args)

    def subtract():
        return reduce(lambda a, b: a - b, args)

    def multiply():
        return reduce(lambda a, b: a * b, args)

    def divide():
        return reduce(lambda a, b: a / b, args)

    if sign == "+":
        return add()
    elif sign == '-':
        return subtract()
    elif sign == '*':
        return multiply()
    elif sign == '/':
        return divide()

