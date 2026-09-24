# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-23 09:36:06
# FILE: sol_MyBannerDict.py
# AUTHOR: Randall Nagy
# File: sol_MyBannerDict.py
# Mission: Solution to act_MyBannerDict.py
#

prefix = \
   {1:"DEBUG", 2:"WARNING", 3:"ERROR", 4:"MESSAGE"}

def show_chars(num, token):
    return "\t" + (token * (num + 4))
            
def show_banner(ss, message):
    if ss < 1:
        ss = 1
    if ss > len(prefix):
        ss = len(prefix)
    message = prefix[ss] + ": " + message
    len_ = len(message)
    stars = show_chars(len_, '*')
    print(stars)
    print("\t* " + message + " *")
    print(stars)

def add_key(tag) -> int:
    if tag and not tag in prefix.values():
        result = len(prefix) + 1
        prefix[result] = tag
        return result

if __name__ == "__main__":
    show_banner(4, "The is a MESSAGE")
    value = add_key('TESTING')
    show_banner(value, "Testing Success!")
