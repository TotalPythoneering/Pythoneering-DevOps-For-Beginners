# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-22 17:34:56
# FILE: act_MyWhile01.py
# AUTHOR: Randall Nagy
# File: act_MyWhile01.py
#

def ascii_dump(range_, ival=32, mod=4):
    result = ''
    arange = range(ival, ival + range_)
    for ss, val in enumerate(arange, 1):
        result += f'{hex(val)}[{chr(val)}]'
        if not ss % mod:
            result += '\n'
    return result

print(*ascii_dump(91, mod=8),sep='')

