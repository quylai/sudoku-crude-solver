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
1|     |     |     |
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

similarly apply to "Col Block"


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
----------------------------------------
Cols comparison

- apply same process as rows-comparison, but use columns instead


----------------------------------------
----------------------------------------
Single candidates (boxSingCand)

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

(h4) will also be solved with '4', after (b4) solved;
this was noticed after the creation of function boxSingCand

Summary:
iterate thru cells of each boxes; eliminating # that ready existed in box/row/col; assign to cell the last possible candidate remained


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
Horizontal single candidates

iterate thru cells of each "rows"; eliminating # that ready existed in row/col/box; assign to cell the last possible candidate remained

test case 1:
9....51.6...3...7.....46......8.......................74...3........769.39621..54

   a b c d e f g h i
  -------------------
1 |9    |    5|1   6|
2 |     |3    |  7  |
3 |     |  4 6|     |
  -------------------
4 |     |8    |     |
5 |     |     |     |
6 |     |     |     |
  -------------------
7 |7 4  |    3|     |
8 |     |    7|6 9  |
9 |3 9 6|2 1  |  5 4|
  -------------------

d1 = 7;  f9 = 8

 9 8 3 | 7 2 5 | 1 4 6
 6 1 4 | 3 8 9 | 5 7 2
 2 5 7 | 1 4 6 | 3 8 9
-------|-------|-------
 1 3 9 | 8 7 4 | 2 6 5
 5 6 8 | 9 3 2 | 4 1 7
 4 7 2 | 5 6 1 | 9 3 8
-------|-------|-------
 7 4 5 | 6 9 3 | 8 2 1
 8 2 1 | 4 5 7 | 6 9 3
 3 9 6 | 2 1 8 | 7 5 4

----------------------------------------

test case 2:
..6.7...8.....5.7..7...14.57.9.4.6....4...5..3.5.8.2...6...87.2.....3.4...2.5...9

   a b c d e f g h i
  -------------------
1 |    6|  7  |    8|
2 |     |    5|  7  |
3 |  7  |    1|4   5|
  -------------------
4 |7   9|  4  |6    |
5 |    4|     |5    |
6 |3   5|  8  |2    |
  -------------------
7 |  6  |    8|7   2|
8 |     |    3|  4  |
9 |    2|  5  |    9|
  -------------------

f4 = 2;  b6 = 1  

 2 5 6 | 9 7 4 | 1 3 8
 4 3 1 | 8 2 5 | 9 7 6
 9 7 8 | 6 3 1 | 4 2 5
-------|-------|-------
 7 8 9 | 5 4 2 | 6 1 3
 6 2 4 | 3 1 9 | 5 8 7
 3 1 5 | 7 8 6 | 2 9 4
-------|-------|-------
 1 6 3 | 4 9 8 | 7 5 2
 5 9 7 | 2 6 3 | 8 4 1
 8 4 2 | 1 5 7 | 3 6 9

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
Vertical single candidates

iterate thru cells of each "cols"; eliminating # that ready existed in col/row/box; assign to cell the last possible candidate remained

test case 1:
...1.........82.......7..9......6......8........9........6.3......7.........54...

   a b c d e f g h i
  -------------------
1 |     |1    |     |
2 |     |  8 2|     |
3 |     |  7  |  9  |
  -------------------
4 |     |    6|     |
5 |     |8    |     |
6 |     |9    |     |
  -------------------
7 |     |6   3|     |
8 |     |7    |     |
9 |     |  5 4|     |
  -------------------
  
d9 = 2;  f3 = 5  

 3 4 8 | 1 6 9 | 5 7 2
 5 7 9 | 4 8 2 | 6 1 3
 1 6 2 | 3 7 5 | 8 9 4
-------|-------|-------
 2 3 1 | 5 4 6 | 9 8 7
 4 9 6 | 8 2 7 | 3 5 1
 8 5 7 | 9 3 1 | 2 4 6
-------|-------|-------
 7 8 4 | 6 9 3 | 1 2 5
 6 2 5 | 7 1 8 | 4 3 9
 9 1 3 | 2 5 4 | 7 6 8

----------------------------------------

test case 2:


