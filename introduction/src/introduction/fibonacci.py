def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    # BEGIN QUESTION 1.1
    "*** REPLACE THIS LINE ***"
    first = 0
    second = 1

    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(1, n):
            num = first + second
            first = second
            second = num
        return second

    # END QUESTION 1.1

