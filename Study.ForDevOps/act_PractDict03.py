# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-23 10:12:51
# FILE: act_PractDict03.py
# AUTHOR: Randall Nagy
# File: act_PractDict03.py
# Mission: Record collection into data files
#

def get_data(fields) -> dict():
    pass

def show_report(fields):    
    print()
    print('*'*5, "Report", '*'*5)
    for key in fields:
        print(f"{key:>8}: {fields[key]}")

data = {"Name":None, "Age":None, "Credit":None}
records = list()

for _ in range(5):
    pass
    
