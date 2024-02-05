import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(
".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2."
              .translate({46: 48}))  
  
# "...1.4..."
# "..1...9.."
# ".9.7.3.6."
# "8.7...1.6" #
# "........." #
# "3.4...5.9" #
# ".5.4.2.3."
# "..8...6.."
# "...8.6..."
              # .translate({46: 48})) 


# ".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2."
####  6# - r;    4# - c;    15# - rcrc;  49# - rcsrcsrcsrcs

# "...9.3.....38274...2.....8.26.4.1.79.7.....5.13.5.2.64.8.....9...41692.....7.8..."
####  7# - rr;   7# - cc;   17# - rcrc   25# - rcsrcs

# "...1.4.....1...9...9.7.3.6.8.7...1.6.........3.4...5.9.5.4.2.3...8...6.....8.6..."
####  2# - r;    0# - c;    2# - rc      5# - rcsrcs;
####  ---------- ---------- ------------  


# for visual
#
#   a b c d e f g h i
#  -------------------
# 1|     |     |     |
# 2|     |     |     |
# 3|     |     |     |
#  -------------------
# 4|  2  |     |     |
# 5|     |     |     |
# 6|     |     |     |
#  -------------------
# 7|     |     |     |
# 8|     |     |     |
# 9|     |     |     |
#  -------------------
#
#  6 8 2 | 1 9 4 | 3 5 7
#  7 3 1 | 5 6 8 | 9 2 4
#  4 9 5 | 7 2 3 | 8 6 1
# -------|-------|-------
#  8 2 7 | 9 3 5 | 1 4 6
#  5 1 9 | 6 4 7 | 2 8 3
#  3 6 4 | 2 8 1 | 5 7 9
# -------|-------|-------
#  9 5 6 | 4 1 2 | 7 3 8
#  2 4 8 | 3 7 9 | 6 1 5
#  1 7 3 | 8 5 6 | 4 9 2


# create a 1D array from list (inputs), then reshape it into 9x9 array
grid = np.array(inputs, dtype=int).reshape(9,9)
az.prtSudoku(grid)  ##



#--------------------------------------- begins processing in main


# r=rowsComp, c=colsComp, s=singCand
az.analyzeSeqs(grid, "rc", "rcrc", "rcsrcsrcsrcs", "", "")



print("----------------------------------------")  ##
az.prtSudoku(grid)  ##

#--------------------------------------- ends processing in main







#---------------------------------------------------------------------------------------
'''


'''


