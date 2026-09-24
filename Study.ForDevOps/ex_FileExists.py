# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_FileExists.py
# AUTHOR: Randall Nagy
#
import os.path
file = True if os.path.exists("myfile.txt") else False
if file:
    print("File ok.")
else:
    print("File nokay.")

