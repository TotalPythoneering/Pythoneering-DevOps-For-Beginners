# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_Bool_is.py
# AUTHOR: Randall Nagy
# Two operators: When 'is' and '==' agree
#
ops = "same." if 'abc' is 'abc' else "not!"
print(ops)

ops = "same." if 'abc' == 'abc' else "not!"
print(ops)


# Three operators: Evaluation Order - Not expected?
ops = "same." if 'abc' is 'abc' is True else "not!"
print(ops)

ops = "same." if 'abc' == 'abc' == True else "not!"
print(ops)


# 'Parenes will fix it:
ops = "same." if ('abc' is 'abc') is True else "not!"
print(ops)

ops = "same." if ('abc' == 'abc') == True else "not!"
print(ops)


