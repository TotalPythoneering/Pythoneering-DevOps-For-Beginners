#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_MyBanner4.py
# AUTHOR: Randall Nagy
#

def MkString(num, token):
    return token * num
            
def Show(message):
    stars = MkString(20, '*')
    print(stars)
    print(message.center(20))
    print(stars)

Show(" SPECIAL ")
Show(" SALE ")
