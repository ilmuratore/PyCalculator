def add(x, y):
    """
    Adds two numbers.

    Args: 
        x: first number.
        y: second number.
    
    Returns:
        The sum of x and y.
    """

    return x + y    

def subtract (x, y): 
    
    """
    Subtracts two numbers.

    Args:
        x: first number.
        y: second number.

    Returns:
        The difference of x and y
    """
    
    return x - y


def multiply (x, y):

    """
    Multiplies two numbers.

    Args:
        x: first number.
        y: second number.

    Returns:
        The product of x and y
    """

    return x * y

def divide (x, y):
    """	
    Divide two numbers.

    Args:
        x: first number.
        y: second number.

    Returns:
        The quotient of x and y
    """
    if y == 0:
        return "Error: Division by zero"
    else:	
        return x / y