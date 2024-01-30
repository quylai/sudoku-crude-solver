----------------------------------------------------------------------------------------
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
         1         2         3         4         5         6         7         8
----------------------------------------
------------------
123456789012345678
------------------
----------------------------------------
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------


----------------------------------------
Obtaining sudoku from
.
https://qqwing.com/generate.html
sample of sudoku outputted format
......43...52..8.7.8.7......3..48.5..4.6....2.9..52.4..6.4.......19..6.3......57. 


----------------------------------------
Labeling

  a b c d e f g h i
 -------------------
1|* * *|     |     |
2|     |     |     |
3|     |     |     |
 -------------------
4|     |     |     |
5|     |     |     |
6|     |     |     |
 -------------------
7|     |     |     |
8|     |     |     |
9|     |     |     |
 -------------------


------------------
Cells

any single space in sudoku grid


------------------
Row Block

part of a row that is segmented by the block
e.g. [a1 to c1] or [d5 to f5] ...


------------------
Rows

a1 to i1
 .     . 
 .     . 
 .     . 
a9 to i9


------------------
Cols

a1 to a9
.     . 
.     . 
.     . 
i9 to i9


------------------
Boxes

a1 to c3  or  d1 to f3  or  g1 to i3
a4 to c6  or  d4 to f6  or  g4 to i6
a7 to c9  or  d7 to f9  or  g7 to i9

  a b c d e f g h i
 -------------------
1|     |     |     |
2|  0  |  1  |  2  |
3|     |     |     |
 -------------------
4|     |     |     |
5|  3  |  4  |  5  |
6|     |     |     |
 -------------------
7|     |     |     |
8|  6  |  7  |  8  |
9|     |     |     |
 -------------------



----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
Methodologies

----------------------------------------
Rows comparison

- compare row1 and row2 for intersection values

- of those intersected values, choose one (inter_val)
  locate the row block in which inter_val is absent on row3

- on row3, determine which of it row block absent of inter_val
  - if only 1 cell of row block vaccant, then
    cell = inter_val
  - else, use cross-column at those vacant cell to see if inter_val can be checkoff

- evaluate next inter_val


----------------------------------------
Cols comparison

- apply same process as rows-comparison, but use columns instead


----------------------------------------
Single candidates

refer to site below, at section "Searching for Single Candidates"
https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques

given initial sudoku:

   a b c d e f g h i
  -------------------
1 |     |1   4|     |
2 |    1|     |9    |
3 |  9  |7   3|  6  |
  -------------------
4 |8   7|     |1   6|
5 |     |     |     |
6 |3   4|     |5   9|
  -------------------
7 |  5  |4   2|  3  |
8 |    8|     |6    |
9 |     |8   6|     |
  -------------------

"...1.4.....1...9...9.7.3.6.8.7...1.6.........3.4...5.9.5.4.2.3...8...6.....8.6..."

observe at (b4); after eliminate all those from box, row, and col;
(b4) is left with numerical '2'


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------














