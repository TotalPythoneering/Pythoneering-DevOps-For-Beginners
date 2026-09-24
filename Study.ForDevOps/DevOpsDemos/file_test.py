# MISSION: Supporting ''Python 1100 - Python for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-04-05 04:42:39
# FILE: file_test.py
# AUTHOR: Randall Nagy
#
import os

def get_python(a_dir):
    ''' Locate any python-string file
    in a directory
    '''
    for file in os.listdir(a_dir):
        lower = file.lower()
        if lower.find('python') != -1:
            return file
        
def get_python_path():
    ''' Locate any python-string file
    along the python $PATH / %PATH%
    '''
    zpath = os.getenv("PATH")
    for dir_ in zpath.split(os.pathsep):
        get_python(dir_)
        

for root, dirs, files in os.walk('/'):
    for file in files:
        if file.find('python.exe') == 0:
            print(f'FILE:{root}@{file}')





