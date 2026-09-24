# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_TestMemDeltas.py
# AUTHOR: Randall Nagy
# File: sol_TestMemDeltas.py
#

str_mems = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
int_mems = ['as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
float_mems = ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
bool_mems = ['as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

def get_mems(type_):
    results = list()
    for val in dir(type_):
        if val[0] != '_':
            results.append(val)
    return results
 
def test_str():
    '''
    >>> test_str()
    True
    '''
    return get_mems('') == str_mems 

def test_int():
    '''
    >>> test_int()
    True
    '''
    return get_mems(1) == int_mems 

def test_float():
    '''
    >>> test_float()
    True
    '''
    return get_mems(0.0) == float_mems 

def test_bool():
    '''
    >>> test_bool()
    True
    '''
    return get_mems(True) == bool_mems 


import doctest
doctest.testmod()
