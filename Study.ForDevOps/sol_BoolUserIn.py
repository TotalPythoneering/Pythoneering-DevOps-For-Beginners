# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_BoolUserIn.py
# AUTHOR: Randall Nagy
#

def is_logged_in():
    print("f1, ", end='')
    return False

def is_registered_user():
    print("f2.")
    return True

if is_logged_in() or is_registered_user():
    print("Welcome!")
else:
    print("Access Denied.")

