#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-23 11:38:44
# FILE: sol_MyListReportFile.py
# AUTHOR: Randall Nagy
#

def list_report(info, a_list, fh):
    nelem = len(a_list)
    message = info + " has " + \
              str(nelem) + " items"
    banner = '*' * len(message)
    print(banner, file=fh)
    print(message, file=fh)
    print(banner, file=fh)
    return nelem

a_file = "MyListReport.txt"
with open(a_file, 'w') as fh:
    list_report("BUILTINS",
                dir(__builtins__),
                fh)
with open(a_file) as fh:
    for line in fh:
        print(line, end='')

        
