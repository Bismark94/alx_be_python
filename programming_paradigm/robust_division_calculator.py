# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Attempts to convert numerator/denominator to float and perform a division.
    Catches:
      - ValueError if inputs are not numeric
      - ZeroDivisionError if denominator is zero
    Returns:
      - A string describing any errors
      - Or a string with the successful division result
    """
    try:
        # Convert the inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform the division
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
