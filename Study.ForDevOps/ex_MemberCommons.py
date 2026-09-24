# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_MemberCommons.py
# AUTHOR: Randall Nagy
#
def members(type_, dict_):
    for val in dir(type_):
        if val in dict_:
            dict_[val] +=1
        else:
            dict_[val] = 1
    return len(dict_)


dict_ = dict()
for type_ in 1, 1.1, True:
    members(type_, dict_)

for key in dict_:
    if key[0] == '_':
        continue
    if dict_[key] == 3:
        print(key)
        
