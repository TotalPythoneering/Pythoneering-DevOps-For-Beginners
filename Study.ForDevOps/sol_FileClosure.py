# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_FileClosure.py
# AUTHOR: Randall Nagy
#
with open("myfile.txt") as fh:
    try:
        print("Got: ", int(fh.readline()))
    except Exception as ex:
        print(ex)

