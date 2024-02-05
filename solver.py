import numpy as np
import lis_of_func as az

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list(
"...1.4.....1...9...9.7.3.6.8.7...1.6.........3.4...5.9.5.4.2.3...8...6.....8.6..."
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
#### 6# w/ rrrr; 4# w/ cccc; 15# w/ rcrcrcrc
# "...9.3.....38274...2.....8.26.4.1.79.7.....5.13.5.2.64.8.....9...41692.....7.8..."
#### 7# w/ rrrr; 7# w/ cccc; 19# w/ rcrcrcrc

# "...1.4.....1...9...9.7.3.6.8.7...1.6.........3.4...5.9.5.4.2.3...8...6.....8.6..."
#### 2# w/ rrrr; 0# w/ cccc; 2# w/ rcrcrcrc; test case for single-candidates

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
# az.prtSudoku(grid)  ##

def singCand(grid):

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

  boxVects = np.array([

                       [0,3,0,3], [0,3,3,6], [0,3,6,9],
                       [3,6,0,3], [3,6,3,6], [3,6,6,9],
                       [6,9,0,3], [6,9,3,6], [6,9,6,9]])


  # box0 is grid[0:3, 0:3]
  # box4 is grid[3:6, 3:6]


  for x in range(9):  # iterate thru boxes
    a = boxVects[x][0].copy()
    b = boxVects[x][1].copy()
    c = boxVects[x][2].copy()
    d = boxVects[x][3].copy()
    scanBox = grid[a:b, c:d]

    numInBox = 0
    for y in scanBox.flat:  # counting cells solved of current box
      if (y > 0):
        numInBox += 1
      if (numInBox == 4):                          
        break

    if (numInBox == 4):  # processing current box w/ 4>= cells solved
      print(scanBox)  ##

      possCand = np.array([1,2,3,4,5,6,7,8,9])


      # eliminating number already exist in box from possCand
      for a in scanBox.flat:
        if (a != 0):
          possCand[np.where(possCand == a)[0][0]] = 0


      # iterating cells of current viable box
      for zdx, z in np.ndenumerate(scanBox):
        if (z == 0):
          gridCoord = coordBoxToGrid(x, zdx)

          print(gridCoord)  ##






  return grid  # return from singCand

  




















  # az.prtSudoku(grid)

#--------------------------------------- begins processing in main

testSingCand = singCand(grid)

# az.analyzeSeqs(grid, "rrrr", "cccc", "rcrcrcrc")

# print("----------------------------------------")  ##
# az.prtSudoku(grid)  ##

#--------------------------------------- ends processing in main

#---------------------------------------------------------------------------------------
# git commit -m
# 
# 
# 
#---------------------------------------------------------------------------------------


