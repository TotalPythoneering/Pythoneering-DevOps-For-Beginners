# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-25 11:36:29
# FILE: sol_MyWhile.py
# AUTHOR: Randall Nagy
# File: sol_MyWhile.py
#

def block_dump(val=10, cols=10, max_=100):
    while True:
        print(f'{val} ', end='')
        val += 1
        if not val % cols:
            print()
            continue
        if val >= max_:
            break

block_dump(max_=90)

