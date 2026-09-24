# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-25 12:14:59
# FILE: sol_PepBannerDT.py
# AUTHOR: Randall Nagy
# File: sol_PepBannerDT.py
#
            
def banner(message):
    '''
    >>> print(banner("foo"))
    *******
    * foo *
    *******
    <BLANKLINE>
    >>> print(banner("food for all"))
    $$$$$$$$$$$$$$$$
    * food for all *
    $$$$$$$$$$$$$$$$
    <BLANKLINE>
    '''

    len_ = len(message)
    char = '$' if len_ > 5 else '*'
    stars = char * (len_ + 4) + '\n'
    result = ''
    result += stars
    result += f'* {message.center(len_)} *\n'
    result += stars
    return str(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

