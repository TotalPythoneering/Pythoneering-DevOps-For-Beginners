# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_StringFormatCaveats.py
# AUTHOR: Randall Nagy
# IndexError: Replacement index ... out of range
# for positional args tuple
#

print("[{:<15}]".format(name="Randall"))
print("[{:05}]".format(123))
print("[{1:>9}]".format(123.976))

