

# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list("......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57.".translate({46: 48}))

# convert elements of var "inputs" into List of in
inputs = [eval(i) for i in inputs]



grid = {
  "tl": [0,0,0,0,0,0,0,0,0],
  "tc": [0,0,0,0,0,0,0,0,0],
  "tr": [0,0,0,0,0,0,0,0,0],
  "ml": [0,0,0,0,0,0,0,0,0],
  "mc": [0,0,0,0,0,0,0,0,0],
  "mr": [0,0,0,0,0,0,0,0,0],
  "bl": [0,0,0,0,0,0,0,0,0],
  "bc": [0,0,0,0,0,0,0,0,0],
  "br": [1,2,3,4,5,6,7,8,9]
}

# for key in grid:
#   print(key, "->", grid[key])

# print(grid["tl"])
# print(len(grid["tl"]))
# print(type(grid["tl"]))

# for blockz, elementz in grid.items():
#   grid[blockz] = [1,2,3,4,5,6,7,8,9]
# print(grid)

# for blockz, elementz in grid.items():
#   grid[blockz] = elementz[8]
# print(grid)

# zeroing = {}

# ascii codes to replace 46 (.) with 48 (0)
# print(inputs.translate({46: 48}))

print(inputs)