import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
# inputs = list("......43."
#               "..52..8.7"
#               ".8.7....."
#               ".3..48.5."#
#               ".4.6....2"#
#               ".9..52.4."#
#               ".6.4....."
#               "..19..6.3"
#               "......57.".translate({46: 48}))
inputs = list("2.9...43."
              "..52948.7"
              ".8.7...95"
              ".3..48.5."#
              ".4.6....2"#
              ".9..52.4."#
              ".6.4....."
              "..19..6.3"
              "......57.".translate({46: 48}))

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


def rowsComp(grid):
  row1 = grid[0,]
  row2 = grid[1,]
  row3 = grid[2,]

  def find_inter_coord(arrA, arrB):
    # getting all value that are intersected
    inter_val = np.intersect1d(arrA, arrB, assume_unique=False)
    if (np.where(inter_val == 0)[0].size != 0):
      temp = inter_val
      inter_val = np.delete(temp, [0])

    inter_val_coord = np.array([], dtype=int)  # initializing

    for idx, x in np.ndenumerate(inter_val):
      if (x != 0):  # bypassing intersection of '0'

        j = np.where(arrA == x)[0]
        k = np.where(arrB == x)[0]

        # append intersected indices from arrA & arrB, to a 1D array,
        # then reshape it into 2D array m x 2
        inter_val_coord = np.append(inter_val_coord, [j, k]).reshape(idx[0]+1, 2)
    return inter_val, inter_val_coord
  
  inter_info = find_inter_coord(row1, row2)



  # print("inter_val_coord is:")
  # print(inter_info[0])
  # print(inter_info[1])
  # print(row1)
  # print(row2)

  return grid
  

rowsComp(grid)
az.prtSudoku(grid)

#---------------------------------------------------------------------------------------
#
#