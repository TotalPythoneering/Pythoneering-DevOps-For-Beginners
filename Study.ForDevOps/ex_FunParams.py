# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-25 11:57:22
# FILE: ex_FunParams.py
# AUTHOR: Randall Nagy
# File: ex_FunParams.py
#

def fun_params(*args, **kwargs):
    print(args)
    print(kwargs)

fun_params(1, "bongo",
           Key=None, max_=123)

