# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_BoolAnd.py
# AUTHOR: Randall Nagy
#

def f1():
    print("f1, ", end='')
    return True

def f2():
    print("f2.")
    return True

ops = "pass." if (f1() and f2()) else "fail!"
print(ops)

