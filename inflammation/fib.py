def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    :param n: The index of the Fibonacci number to calculate.
    :type n: int
    :return: The nth Fibonacci number.
    :rtype: int
    :raises ValueError: If n is less than zero.
    
    :notes:
        This function uses a recursive implementation to calculate the Fibonacci number.
        The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for N < 0')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
