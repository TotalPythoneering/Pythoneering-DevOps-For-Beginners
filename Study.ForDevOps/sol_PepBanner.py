# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-25 10:00:22
# FILE: sol_PepBanner.py
# AUTHOR: Randall Nagy
# File: sol_PepBanner.py
#
            
def banner(message):
    len_ = len(message)
    char = '$' if len_ > 5 else '*'
    stars = char * (len_ + 4)
    print(stars)
    print(f'* {message.center(len_)} *')
    print(stars)

banner("The is a MESSAGE")
banner("Doh!")

