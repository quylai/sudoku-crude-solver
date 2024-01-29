import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(

              "...9.3..."
              "..38274.."
              ".2.....8."
              "26.4.1.79"  #
              ".7.....5."  #
              "13.5.2.64"  #
              ".8.....9."
              "..41692.."
              "...7.8..."
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

# "96.8....5.5.92..46....1.......6.2.81.82.3.57.14.7.5.......5....71..49.5.2....8.34" #5R
# "...19.....29.54.6...7...93..5.7.2..347.....926..9.5.7..31...2...6.42.18.....61..." #5R
# ".57.3......1..9..5..8.45217.83.5....7.42.19.3....6.74.47652.1..1..7..4......1.57." #6R
# ".6..8..4.9..12.6.7.819..2........83.41.....69.95........6..917.1.2.54..8.3..1..2." #7R
# "...9.3.....38274...2.....8.26.4.1.79.7.....5.13.5.2.64.8.....9...41692.....7.8..." #7R

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
# az.prtSudoku(grid)  ##


def colsComp(grid):
  print("in colsComp")  ##

  def procThirdCol(grid, info, curColsSeq):
    # info[0] is intersected values array
    # info[1] is intersected coordinates array

    print(info[0])
    print(info[1])
    # print("------------------")

  


  #--------------------------------------- begins processing in colsComp
  colsSeq = np.array([
                      [0,1,2], [0,2,1], [1,2,0],
                      [3,4,5], [3,5,4], [4,5,3],
                      [6,7,8], [6,8,7], [7,8,6]
  ])


  for i in colsSeq:
    inter_info = az.find_inter_coord(grid, i, 'c')
    procThirdCol(grid, inter_info, i)
  #--------------------------------------- ends processing in colsComp
  
  return grid







#--------------------------------------- begins processing in main

grid = colsComp(grid)


# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)
# grid = az.rowsComp(grid)
# print("----------------------------------------")
# az.prtSudoku(grid)
#--------------------------------------- ends processing in main

#---------------------------------------------------------------------------------------
