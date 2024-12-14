# Problem 1: Calculator
class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'Addition':
            return self.a + self.b
        elif self.operation == 'Subtraction':
            return self.a - self.b
        elif self.operation == 'Multiplication':
            return self.a * self.b
        elif self.operation == 'Division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example usage
calc = Calculator(10.5, 2.5, 'Addition')
print(calc.calculate())