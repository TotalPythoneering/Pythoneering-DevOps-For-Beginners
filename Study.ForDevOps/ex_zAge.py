# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-17 10:34:06
# FILE: ex_zAge.py
# AUTHOR: Randall Nagy
# File: ex_zAge.py
#

zAge = 16
if zAge >= 21:
    print("You can drive an 18 wheeler!")
if zAge >= 16:
    print("You can drive a car.")
if zAge >= 16 and zAge <= 18:
    print("Time to learn how to drive a 'Rig?")

if zAge >= 16 or zAge <= 18:
    print("Time to learn how to drive a 'Rig?")

if (zAge >= 16) or (zAge <= 18):
    print("Time to learn how to drive a 'Rig?")

zAge = 16
if not ((zAge >= 16) or (zAge <= 18)):
    print("Time to learn how to drive a 'Rig?")
else:
    print("Classic Negation!")



