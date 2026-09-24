# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-22 05:19:20
# FILE: ex_ShowMemPubs.py
# AUTHOR: Randall Nagy
# File: ex_ShowMemPubs.py
#

def get_mems(type_):
    results = list()
    for val in dir(type_):
        if val[0] != '_':
            results.append(val)
    return results

report = get_mems(set())
for ss, line in enumerate(report, 1):
    print(f'{line:<30}', end=' ')
    if ss % 2 == 0:
        print()
