def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = a / b
    return c


def square(a, ):
    a = int(a)
    return a * a


def square_root(a, ):
    a = int(a)
    return a * a / a


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

    def square(self, a, ):
        self.result = a * a
        return self.result

    def root(self, a, ):
        self.result = a * a / a
        return self.result
