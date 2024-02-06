import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(
"...1.........82.......7..9......6......8........9........6.3......7.........54..."
              .translate({46: 48}))  
  

# ".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2."
#32#  6# - r;  4# - c;  15# - rcrc;    49# - rcbrcbrcbrcb;  49# - rcbhrcbhrcbh

# "...9.3.....38274...2.....8.26.4.1.79.7.....5.13.5.2.64.8.....9...41692.....7.8..."
#32#  7# - rr; 7# - cc; 19# - rcrcrc;  25# - rcbrcb;        49# - rcbhrcbhrcbhrcbh

# "...1.4.....1...9...9.7.3.6.8.7...1.6.........3.4...5.9.5.4.2.3...8...6.....8.6..."
#24#  2# - r;  0# - c;  2# - rc;       5# - rcbrcb;         5# - rcbhrcbh
####  -------- -------- -------------- --------------------

# "..6.7...8.....5.7..7...14.57.9.4.6....4...5..3.5.8.2...6...87.2.....3.4...2.5...9"
#28#  #13 - rcbhrcbhrcbh



# for visual
#
#   a b c d e f g h i
#  -------------------
# 1|     |     |     |
# 2|     |     |     |
# 3|     |     |     |
#  -------------------
# 4|     |     |     |
# 5|     |     |     |
# 6|     |     |     |
#  -------------------
# 7|     |     |     |
# 8|     |     |     |
# 9|     |     |     |
#  -------------------


# create a 1D array from list (inputs), then reshape it into 9x9 array
grid = np.array(inputs, dtype=int).reshape(9,9)
az.prtSudoku(grid)  ##








#--------------------------------------- begins processing in main

# testingGrid = vSingCand(grid)

# r=rowsComp, c=colsComp, b=boxSingCand, h=hSingCand
# az.analyzeSeqs(grid, "rcbh", "rcbhrcbh", "rcbhrcbhrcbh", "rcbhrcbhrcbhrcbh")
az.analyzeSeqs(grid, "v")





print("----------------------------------------")  ##
# az.prtSudoku(grid)  ##

#--------------------------------------- ends processing in main







#---------------------------------------------------------------------------------------
'''
'''


