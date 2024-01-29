import numpy as np


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# GLOBAL CONSTANTS

LINES_SEQ = np.array([
                    [0,1,2], [0,2,1], [1,2,0],
                    [3,4,5], [3,5,4], [4,5,3],
                    [6,7,8], [6,8,7], [7,8,6]
])


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# notes annotated are based from written hard code, see notes:
# "prtSudoku hardcode"
# function: to print sudoku onto cmd line
def prtSudoku(grid):
  oneline_sudoku = grid.flatten()

  for idx, x in np.ndenumerate(oneline_sudoku):

    if idx[0] == 0 or idx[0] == 27 or idx[0] == 54:
      print("-------------------")
    
    if idx[0] % 9 == 0:
      print('|', end='')                                        # for "b|"

    # swap out zero with ' '
    if (x == 0):
      print(' ', end='')
    else:                                                   
      print(x, end='')                                          # for 'x'

    # fork for:
    # row ending bar or between cells bar or space between cells
    if (idx[0] + 1) % 9 == 0:                                   # for "|e"
      print('|')
    elif (idx[0] - 2) % 3 == 0 and (idx[0] + 1) % 9 != 0:       # for '|'
      print('|', end='')
    elif (idx[0] % 3 == 0 or idx[0] % 3 == 1):                  # for 's'
      print(' ', end='')

    # bottom grid border
    if (idx[0] == 80):
      print("-------------------")


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def find_inter_coord(grid, linesSeq, rowsOrCols):

  if (rowsOrCols == 'r'):
    arrA = grid[linesSeq[0],]
    arrB = grid[linesSeq[1],]
    arrC = grid[linesSeq[2],]
  elif (rowsOrCols == 'c'):
    arrA = grid[:, linesSeq[0]]
    arrB = grid[:, linesSeq[1]]
    arrC = grid[:, linesSeq[2]]

  # getting all value that are intersected, between arrA & arrB
  inter_val = np.intersect1d(arrA, arrB, assume_unique=False)
  interWithArrC = np.intersect1d(inter_val, arrC, assume_unique=False)

  # turn all value of inter_val that matched with interWithArrC, equal 0
  for idx, i in np.ndenumerate(inter_val):
    for j in interWithArrC:
      if (i == j):
        inter_val[idx[0]] = 0

  # deleting all element with value of 0, in array inter_val
  inter_val = np.sort(inter_val)
  while (np.where(inter_val == 0)[0].size != 0):
    temp = inter_val
    inter_val = np.delete(temp, [0])

  inter_val_coord = np.array([], dtype=int)  # initializing array
  for xdx, x in np.ndenumerate(inter_val):

    i = np.where(arrA == x)[0]
    j = np.where(arrB == x)[0]

    # append intersected indices from arrA & arrB
    inter_val_coord = np.append(inter_val_coord, [i, j]).reshape(xdx[0]+1, 2)

  return inter_val, inter_val_coord


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def rowsComp(grid):

  def procThirdRow(grid, info, curRowsSeq):
    # info[0] is intersected values array
    # info[1] is intersected coordinates array

    for idx, i in np.ndenumerate(info[0]):  # in intersected values
      rowBlocOccupy = np.array([0,0,0])  # flags

      for j in info[1][idx]:  # in intersected coord
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
            tarRowBlocInd = np.array([0,1,2])
          elif (xdx[0] == 1):
            tarRowBlocInd = np.array([3,4,5])
          elif (xdx[0] == 2):
            tarRowBlocInd = np.array([6,7,8])

      rowBlocElement = np.array([8,8,8])  # initializing
      # initial iteration thru target row block indices
      # to note which element is vacant; 1=occupied 0=vacant
      for ydx, y in np.ndenumerate(tarRowBlocInd):
        if (grid[curRowsSeq[2]][y] == 0):
          rowBlocElement[ydx[0]] = 0
        else:
          rowBlocElement[ydx[0]] = 1
      
      # when 2_or_3 vacant occurred in rowBlocElement 
      dummyRBE = rowBlocElement
      if (np.where(dummyRBE == 0)[0].size >= 2):
        for z in np.where(dummyRBE == 0)[0]:
          dummyCol = grid[:, tarRowBlocInd[z]]
          for a in dummyCol:
            if (a == i):
              rowBlocElement[z] = 1
            
      # when single vacant occurred in rowBlocElement 
      if (np.where(rowBlocElement == 0)[0].size == 1):
        grid[curRowsSeq[2], tarRowBlocInd[np.where(rowBlocElement == 0)[0][0]]] = i

    return grid

  #--------------------------------------- begins processing in rowsComp
  for i in LINES_SEQ:
    inter_info = find_inter_coord(grid, i, 'r')
    procThirdRow(grid, inter_info, i)
  #--------------------------------------- ends processing in rowsComp

  return grid


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def colsComp(grid):

  def procThirdCol(grid, info, curColsSeq):
    # info[0] is intersected values array
    # info[1] is intersected coordinates array

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

    return grid

  #--------------------------------------- begins processing in colsComp
  for i in LINES_SEQ:
    inter_info = find_inter_coord(grid, i, 'c')
    procThirdCol(grid, inter_info, i)
  #--------------------------------------- ends processing in colsComp
  
  return grid


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def nCount(grid):  # counting all cells filled
  count = 0
  for x in grid:
    for y in x:
      if (y == 0):
        count += 1

  return 81-count
