# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_OperatorCommons.py
# AUTHOR: Randall Nagy
#
def test_subs():
    '''
    >>> 123 - 456
    -333
    >>> test_subs()
    True
    '''
    try:
        "123" - "1"
    except:
        return True


def test_str_mul():
    '''
    >>> test_str_mul()
    True
    '''
    try:
        '123' * '2'
    except:
        return True
    return False


def test_equality():
    '''
    >>> 'abc' == 'abc'
    True
    >>> 'abc' != 'abc'
    False
    >>> 123 == 321
    False
    >>> 123 != 321
    True
    '''
    pass


def test_mult():
    '''
    >>> '*' * 5
    '*****'
    >>> 5 * 5
    25
    '''
    pass


import doctest
doctest.testmod()
