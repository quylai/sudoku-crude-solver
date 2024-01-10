

# initial sudoku format is oneline, rows from top-bottom, connected tail-to-head
# .
# modify string using ascii codes to replace 46 (.) with 48 (0), then typecast it into a list of characters
inputs = list("......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57.".translate({46: 48}))

# convert elements of var "inputs" into List of in
inputs = [eval(i) for i in inputs]

# Rows notation: rowTopTop (rtt), rowTopCenter (rtc),
# rowTopBottom (rtb), rowMiddleBottom (rmb), and rowBottomBottom (rbb)
grid = {
  "rtt": [0,0,0,0,0,0,0,0,0],
  "rtc": [0,0,0,0,0,0,0,0,0],
  "rtb": [0,0,0,0,0,0,0,0,0],
  "rmt": [0,0,0,0,0,0,0,0,0],
  "rmc": [0,0,0,0,0,0,0,0,0],
  "rmb": [0,0,0,0,0,0,0,0,0],
  "rbt": [0,0,0,0,0,0,0,0,0],
  "rbc": [0,0,0,0,0,0,0,0,0],
  "rbb": [0,0,0,0,0,0,0,0,0]
}

# updating initial sudoku state onto grid
n = 0
for k, l in grid.items():
  grid[k] = inputs[n:n+len(l)]
  n += len(l)

print(grid)


