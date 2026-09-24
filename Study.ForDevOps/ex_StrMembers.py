# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_StrMembers.py
# AUTHOR: Randall Nagy
#

for ss, val in enumerate(dir("")):
    if val[0] != '_' and len(val) < 16:
        print(f'{val:<16}', end='')
        if ss % 4 == 0:
            print()

