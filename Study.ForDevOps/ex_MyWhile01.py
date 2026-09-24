# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-25 11:31:34
# FILE: ex_MyWhile01.py
# AUTHOR: Randall Nagy
# File: ex_MyWhile01.py
#

def ascii_dump(val = 32, max_ = 127):
    while val < 256:
        print(f'{hex(val)}:[{chr(val):>2}] ', end='')
        val += 1
        if not val % 4:
            print()
            continue
        if val >= max_:
            break

ascii_dump()

