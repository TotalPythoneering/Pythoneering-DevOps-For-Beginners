# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: demo_MainName.py
# AUTHOR: Randall Nagy
#

def first_class():
    ''' We are now test-able!
    >>> first_class()
    True
    '''
    return False # TC ERROR!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

