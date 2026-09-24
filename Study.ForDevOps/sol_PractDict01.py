# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-23 09:48:12
# FILE: sol_PractDict01.py
# AUTHOR: Randall Nagy
# File: sol_PractDict01.py
# Mission: Solution to act_PractDict01.py
#

fields = {"Name":None, "Age":None, "Credit":None}

for key in fields:
    fields[key] = input(key + ": ")
    
print()
print('*'*5, "Report", '*'*5)
for key in fields:
    print(f"{key:>8}: {fields[key]}")
