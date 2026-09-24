# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-22 08:17:50
# FILE: act_MyListDelta.py
# AUTHOR: Randall Nagy
# File: act_MyListDelta.py
#

alist = ("Fred", "Ralph", "Zelda", "Zoe")

for ss in range(len(alist)):
    alist[ss] = "Guest " + alist[ss]
    print(alist[ss])

