
I make way too many mistakes when I work on puzzles like sudoku. Well, I understand the process well enough to write a program that solves at least some. ssolve.py will solve at least some of the easiest puzzles I've tested it against.

I also wanted to mess with pygame a bit more, so I used it to display the screen

$ python sudoku.py

will run the program. you can click on squares and enter numbers. clicking start will start the solve process.

you can also run

$ python sudoku.py F file

where file contains text that looks like:

060075004
020004900
401003027
502008036
049000270
130700408
650100309
007500040
200340050

O's represent squares that are blank. the program will display the puzzle and when you click start, try to solve it.
