# MISSION: Supporting ''Python 1100 - Python for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-04-06 06:35:07
# FILE: file_bin.py
# AUTHOR: Randall Nagy
#

with open ('c:/study/WTEST2.TXT', 'w') as fh:
    zbytes = "THIS\nIS\nA\nTEST\n"
    try:
        print(zbytes, end='', file=fh)
    except:
        print("print() requires a string.")

