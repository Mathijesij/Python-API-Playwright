# Define custom exception
class DivisionInputError(Exception):
    def __init__(self, value, message):
        super().__init__(f"Invalid input ({value}): {message}")

def safe_divide(a, b):
    if not isinstance(a, (int, float)):
        raise DivisionInputError(a, "Numerator must be a number")
    if not isinstance(b, (int, float)):
        raise DivisionInputError(b, "Denominator must be a number")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = safe_divide(1000, 20)
    print("Result:", result)
except DivisionInputError as e:
    print(f"Error1: {e}")
except ZeroDivisionError as e:
    print(f"Error2: {e}")
finally:
    print("Division process completed.")
