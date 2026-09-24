# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-22 08:36:25
# FILE: sol_MyWhile01.py
# AUTHOR: Randall Nagy
# File: sol_MyWhile01.py
# Related: ex_AsciiDump.py
#

def ascii_dump(*args, **kwargs):
    result = ''
    if not 'ival' in kwargs:
        kwargs['ival'] = 32
    if not 'mod' in kwargs:
        kwargs['mod'] = 4
    try:
        ival = kwargs['ival']
        mod = kwargs['mod']
        range_ = args[0]
        arange = range(ival, ival + range_)
        for ss, val in enumerate(arange, 1):
            result += f'{hex(val)}[{chr(val)}]'
            if not ss % mod:
                result += '\n'
    except Exception as ex:
        print(ex)
    return result

print(*ascii_dump(91, mod=8),sep='')
