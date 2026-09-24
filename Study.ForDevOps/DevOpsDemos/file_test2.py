# MISSION: Supporting ''Python 1100 - Python for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-04-05 09:07:38
# FILE: file_test2.py
# AUTHOR: Randall Nagy
#
import os

try:
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file.find('python') != -1:
                print(f'FILE:{root}@{file}')
except:
    print("\n\nException\n\n")

