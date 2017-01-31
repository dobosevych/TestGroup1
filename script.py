def num_num(n):
    """
    Inverses integer number.

    :param n: integer number
    :return: inversed integer number

    >>> num_num(10)
    1
    >>> num_num(2017)
    7102
    """
    return int(str(n)[::-1])