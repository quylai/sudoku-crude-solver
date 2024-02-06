import numpy as np


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# GLOBAL CONSTANTS

LINES_SEQ = np.array([[0,1,2], [0,2,1], [1,2,0],
                      [3,4,5], [3,5,4], [4,5,3],
                      [6,7,8], [6,8,7], [7,8,6]])

BOX_VECTS = np.array([[0,3,0,3], [0,3,3,6], [0,3,6,9],
                      [3,6,0,3], [3,6,3,6], [3,6,6,9],
                      [6,9,0,3], [6,9,3,6], [6,9,6,9]])


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
      dummyRBE = rowBlocElement.copy()
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
      dummyCBE = colBlocElement.copy()
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
def coordBoxToGrid(boxNum, boxCoord):
  box0 = np.array([[(0,0), (0,1), (0,2)], 
                   [(1,0), (1,1), (1,2)], 
                   [(2,0), (2,1), (2,2)]])

  box1 = np.array([[(0,3), (0,4), (0,5)], 
                   [(1,3), (1,4), (1,5)], 
                   [(2,3), (2,4), (2,5)]])

  box2 = np.array([[(0,6), (0,7), (0,8)], 
                   [(1,6), (1,7), (1,8)], 
                   [(2,6), (2,7), (2,8)]])
  
  box3 = np.array([[(3,0), (3,1), (3,2)], 
                   [(4,0), (4,1), (4,2)], 
                   [(5,0), (5,1), (5,2)]])
  
  box4 = np.array([[(3,3), (3,4), (3,5)], 
                   [(4,3), (4,4), (4,5)], 
                   [(5,3), (5,4), (5,5)]])
  
  box5 = np.array([[(3,6), (3,7), (3,8)], 
                   [(4,6), (4,7), (4,8)], 
                   [(5,6), (5,7), (5,8)]])
  
  box6 = np.array([[(6,0), (6,1), (6,2)], 
                   [(7,0), (7,1), (7,2)], 
                   [(8,0), (8,1), (8,2)]])
  
  box7 = np.array([[(6,3), (6,4), (6,5)], 
                   [(7,3), (7,4), (7,5)], 
                   [(8,3), (8,4), (8,5)]])
  
  box8 = np.array([[(6,6), (6,7), (6,8)], 
                   [(7,6), (7,7), (7,8)], 
                   [(8,6), (8,7), (8,8)]])

  if (boxNum == 0):
    gridCoord = box0[boxCoord[0], boxCoord[1]]
  elif (boxNum == 1):
    gridCoord = box1[boxCoord[0], boxCoord[1]]
  elif (boxNum == 2):
    gridCoord = box2[boxCoord[0], boxCoord[1]]
  elif (boxNum == 3):
    gridCoord = box3[boxCoord[0], boxCoord[1]]
  elif (boxNum == 4):
    gridCoord = box4[boxCoord[0], boxCoord[1]]
  elif (boxNum == 5):
    gridCoord = box5[boxCoord[0], boxCoord[1]]
  elif (boxNum == 6):
    gridCoord = box6[boxCoord[0], boxCoord[1]]
  elif (boxNum == 7):
    gridCoord = box7[boxCoord[0], boxCoord[1]]
  elif (boxNum == 8):
    gridCoord = box8[boxCoord[0], boxCoord[1]]

  return gridCoord


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def boxSingCand(grid):

  for x in range(9):  # iterate thru boxes
    a = BOX_VECTS[x][0].copy()
    b = BOX_VECTS[x][1].copy()
    c = BOX_VECTS[x][2].copy()
    d = BOX_VECTS[x][3].copy()
    scanBox = grid[a:b, c:d]

    numInBox = 0
    for y in scanBox.flat:  # counting cells solved of current box
      if (y > 0):
        numInBox += 1
      if (numInBox == 4):                          
        break

    if (numInBox == 4):  # processing current box w/ 4>= cells solved

      possCand = np.array([1,2,3,4,5,6,7,8,9])

      # eliminating number already exist in box from possCand
      for a in scanBox.flat:
        if (a != 0):
          possCand[np.where(possCand == a)[0][0]] = 0

      # iterating cells of current viable box
      for zdx, z in np.ndenumerate(scanBox):
        dummyPC = possCand.copy()

        if (z == 0):
          gridCoord = coordBoxToGrid(x, zdx)

          row = grid[gridCoord[0],]
          col = grid[:, gridCoord[1]]

          # eliminating number already exist in row from possCand
          for b in row:
            if (b != 0 and np.where(dummyPC == b)[0].size != 0):
              dummyPC[np.where(dummyPC == b)[0][0]] = 0

          # eliminating number already exist in col from possCand
          for c in col:
            if (c != 0 and np.where(dummyPC == c)[0].size != 0):
              dummyPC[np.where(dummyPC == c)[0][0]] = 0

          # when sole non-zero exist in possible-candiate array
          if (np.nonzero(dummyPC)[0].size == 1):
            grid[gridCoord[0], gridCoord[1]] = dummyPC[np.nonzero(dummyPC)[0][0]]

  return grid 


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def arrBoxes(grid, line, rowsOrCols):
  arrOfBoxes = np.array([[]], dtype=int)  # initializing

  if (rowsOrCols == 'r'):

    if (line >= 0 and line < 3):
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 0:3].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 3:6].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 6:9].copy()).reshape(3,9)

    elif (line >= 3 and line < 6):
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 0:3].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 3:6].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 6:9].copy()).reshape(3,9)

    elif (line >= 6 and line < 9):
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 0:3].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 3:6].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 6:9].copy()).reshape(3,9)

  elif (rowsOrCols == 'c'):

    if (line >= 0 and line < 3):
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 0:3].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 0:3].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 0:3].copy()).reshape(3,9)

    elif (line >= 3 and line < 6):
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 3:6].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 3:6].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 3:6].copy()).reshape(3,9)

    elif (line >= 6 and line < 9):
      arrOfBoxes = np.append(arrOfBoxes, grid[0:3, 6:9].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[3:6, 6:9].copy())
      arrOfBoxes = np.append(arrOfBoxes, grid[6:9, 6:9].copy()).reshape(3,9)
    
  return arrOfBoxes


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def hSingCand(grid):

  for x in range(9):  # iterating thru rows
    scanRow = grid[x,]

    if (x == 0):
      arrOfBoxes = arrBoxes(grid, 0, 'r')
    elif (x == 3):
      arrOfBoxes = arrBoxes(grid, 3, 'r')
    elif (x == 6):
      arrOfBoxes = arrBoxes(grid, 6, 'r')

    lBox = arrOfBoxes[0]
    mBox = arrOfBoxes[1]
    rBox = arrOfBoxes[2]

    numInBox = 0
    for y in scanRow:  # counting cells solved of current row
      if (y > 0):
        numInBox += 1
      if (numInBox == 4):                          
        break

    if (numInBox == 4):  # processing current row w/ 4>= cells solved
      possCand = np.array([1,2,3,4,5,6,7,8,9])

      # eliminating number already exist in row from possCand
      for a in scanRow:
        if (a != 0):
          possCand[np.where(possCand == a)[0][0]] = 0

      # iterating cells of current viable row
      for zdx, z in np.ndenumerate(scanRow):
        dummyPC = possCand.copy()

        if (z == 0):
          col = grid[:, zdx[0]]

          # eliminating number already exist in col from possCand
          for b in col:
            if (b != 0 and np.where(dummyPC == b)[0].size != 0):
              dummyPC[np.where(dummyPC == b)[0][0]] = 0

          # eliminating number already exist in left-box from possCand
          if (zdx[0] >= 0 and zdx[0] < 3):
            for c in lBox:
              if (c != 0 and np.where(dummyPC == c)[0].size != 0):
                dummyPC[np.where(dummyPC == c)[0][0]] = 0

          # eliminating number already exist in mid-box from possCand
          elif (zdx[0] >= 3 and zdx[0] < 6):
            for d in mBox:
              if (d != 0 and np.where(dummyPC == d)[0].size != 0):
                dummyPC[np.where(dummyPC == d)[0][0]] = 0

          # eliminating number already exist in right-box from possCand
          elif (zdx[0] >= 6 and zdx[0] < 9):
            for e in rBox:
              if (e != 0 and np.where(dummyPC == e)[0].size != 0):
                dummyPC[np.where(dummyPC == e)[0][0]] = 0

          # when sole non-zero exist in possible-candiate array
          if (np.nonzero(dummyPC)[0].size == 1):
            grid[x, zdx[0]] = dummyPC[np.nonzero(dummyPC)[0][0]]

  return grid 


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def vSingCand(grid):

  for x in range(9):  # iterating thru cols
    scanCol = grid[:, x]

    if (x == 0):
      arrOfBoxes = arrBoxes(grid, 0, 'c')
    elif (x == 3):
      arrOfBoxes = arrBoxes(grid, 3, 'c')
    elif (x == 6):
      arrOfBoxes = arrBoxes(grid, 6, 'c')

    tBox = arrOfBoxes[0]
    mBox = arrOfBoxes[1]
    bBox = arrOfBoxes[2]

    numInBox = 0
    for y in scanCol:  # counting cells solved of current col
      if (y > 0):
        numInBox += 1
      if (numInBox == 4):                          
        break

    if (numInBox == 4):  # processing current col w/ 4>= cells solved
      possCand = np.array([1,2,3,4,5,6,7,8,9])

      # eliminating number already exist in col from possCand
      for a in scanCol:
        if (a != 0):
          possCand[np.where(possCand == a)[0][0]] = 0

      # iterating cells of current viable col
      for zdx, z in np.ndenumerate(scanCol):
        dummyPC = possCand.copy()

        if (z == 0): # @ empty cell in scanCol
          row = grid[zdx[0],]

          # eliminating number already exist in row from possCand
          for b in row:
            if (b != 0 and np.where(dummyPC == b)[0].size != 0):
              dummyPC[np.where(dummyPC == b)[0][0]] = 0

          # eliminating number already exist in top-box from possCand
          if (zdx[0] >= 0 and zdx[0] < 3):
            for c in tBox:
              if (c != 0 and np.where(dummyPC == c)[0].size != 0):
                dummyPC[np.where(dummyPC == c)[0][0]] = 0

          # eliminating number already exist in mid-box from possCand
          elif (zdx[0] >= 3 and zdx[0] < 6):
            for d in mBox:
              if (d != 0 and np.where(dummyPC == d)[0].size != 0):
                dummyPC[np.where(dummyPC == d)[0][0]] = 0

          # eliminating number already exist in bottom-box from possCand
          elif (zdx[0] >= 6 and zdx[0] < 9):
            for e in bBox:
              if (e != 0 and np.where(dummyPC == e)[0].size != 0):
                dummyPC[np.where(dummyPC == e)[0][0]] = 0

          # when sole non-zero exist in possible-candiate array
          if (np.nonzero(dummyPC)[0].size == 1):
            grid[zdx[0], x] = dummyPC[np.nonzero(dummyPC)[0][0]]

  return grid


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def nCount(grid):  # counting all cells filled in grid
  count = 0
  for x in grid:
    for y in x:
      if (y == 0):
        count += 1

  return 81-count


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def analyzeSeqs(grid, *seqsOfStr):

  for aSeq in seqsOfStr:
    gridProc = grid.copy()
    gridInitNums = nCount(gridProc)

    for x in aSeq:
      if (x == 'r'):
        gridProc = rowsComp(gridProc)
      elif (x == 'c'):
        gridProc = colsComp(gridProc)
      elif (x == 'b'):
        gridProc = boxSingCand(gridProc)
      elif (x == 'h'):
        gridProc = hSingCand(gridProc)
      elif (x == 'v'):
        gridProc = vSingCand(gridProc)

    print("initially: " + str(gridInitNums) + "; ran sequence " + aSeq + ", now " + 
          str(nCount(gridProc)) +"; solved " + str(nCount(gridProc)-gridInitNums))
    
    prtSudoku(gridProc)  # do not delete, needed for troubleshooting

    




