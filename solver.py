

# initial sudoku format is one, row from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list("......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57.".translate({46: 48}))

# convert elements of var "inputs" into List of in
inputs = [eval(i) for i in inputs]

# Rows notation: topTop (tt), topCenter (tc),
# topBottom (tb), middleBottom (mb), and bottomBottom (bb)
grid = {
  "tt": [0,0,0,0,0,0,0,0,0],
  "tc": [0,0,0,0,0,0,0,0,0],
  "tb": [0,0,0,0,0,0,0,0,0],
  "mt": [0,0,0,0,0,0,0,0,0],
  "mc": [0,0,0,0,0,0,0,0,0],
  "mb": [0,0,0,0,0,0,0,0,0],
  "bt": [0,0,0,0,0,0,0,0,0],
  "bc": [0,0,0,0,0,0,0,0,0],
  "bb": [0,0,0,0,0,0,0,0,0]
}

# updating initial sudoku state onto grid
n = 0
for k, l in grid.items():
  grid[k] = inputs[n:n+len(l)]
  n += len(l)

print(grid)


