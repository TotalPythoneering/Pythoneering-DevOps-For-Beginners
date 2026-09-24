# MISSION: Supporting ''Python 1100 - Python for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-04-05 09:34:29
# FILE: file_test3.py
# AUTHOR: Randall Nagy
#
import os

try:
    for root, dirs, files in os.walk('/'):
        for file in files:
            a_file = root + '/' + file
            a_file = a_file.replace('\\', '/')
            if a_file.lower().find('python') >= 0:
                file_info = os.stat(a_file)
                print(f'FOUND {a_file}')
                print(f'\t@ {file_info.st_mtime}')
except:
    print("\n\nException\n\n")

