# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-22 08:51:48
# FILE: act_MyBannerList.py
# AUTHOR: Randall Nagy
# File: act_MyBannerTup.py
# Mission: Convert to a mutable prefix list.
#

prefix = ("DEBUG", "WARNING", "ERROR", "MESSAGE")

def ShowChars(num, token):
    return "\t" + (token * (num + 4))
            
def Show(ss, message):
    if ss < 1:
        ss = 1
    if ss > 4:
        ss = 4
    message = prefix[ss - 1] + ": " + message
    xx = len(message)
    stars = ShowChars(xx, '*')
    print(stars)
    print("\t* " + message + " *")
    print(stars)

Show(4, "The is a MESSAGE")
Show(1, "Doh!")
