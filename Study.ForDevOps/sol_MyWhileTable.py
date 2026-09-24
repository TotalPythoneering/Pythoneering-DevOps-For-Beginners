# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-03-22 17:41:11
# FILE: sol_MyWhileTable.py
# AUTHOR: Randall Nagy
# File: sol_MyWhileTable.py
#

start = 10
stop = 90
total = 0
while True: # Loop forever!
    print(start, end=' ')
    total += 1; start += 1
    if(total % 10 == 0):
        print()
        continue
    if(start >= stop):
        break
print("...")


        
    

        
