# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-09 09:21:11
# FILE: ex_MatchCase.py
# AUTHOR: Randall Nagy
# File: ex_MatchCase.py
#

import random
def a_func():
    return random.randrange(1, 10)

# Before
while True:
    a_val = a_func()
    if a_val < 4:
        print(f"{a_val} < 5")
    elif a_val < 8:
        print(f"{a_val} < 8")
    else:
        print("Bingo!\n")
        break

# After
while True:
    match(a_val := a_func()):
        case 0|1|2|4:
            print(f"{a_val} < 5")
        case 5|6|7:
            print(f"{a_val} < 8")
        case _:
            print(f"Bingo!")
            break

# Caveats
while True:
    match(a_val := a_func()):
        case a_val < 5:
            print(f"{a_val} < 5")
        case 5|6|7:
            print(f"{a_val} < 8")
        case _:
            print(f"Bingo!")
            break

