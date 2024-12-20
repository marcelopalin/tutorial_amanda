from typing import Union

def soma(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.

    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"O cabeçudo!! Não leu a documentação! int or float for 'a', got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
    return a + b


def subtracao(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first number.

    Args:
        a (int or float): The number from which to subtract.
        b (int or float): The number to subtract.

    Returns:
        int or float: The result of the subtraction.

    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
    return a - b