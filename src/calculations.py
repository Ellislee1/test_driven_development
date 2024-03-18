class Calculations:
    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiplication(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def division(a: int, b: int) -> float:
        if b == 0:
            raise ZeroDivisionError()

        return float(a / b)
