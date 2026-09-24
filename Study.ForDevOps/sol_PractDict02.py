# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-23 12:44:53
# FILE: sol_PractDict02.py
# AUTHOR: Randall Nagy
# File: sol_PractDict02.py
# Mission: Solution to act_PractDict02.py
#

def get_data(fields) -> dict():
    for key in fields:
        fields[key] = input(key + ": ")
    return fields

def show_report(fields):    
    print()
    print('*'*5, "Report", '*'*5)
    for key in fields:
        print(f"{key:>8}: {fields[key]}")

data = {"Name":None, "Age":None, "Credit":None}
records = list()

for _ in range(5):
    record = get_data(data.fromkeys(data.keys()))
    records.append(record)
    show_report(record)
    
    
