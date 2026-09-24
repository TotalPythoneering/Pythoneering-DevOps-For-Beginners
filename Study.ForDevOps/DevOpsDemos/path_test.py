# MISSION: Supporting ''Python 1100 - Python for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-04-02 07:34:26
# FILE: path_test.py
# AUTHOR: Randall Nagy
#
import os
zpath = os.getenv("PATH")
for dir_ in zpath.split(os.pathsep):
    lower = dir_.lower()
    if lower.find('python') >= 0:
        print(dir_)
        
