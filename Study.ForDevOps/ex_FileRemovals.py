# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_FileRemovals.py
# AUTHOR: Randall Nagy
#
import os # new
import os.path
my_file = "myfile.txt"
if os.path.exists(my_file):
    os.unlink(my_file) # also os.remove()
    print("Deleted", my_file)
else:
    print("File", my_file, "not found.")

