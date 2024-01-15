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
  - else, inclusive

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
prtSudoku hardcode

i=0
	print("-------------------")

	print('|', end='')		b|

	print(x, end='')		x
	print(' ', end='')		s
i=1
	print(x, end='')		x
	print(' ', end='')		s
i=2
	print(x, end='')		x
	print('|', end='')		|
i=3
	print(x, end='')		x
	print(' ', end='')		s
i=4
	print(x, end='')		x
	print(' ', end='')		s
i=5
	print(x, end='')		x
	print('|', end='')		|
i=6
	print(x, end='')		x
	print(' ', end='')		s
i=7
	print(x, end='')		x
	print(' ', end='')		s
i=8
	print(x, end='')		x
	print('|')			|e
i=9
	print('|', end='')		b|

	print(x, end='')		x
	print(' ', end='')		s
i=10
	print(x, end='')		x
	print(' ', end='')		s
i=11
	print(x, end='')		x
	print('|', end='')		|
i=12
	print(x, end='')		x
	print(' ', end='')		s
i=13
	print(x, end='')		x
	print(' ', end='')		s
i=14
	print(x, end='')		x
	print('|', end='')		|
i=15
	print(x, end='')		x
	print(' ', end='')		s
i=16
	print(x, end='')		x
	print(' ', end='')		s
i=17
	print(x, end='')		x
	print('|')			|e
i=18
	print('|', end='')		b|

	print(x, end='')		x
	print(' ', end='')		s
i=19
	print(x, end='')		x
	print(' ', end='')		s
i=20
	print(x, end='')		x
	print('|', end='')		|
i=21
	print(x, end='')		x
	print(' ', end='')		s
i=22
	print(x, end='')		x
	print(' ', end='')		s
i=23
	print(x, end='')		x
	print('|', end='')		|
i=24
	print(x, end='')		x
	print(' ', end='')		s
i=25
	print(x, end='')		x
	print(' ', end='')		s
i=26
	print(x, end='')		x
	print('|')			|e


#-----------------
Above are hardcode of function "prtSudoku" from indices 0 to 26.  Annotation are as followed:
{b|}	row beginning bar
{x}	cell value
{|e}	row ending bar
{|}	between cells bar
{s}	space between cells


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------














