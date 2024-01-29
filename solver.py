import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(

".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2."
              .translate({46: 48}))  
  
              # "...9.3..."
              # "..38274.."
              # ".2.....8."
              # "26.4.1.79"  #
              # ".7.....5."  #
              # "13.5.2.64"  #
              # ".8.....9."
              # "..41692.."
              # "...7.8..."
              # .translate({46: 48}))  ## orig, with proc 4 times of rowsComp, 7# solved


# ".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2."
#### 7# w/ rrrr; 4# w/ cccc; 15# w/ rcrcrcrc
# "...9.3.....38274...2.....8.26.4.1.79.7.....5.13.5.2.64.8.....9...41692.....7.8..."
#### 7# w/ rrrr; 4# w/ cccc;

# for visual
#
#  2 7 9 | 5 8 6 | 4 3 1
#  3 1 5 | 2 9 4 | 8 6 7
#  6 8 4 | 7 1 3 | 2 9 5
# -------|-------|-------
#  7 3 2 | 1 4 8 | 9 5 6
#  5 4 8 | 6 7 9 | 3 1 2
#  1 9 6 | 3 5 2 | 7 4 8
# -------|-------|-------
#  8 6 7 | 4 3 5 | 1 2 9
#  4 5 1 | 9 2 7 | 6 8 3
#  9 2 3 | 8 6 1 | 5 7 4
#
# -------------------
# |     |     |4 3  |
# |    5|2    |8   7|
# |  8  |7    |     |
# -------------------
# |  3  |  4 8|  5  |
# |  4  |6    |    2|
# |  9  |  5 2|  4  |
# -------------------
# |  6  |4    |     |
# |    1|9    |6   3|
# |     |     |5 7  |
# -------------------
#
#   a b c d e f g h i
#  -------------------
# 1|0 1 2|3 4 5|6 7 8|
# 2|9 0 1|2 3 4|5 6 7|
# 3|8 9 0|1 2 3|4 5 6|
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




# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)

# grid = az.colsComp(grid)
# grid = az.colsComp(grid)
# grid = az.colsComp(grid)
# grid = az.colsComp(grid)

grid = az.rowsComp(grid)
grid = az.colsComp(grid)
grid = az.rowsComp(grid)
grid = az.colsComp(grid)
grid = az.rowsComp(grid)
grid = az.colsComp(grid)
grid = az.rowsComp(grid)
grid = az.colsComp(grid)




print("----------------------------------------")
az.prtSudoku(grid)
#--------------------------------------- ends processing in main

#---------------------------------------------------------------------------------------
