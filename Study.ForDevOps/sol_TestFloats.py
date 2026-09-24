# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-17 11:25:44
# FILE: sol_TestFloats.py
# AUTHOR: Randall Nagy
# File: sol_TestFloats.py
#

'''
>>> val = 123.456E64; val
1.23456e+66
>>> val.imag
0.0
>>> val.real
1.23456e+66
>>> val.is_integer()
True
>>> val.__getformat__('float')
'IEEE, little-endian'
'''

import doctest
doctest.testmod()
