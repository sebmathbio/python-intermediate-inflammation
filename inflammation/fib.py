def fibonacci(n):
    """Calculate the nth Fibonacci number.

    A recursive implementation of Fibonacci array elements.

    Params
     ----
     n: integer

    Raises
     ----
    ValueError: raised if n is less than zero

    Returns
     ----
     Fibonacci number
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for N < 0')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)