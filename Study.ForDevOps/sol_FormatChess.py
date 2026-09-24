#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for DevOps.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Pythoneering-DevOps-For-Beginners
# DATE: 2022-02-16 19:50:51
# FILE: sol_FormatChess.py
# AUTHOR: Randall Nagy
#

# '♔♕♖♗♘♙♚♛♜♝♞♟'

glyphs = ''
for val in range(9812, 9824):
    glyphs += chr(val)

for val in glyphs:
    print('%c' % val, '%a' % val)

print("repr()\t", repr(glyphs))
print("str()\t ", str(glyphs))
print("ascii()\t", ascii(glyphs))

