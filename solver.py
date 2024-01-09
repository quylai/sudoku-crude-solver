

# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list("......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57.".translate({46: 48}))

# convert elements of var "inputs" into List of in
inputs = [eval(i) for i in inputs]

# Blocks notation: topLeft (tl), middleLeft (ml),
# bottomLeft (bl), bottomCenter (bc), and bottomRight (br)
grid = {
  "tl": [0,0,0,0,0,0,0,0,0],
  "tc": [1,1,1,1,1,1,1,1,1],
  "tr": [0,0,0,0,0,0,0,0,0],
  "ml": [0,0,0,0,0,0,0,0,0],
  "mc": [0,0,0,0,0,0,0,0,0],
  "mr": [0,0,0,0,0,0,0,0,0],
  "bl": [0,0,0,0,0,0,0,0,0],
  "bc": [9,8,7,6,5,4,3,2,1],
  "br": [1,2,3,4,5,6,7,8,9]
}

# updating initial sudoku state onto grid
n = 0
for k, l in grid.items():
  grid[k] = inputs[n:n+len(l)]
  n += len(l)

print(grid)


