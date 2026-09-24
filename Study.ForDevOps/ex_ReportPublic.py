# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_ReportPublic.py
# AUTHOR: Randall Nagy
# List Comprehension:
#
def get_public(atype) -> list():
    return [a for a in dir(atype) if a[0] != '_']

# Common Report:
def report_public(atype):
    vals = get_public(atype)
    for ss, val in enumerate(vals, 1):
        print(f'{val:18}', end='')
        if ss % 4 == 0:
            print()
    print('\n\n')

if __name__ == '__main__':
    # Verifications:
    for type_ in 1, 1.0:
        print(type(type_),":\n")
        report_public(type_)
