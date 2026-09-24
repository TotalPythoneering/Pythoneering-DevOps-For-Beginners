# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-23 08:51:10
# FILE: ex_AsciiDumpQ.py
# AUTHOR: Randall Nagy
# File: ex_AsciiDumpQ.py
#

def dump_line(s_val, nelem):
    for val in range(s_val, s_val + nelem):
        print(
            f'[{hex(val)}]:\[{chr(val):>2}]',
            end='')

def dump_lines(s_val = 32, e_val = 126):
    cols = int((e_val / s_val) + 1)
    while True:
        dump_line(s_val, cols)
        print("\n> Continue?")
        if input("> y/n: ") == 'y':
            s_val += cols
            continue
        print('...')
        break


dump_lines()

