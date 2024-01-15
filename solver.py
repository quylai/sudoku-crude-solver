import numpy as np

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list("......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57.".translate({46: 48}))

# for visual
#
# ......43.
# ..52..8.7
# .8.7.....

# .3..48.5.
# .4.6....2
# .9..52.4.

# .6.4.....
# ..19..6.3
# ......57.

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


# notes annotated are based from written hard code, see notes:
# "prtSudoku hardcode"
def prtSudoku(grid):
  oneline_sudoku = grid.flatten()

  for idx, x in np.ndenumerate(oneline_sudoku):

    if idx[0] == 0:
      print("-------------------")
    
    if idx[0] % 9 == 0:
      print('|', end='')                                        # for "b|"

    # swap out zero with ' '
    if (x == 0):
      print(' ', end='')
    else:                                                   
      print(x, end='')                                          # for 'x'

    if idx[0] < 27:
      if (idx[0] + 1) % 9 == 0:                                 # for "|e"
        print('|')
      elif (idx[0] - 2) % 3 == 0 and (idx[0] + 1) % 9 != 0:     # for '|'
        print('|', end='')
      elif (idx[0] % 3 == 0 or idx[0] % 3 == 1):                # for 's'
        print(' ', end='')

 



  # print("-------------------")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("-------------------")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("-------------------")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("|     |     |     |")
  # print("-------------------")



prtSudoku(grid)

