# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: act_MainNameFunc.py
# AUTHOR: Randall Nagy
#

def query_name_age():
    name = input("Name: ")
    print("Welcome, '", name, "'!")
    while True:
        try:
            return name, int(input("Age: "))
        except ValueError:
            print('Age is not numeric')

