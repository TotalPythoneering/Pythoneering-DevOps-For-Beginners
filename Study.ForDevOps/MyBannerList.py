# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-22 08:46:30
# FILE: MyBannerList.py
# AUTHOR: Randall Nagy
# File: MyBannerList.py
#

prefix = ["DEBUG", "WARNING", "ERROR", "MESSAGE"]

def ShowChars(num, token):
    return "\t" + (token * (num + 4))
            
def Show(ss, message):
    if ss < 1:
        ss = 1
    if ss > len(prefix):
        ss = len(prefix)
    message = prefix[ss - 1] + ": " + message
    xx = len(message)
    stars = ShowChars(xx, '*')
    print(stars)
    print("\t* " + message + " *")
    print(stars)

def Append(zpre):
    prefix.append(zpre)

Append("TEST")
Show(999, "The is a MESSAGE")
Show(1, "Doh!")

for dat in prefix:
    print(dat)
