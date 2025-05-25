def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide)
    on two numbers: num1 and num2.

    :param num1: float - The first number
    :param num2: float - The second number
    :param operation: str - The operation to perform ('add', 'subtract', 'multiply', 'divide')
    :return: float or str - The result of the operation, or a special message (e.g., divide by zero)
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
