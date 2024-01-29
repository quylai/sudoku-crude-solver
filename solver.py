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
              ".86....9."
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
az.prtSudoku(grid)  ##


def colsComp(grid):

  def procThirdCol(grid, info, curColsSeq):
    # info[0] is intersected values array
    # info[1] is intersected coordinates array
    print("------------------")
    print(info[0])
    print(info[1])

    for idx, i in np.ndenumerate(info[0]):  # in intersected values
      colBlocOccupy = np.array([0,0,0])  # flags

      for j in info[1][idx]:  # in intersected coord
        for k in range(9):  # flagging colBloc existed targeted number
          if (j == k):
            if (k in range(0,3)):
              colBlocOccupy[0] = 1
            elif (k in range(3,6)):
              colBlocOccupy[1] = 1
            elif (k in range(6,9)):
              colBlocOccupy[2] = 1
      
      # assigning indices to targeted col block
      for xdx, x in np.ndenumerate(colBlocOccupy):
        if (x == 0):
          if (xdx[0] == 0):
            tarColBlocInd = np.array([0,1,2])
          elif (xdx[0] == 1):
            tarColBlocInd = np.array([3,4,5])
          elif (xdx[0] == 2):
            tarColBlocInd = np.array([6,7,8])

      colBlocElement = np.array([8,8,8])  # initializing
      # initial iteration thru target col block indices
      # to note which element is vacant; 1=occupied 0=vacant
      for ydx, y in np.ndenumerate(tarColBlocInd):
        if (grid[y:y+1, curColsSeq[2]] == 0):
          colBlocElement[ydx[0]] = 0
        else:
          colBlocElement[ydx[0]] = 1

      # when 2_or_3 vacant occurred in colBlocElement 
      dummyCBE = colBlocElement
      if (np.where(dummyCBE == 0)[0].size >= 2):
        for z in np.where(dummyCBE == 0)[0]:
          dummyRow = grid[tarColBlocInd[z],]
          for a in dummyRow:
            if (a == i):
              colBlocElement[z] = 1

      # when single vacant occurred in colBlocElement 
      if (np.where(colBlocElement == 0)[0].size == 1):
        grid[tarColBlocInd[np.where(colBlocElement == 0)[0][0]], curColsSeq[2]] = i


      print(colBlocElement)  ##




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
az.prtSudoku(grid)
#--------------------------------------- ends processing in main

#---------------------------------------------------------------------------------------
