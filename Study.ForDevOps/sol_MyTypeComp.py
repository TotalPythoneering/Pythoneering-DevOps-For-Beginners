# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_MyTypeComp.py
# AUTHOR: Randall Nagy
# File: sol_MyTypeComp.py
#

'''
>>> test_ease()
iNum != sNum
str(iNum) == sNum
'''
def test_ease():
    sNum = "20" # s = "string"
    iNum = int(sNum) # i = "integer"
    if iNum == sNum:
        print("iNum == sNum")
    else:
        print("iNum != sNum")

    if str(iNum) == sNum:  # str copy
        print("str(iNum) == sNum")
    else:
        print("str(iNum) != sNum")


import doctest
doctest.testmod()
