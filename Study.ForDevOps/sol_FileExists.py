# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_FileExists.py
# AUTHOR: Randall Nagy
#
import os.path
my_file = "myfiletoo.txt"
if os.path.exists(my_file):
    with open(my_file, 'rt') as fh:
        print(fh.read())
else:
    with open(my_file, 'wt') as fh:
        print("We\nhave\nlines!", file=fh)
    print("Created", my_file)

