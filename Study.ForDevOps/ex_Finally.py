# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_Finally.py
# AUTHOR: Randall Nagy
#
name = input("Name: ")
while True:
    try:
        print('Got:', name, int(input("Age: ")))
        break
    except ValueError:
        print('Age is not numeric ...')
    finally:
        print('*' * len(name))

