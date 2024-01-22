import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(
              "2795..43."
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

  def find_inter_coord(arrA, arrB, arrC):
    # getting all value that are intersected, between row1 & row2
    inter_val = np.intersect1d(arrA, arrB, assume_unique=False)
    interWithRowC = np.intersect1d(inter_val, arrC, assume_unique=False)


    # turn all value of inter_val that matched with interWithRowC, equal 0
    for idx, i in np.ndenumerate(inter_val):
      for j in interWithRowC:
        if (i == j):
          inter_val[idx[0]] = 0

    # deleting all element with value of 0, in array inter_val
    inter_val = np.sort(inter_val)
    while (np.where(inter_val == 0)[0].size != 0):
      temp = inter_val
      inter_val = np.delete(temp, [0])

    inter_val_coord = np.array([], dtype=int)  # initializing array
    for idx, x in np.ndenumerate(inter_val):

      j = np.where(arrA == x)[0]
      k = np.where(arrB == x)[0]

      # append intersected indices from arrA & arrB
      inter_val_coord = np.append(inter_val_coord, [j, k]).reshape(idx[0]+1, 2)

    return inter_val, inter_val_coord

  def procThird(grid, info):
    # info[0] is value list
    # info[1] is coord list

    for idx, i in np.ndenumerate(info[0]):  # in value
      rowBlocOccupy = [0,0,0]  # flags

      for j in info[1][idx]:  # in coord
        for k in range(9):  # flagging rowBloc existed targeted number
          if (j == k):
            if (k in range(0,3)):
              rowBlocOccupy[0] = 1
            elif (k in range(3,6)):
              rowBlocOccupy[1] = 1
            elif (k in range(6,9)):
              rowBlocOccupy[2] = 1
      
      # assigning indices to targeted row block
      for xdx, x in np.ndenumerate(rowBlocOccupy):
        if (x == 0):
          if (xdx[0] == 0):
            tarRowBloc = [0,1,2]
          elif (xdx[0] == 1):
            tarRowBloc = [3,4,5]
          elif (xdx[0] == 2):
            tarRowBloc = [6,7,8]

      # rowBlocElement = [8,8,8]
      # # initial iteration thru target row block indices
      # # to note which element is vacant; 1=occupied 0=vacant
      # for ydx, y in np.ndenumerate(tarRowBloc):
      #   if (row3[y] == 0):
      #     rowBlocElement[ydx[0]] = 0
      #   else:
      #     rowBlocElement[ydx[0]] = 1

      # print(rowBlocElement)

  



    # print(type(info))
    print("inter_info is:")
    print(info[0])
    print(info[1])
    
    return grid



  #--------------------------------------- processing in rowsComp
  inter_info = find_inter_coord(row1, row2, row3)

  # print("crossCol is ", end='')
  # print(crossCol(grid, 8))

  procThird(grid, inter_info)
  #---------------------------------------


  print(row1)
  print(row2)
  print(row3)
  print()

  return grid
  
#--------------------------------------- processing in main
rowsComp(grid)
az.prtSudoku(grid)
#---------------------------------------

#---------------------------------------------------------------------------------------

# need to:
# iterate thru target row block indices
# at each blank cell, generate the column of that cell to compare