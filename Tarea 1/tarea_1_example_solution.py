def operation_selector(num1, num2, op):
    """
    Applies the operation defined by op to num1 and num2,
    in that order.

    Parameters:
    - num1 (int): First operand
    - num2 (int): Second operand
    - op (str): Operation, must be one of +, -, *, &

    Returns:
    - (result_code, result)
    -- result_code (int): A success/error code
    -- result (int or None): The result of applying the operation
    to the operands, or None if an error occurred.
    """

    # Check that both operands are ints
    if not (type(num1) is int and type(num2) is int):
        # Return an error error code if at least one of them isn't
        return -50, None

    # Check that the operator selector is a str
    if not type(op) is str:
        # Return an error code if it isn't
        return -60, None

    # Check that the operator selector is one of the expected options
    if op not in ("+", "-", "*", "&"):
        # Return an error code if it isn't
        return -70, None

    # Once this part is reached all checks have been passed, and the result
    # can be calculated
    result_code = 0  # Success
    result = 0

    # Apply the selected operation
    match op:
        case "+":
            result = num1 + num2
        case '-':
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "&":
            result = num1 & num2

    return result_code, result


def calculo_promedio(lista_valores):
    """
    Calculates the average of a list of numeric values.

    Parameters:
    lista_valores (list): A list of int or float values to calculate
    the average of.

    Returns:
    - (result_code, average)
    -- result_code (int): A success/error code
    -- average (int or float or None): Average of all values
    contained in the list, or None if an error occurred.
    """

    # Helper function to check if a variable is
    # of a numeric type (int or float)
    def is_numeric(x):
        return type(x) in (int, float)

    # Check that all items in the supplied list are of a numeric type
    if not all([is_numeric(x) for x in lista_valores]):
        # Return an error code if at least one them isn't
        return -80, None

    # Check that the list doesn't contain more than 10 items
    if len(lista_valores) > 10:
        # Return an error code if it does
        return -90, None

    # Once this part is reached all checks have been passed, and the result
    # can be calculated
    result_code = 0  # Success
    average = sum(lista_valores) / len(lista_valores)

    return result_code, average
