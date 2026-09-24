# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_IntMembers.py
# AUTHOR: Randall Nagy
#
counter = 1
for val in dir(123):
    if val[0] != '_':
        print(counter, val)
    counter += 1

