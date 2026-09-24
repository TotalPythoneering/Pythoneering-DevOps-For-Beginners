# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: ex_FileClassics.py
# AUTHOR: Randall Nagy
#
fh = None
try:
    fh = open("myfile.txt")
    line = fh.readline()
    value = int(line)
    print("Got: ", value)
except ValueError:
    print("ValueError: Bad Data.")
except IOError as ex:
    print(ex.strerror)
finally:
    if fh:
        fh.close()

