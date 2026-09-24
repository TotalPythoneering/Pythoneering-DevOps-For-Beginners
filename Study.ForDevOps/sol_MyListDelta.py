# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-22 08:11:53
# FILE: sol_MyListDelta.py
# AUTHOR: Randall Nagy
# File: sol_MyListDelta.py
#

names = ("Fred", "Ralph", "Zelda", "Zoe")
alist = list(names)

for ss in range(len(alist)):
    alist[ss] = "Guest " + alist[ss]
    print(alist[ss])

