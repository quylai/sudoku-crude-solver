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

a1 to i1   :	rowTopTop		rtt
a2 to i2   :	rowTopCenter		rtc
a3 to i3   :	rowTopBottom		rtb
a6 to i6   :	rowMiddleBottom		rmb
a9 to i9   :	rowBottomBottom		rbb




----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
Methodologies


----------------------------------------
Rows comparison

------------------
Top segment

- compare row1 and row2 for intersection values

- of those intersected values, choose one (inter_val)
  locate the row block in which inter_val is absent on row3

- on row3, determine which of it row block absent of inter_val
  - if only 1 cell of row block vaccant, then
    cell = inter_val
  - else, use cross-column at those vacant cell to see if inter_val can be checkoff

- evaluate next inter_val









----------------------------------------
crosshair
.
checking if number exist on row/column of current element


----------------------------------------
same # exist in 2/3 box
.
get tl to intersect with tm;
save the index of intersection;
manipulate tr



----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------














