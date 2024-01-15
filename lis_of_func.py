import numpy as np


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
