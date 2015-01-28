__author__ = 'alberto'


class SimpleCalculator():
    def sum(self, values):
        result = 0.0
        for value in values:
            result = result + value
        return result

    def multiply(self, values):
        result = 1.0
        for value in values:
            result = result * value
        return result

    def divide(self, values):
        pass