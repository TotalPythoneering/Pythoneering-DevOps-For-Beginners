# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-17 11:19:26
# FILE: sol_TestPromos.py
# AUTHOR: Randall Nagy
# File: sol_TestPromos.py
#

def test_muls():
    '''
    >>> 5 * 5
    25
    >>> 5 ** 5
    3125
    '''
    pass

def test_divs():
    '''
    >>> 5 / 5
    1.0
    >>> 5 // 5
    1
    '''
    pass

def test_promos():
    '''
    >>> True + True
    2
    >>> True + 1
    2
    >>> True * 2 + 2.0
    4.0
    '''
    pass

def test_selfs():
    '''
    >>> a = 1; a += True; a
    2
    >>> a = 1; a += True; a += 2.567; a
    4.567
    '''
    pass

import doctest
doctest.testmod()
