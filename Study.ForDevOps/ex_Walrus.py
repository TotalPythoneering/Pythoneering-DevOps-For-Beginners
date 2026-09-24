# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-09 09:00:32
# FILE: ex_Walrus.py
# AUTHOR: Randall Nagy
# File: ex_Walrus.py
#

def a_func():
    return 9

# Before
a_val = a_func()
if a_val:
    print(f"a_val = {a_val}")
    
# After
if a_val := a_func():
    print(f"a_val := {a_val}")


