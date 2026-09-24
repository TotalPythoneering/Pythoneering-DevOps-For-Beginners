# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-22 17:02:08
# FILE: ex_AsciiDump.py
# AUTHOR: Randall Nagy
# File: ex_AsciiDump.py
#
def dump_chars(s_val = 32, e_val = 126):
    column = 1
    for val in range(s_val, e_val + 1):
        print(
            f'[{hex(val)}]:\[{chr(val):>2}]',
            end='')
        if not column % 4:
            print()
        column += 1

dump_chars()

