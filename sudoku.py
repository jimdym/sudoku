#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pStart.py
#  
#  Copyright 2022  <jimduba@duba.org>
#
#	If you use this program or pieces of it or if you find anything wrong
#  with it, please, let me know at the above email address.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import pygame
from pygame.locals import *
import sys
import pygame_widgets
from pygame_widgets.button import Button


# colors
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255) # not very visible against black
BLACK = (0, 0, 0)

#size of the screen
HEIGHT = 800  # enough space for a button
WIDTH = 600
CELL_SIZE = 54
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
button = Button(
    WIN, 200, 700, 50, 25, text='START',
    fontSize=20, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: sPuzzle()
)

pygame.display.set_caption("SUDOKU")
pygame.font.init()
pFont = pygame.font.Font(pygame.font.get_default_font(), 40)

# the grid is a dictionary containing an index (cell number) and a cell value
# which is a string 0-9 where 0 will be a blank square when the user sees it.

# in this pass I want the value to become a list cosisting of
# [v,[r,c,s],[1,2,3,4,5,6,7,8,9]] where v is the actual value the cell contains,
# [r,c,s] represents the row, column, and square the cell belongs to, and
# [1,2,3,...] is the list of possible values the celll could take on.

def initGrid():
	m={}
	m[1]=['0',[0,0,0],['1','2','3','4','5','6','7','8','9']]
	m[2]=['0',[0,1,0],['1','2','3','4','5','6','7','8','9']]
	m[3]=['0',[0,2,0],['1','2','3','4','5','6','7','8','9']]	
	m[4]=['0',[0,3,1],['1','2','3','4','5','6','7','8','9']]
	m[5]=['0',[0,4,1],['1','2','3','4','5','6','7','8','9']]
	m[6]=['0',[0,5,1],['1','2','3','4','5','6','7','8','9']]	
	m[7]=['0',[0,6,2],['1','2','3','4','5','6','7','8','9']]
	m[8]=['0',[0,7,2],['1','2','3','4','5','6','7','8','9']]
	m[9]=['0',[0,8,2],['1','2','3','4','5','6','7','8','9']]
	
	m[10]=['0',[1,0,0],['1','2','3','4','5','6','7','8','9']]
	m[11]=['0',[1,1,0],['1','2','3','4','5','6','7','8','9']]
	m[12]=['0',[1,2,0],['1','2','3','4','5','6','7','8','9']]
	
	m[13]=['0',[1,3,1],['1','2','3','4','5','6','7','8','9']]
	m[14]=['0',[1,4,1],['1','2','3','4','5','6','7','8','9']]
	m[15]=['0',[1,5,1],['1','2','3','4','5','6','7','8','9']]
	
	m[16]=['0',[1,6,2],['1','2','3','4','5','6','7','8','9']]
	m[17]=['0',[1,7,2],['1','2','3','4','5','6','7','8','9']]
	m[18]=['0',[1,8,2],['1','2','3','4','5','6','7','8','9']]
	
	m[19]=['0',[2,0,0],['1','2','3','4','5','6','7','8','9']]
	m[20]=['0',[2,1,0],['1','2','3','4','5','6','7','8','9']]
	m[21]=['0',[2,2,0],['1','2','3','4','5','6','7','8','9']]
	
	m[22]=['0',[2,3,1],['1','2','3','4','5','6','7','8','9']]
	m[23]=['0',[2,4,1],['1','2','3','4','5','6','7','8','9']]
	m[24]=['0',[2,5,1],['1','2','3','4','5','6','7','8','9']]
	
	m[25]=['0',[2,6,2],['1','2','3','4','5','6','7','8','9']]
	m[26]=['0',[2,7,2],['1','2','3','4','5','6','7','8','9']]
	m[27]=['0',[2,8,2],['1','2','3','4','5','6','7','8','9']]
	
	m[28]=['0',[3,0,3],['1','2','3','4','5','6','7','8','9']]
	m[29]=['0',[3,1,3],['1','2','3','4','5','6','7','8','9']]
	m[30]=['0',[3,2,3],['1','2','3','4','5','6','7','8','9']]
	
	m[31]=['0',[3,3,4],['1','2','3','4','5','6','7','8','9']]
	m[32]=['0',[3,4,4],['1','2','3','4','5','6','7','8','9']]
	m[33]=['0',[3,5,4],['1','2','3','4','5','6','7','8','9']]
	
	m[34]=['0',[3,6,5],['1','2','3','4','5','6','7','8','9']]
	m[35]=['0',[3,7,5],['1','2','3','4','5','6','7','8','9']]
	m[36]=['0',[3,8,5],['1','2','3','4','5','6','7','8','9']]
	
	m[37]=['0',[4,0,3],['1','2','3','4','5','6','7','8','9']]
	m[38]=['0',[4,1,3],['1','2','3','4','5','6','7','8','9']]
	m[39]=['0',[4,2,3],['1','2','3','4','5','6','7','8','9']]
	
	m[40]=['0',[4,3,4],['1','2','3','4','5','6','7','8','9']]
	m[41]=['0',[4,4,4],['1','2','3','4','5','6','7','8','9']]
	m[42]=['0',[4,5,4],['1','2','3','4','5','6','7','8','9']]
	
	m[43]=['0',[4,6,5],['1','2','3','4','5','6','7','8','9']]
	m[44]=['0',[4,7,5],['1','2','3','4','5','6','7','8','9']]
	m[45]=['0',[4,8,5],['1','2','3','4','5','6','7','8','9']]
	
	m[46]=['0',[5,0,3],['1','2','3','4','5','6','7','8','9']]
	m[47]=['0',[5,1,3],['1','2','3','4','5','6','7','8','9']]
	m[48]=['0',[5,2,3],['1','2','3','4','5','6','7','8','9']]
	
	m[49]=['0',[5,3,4],['1','2','3','4','5','6','7','8','9']]
	m[50]=['0',[5,4,4],['1','2','3','4','5','6','7','8','9']]
	m[51]=['0',[5,5,4],['1','2','3','4','5','6','7','8','9']]

	m[52]=['0',[5,6,5],['1','2','3','4','5','6','7','8','9']]
	m[53]=['0',[5,7,5],['1','2','3','4','5','6','7','8','9']]
	m[54]=['0',[5,8,5],['1','2','3','4','5','6','7','8','9']]
	
	m[55]=['0',[6,0,6],['1','2','3','4','5','6','7','8','9']]
	m[56]=['0',[6,1,6],['1','2','3','4','5','6','7','8','9']]
	m[57]=['0',[6,2,6],['1','2','3','4','5','6','7','8','9']]
	m[58]=['0',[6,3,7],['1','2','3','4','5','6','7','8','9']]
	m[59]=['0',[6,4,7],['1','2','3','4','5','6','7','8','9']]
	m[60]=['0',[6,5,7],['1','2','3','4','5','6','7','8','9']]
	m[61]=['0',[6,6,8],['1','2','3','4','5','6','7','8','9']]
	m[62]=['0',[6,7,8],['1','2','3','4','5','6','7','8','9']]
	m[63]=['0',[6,8,8],['1','2','3','4','5','6','7','8','9']]
	
	m[64]=['0',[7,0,6],['1','2','3','4','5','6','7','8','9']]
	m[65]=['0',[7,1,6],['1','2','3','4','5','6','7','8','9']]
	m[66]=['0',[7,2,6],['1','2','3','4','5','6','7','8','9']]
	m[67]=['0',[7,3,7],['1','2','3','4','5','6','7','8','9']]
	m[68]=['0',[7,4,7],['1','2','3','4','5','6','7','8','9']]
	m[69]=['0',[7,5,7],['1','2','3','4','5','6','7','8','9']]
	m[70]=['0',[7,6,8],['1','2','3','4','5','6','7','8','9']]
	m[71]=['0',[7,7,8],['1','2','3','4','5','6','7','8','9']]
	m[72]=['0',[7,8,8],['1','2','3','4','5','6','7','8','9']]
	
	m[73]=['0',[8,0,6],['1','2','3','4','5','6','7','8','9']]
	m[74]=['0',[8,1,6],['1','2','3','4','5','6','7','8','9']]
	m[75]=['0',[8,2,6],['1','2','3','4','5','6','7','8','9']]
	m[76]=['0',[8,3,7],['1','2','3','4','5','6','7','8','9']]
	m[77]=['0',[8,4,7],['1','2','3','4','5','6','7','8','9']]
	m[78]=['0',[8,5,7],['1','2','3','4','5','6','7','8','9']]
	m[79]=['0',[8,6,8],['1','2','3','4','5','6','7','8','9']]
	m[80]=['0',[8,7,8],['1','2','3','4','5','6','7','8','9']]
	m[81]=['0',[8,8,8],['1','2','3','4','5','6','7','8','9']]
	
	return m
	
# end initGrid()

def iniRows():
	# rows is a list of lists. the inner list is a list of cells belonging to a
	# row. similarly, we'll need a list of cells belonging to each column and a
	# list of cells belonging to each square.
	rows=[]
	rn=[]
	i=1
	j=0
	while (i+j<82):
		rn.append(str(i+j))
		i=i+1
		if (i%9==0):
			rn.append(str(i+j))
			j=i+j
			i=1
			rows.append(rn)
			rn=[]
	return rows
# iniRows

def iniCols(rows):
	# now logic for the columns for each row, select nth cell and put it in
	# the current column
	i=0 # count through the rows
	j=0 #the column
	cols=[]
	cn=[]
	while (j<9):
		cn.append(rows[i][j])
			
		i+=1
		if i==9:
			j+=1
			i=0
			cols.append(cn)
			cn=[]
	return cols
# iniCols

def iniSqs():
	return [['1','2','3','10','11','12','19','20','21'],['4','5','6','13','14','15','22','23','24'],['7','8','9','16','17','18','25','26','27'],['28','29','30','37','38','39','46','47','48'],['31','32','33','40','41','42','49','50','51'],['34','35','36','43','44','45','52','53','54'],['55','56','57','64','65','66','73','74','75'],['58','59','60','67','68','69','76','77','78'],['61','62','63','70','71','72','79','80','81']]


def iGame():
	# built in game
	return [['0', '0', '3', '0', '0', '0', '8', '5', '0'], ['6', '0', '0', '0', '1', '0', '0', '3', '4'], ['0', '0', '0', '6', '0', '0', '7', '0', '0'], ['0', '0', '0', '0', '6', '4', '0', '0', '1'], ['4', '7', '0', '0', '0', '2', '5', '6', '8'], ['1', '6', '2', '5', '0', '8', '4', '0', '3'], ['8', '0', '1', '2', '0', '6', '3', '0', '0'], ['0', '2', '0', '0', '0', '0', '1', '0', '5'], ['0', '4', '5', '8', '0', '0', '6', '9', '0']]
	
# end iGame function


def loadGame(gameList):
	# update the grid value and possibles list with a game. From a fle or the internal game
	r=0 # row 
	c=0 # column
	cell=1
	while cell <=81:
		# print("inserting "+str(r)+" "+str(c) + " cell " + str(cell) + "value" + gameList[r][c])
		l=gameList[r][c]
		ml=m[cell]
		ml[0] = l
		if ml[0] != '0':
			ml[2]=[] # if the possible list is empty, we know what the cell value is
		m[cell]=ml
		# l is the value that needs to go in cell, but it needs to be removed from the 
		# list of possible values
		c+=1
		if c==9:
			c=0
			r+=1
		cell += 1
	return 0
	
# end loadGame

def drawGrid():
	r = CELL_SIZE
	c = CELL_SIZE
	lc = 1
	while r <= 540:
		if lc == 4 or lc == 7:
			pygame.draw.line(WIN, RED, (r, c), (r, WIDTH - CELL_SIZE), 3)
		else:
			pygame.draw.line(WIN, WHITE, (r, c), (r, WIDTH - CELL_SIZE), 1)
		r += CELL_SIZE
		lc += 1
	r = CELL_SIZE
	c = CELL_SIZE
	lc = 1
	while c <= 540:
		if lc == 4 or lc == 7:
			pygame.draw.line(WIN, RED, (r, c), (HEIGHT - 200 - CELL_SIZE, c), 3)
		else:
			pygame.draw.line(WIN, WHITE, (r, c), (HEIGHT - 200 - CELL_SIZE, c), 1)
		c += CELL_SIZE
		lc += 1
	# draw the basic sudoku grid
	
# end drawGrid

def drawValues():
	# so now we need to print the values in the matrix on the grid
	c = 1
	while c < 82:
		ml = m[c]
		rcs = ml[1]
		if ml[0] != '0':
			xloc = (CELL_SIZE+2)*(int(rcs[1])+1)
			yloc = (CELL_SIZE+2)*(int(rcs[0])+1)
			textSurface=pFont.render(ml[0],True, GREEN)
			WIN.blit(textSurface,(xloc,yloc))
		c += 1
	return
	
# end drawValues

def chkRCS(cell, val, dLevel):
	# m is the game, cell is the number of the cell we want to change, and 
	# val is the proposed new value. returns True if no conflicts, False if
	# conflicts. get the RCS values from the cell.
	# loop through all the cells in m except the cell we're interested in
	# if one of RCS matches, check the value of the cell against val and if 
	# they match, we've detected a conflict.

	# get RCS for the cell in question
	cTBC = m[cell]
	cTBCrcs = cTBC[1]
	cRow = cTBCrcs[0]
	cCol = cTBCrcs[1]
	cSqr = cTBCrcs[2]
	lCnt = 0 # point to the cell to test against
	while lCnt < 81:
		if lCnt != cell:
			lm = m[lCnt+1]
			if lm[0] != 0: # if it already has a value, don't bother
				lmrcs = lm[1]
				if cRow == lmrcs[0] or cCol == lmrcs[1] or cSqr == lmrcs[2]:
					if val == lm[0]: # trying to change to a value another cell has
						print("want to change " + str(cell) + " to " +str(val))
						print(cTBC)
						print("found " + str(lCnt+1) + " with value " + str(lm[0]))
						print(lm)
						print("The program fails")
						with open("debug.dat","a") as file:
							file.write("chkRCS checking cell " + str(cell) +" ")
							file.write("against "+str(lCnt+1) + "\n")
							file.close()
						return False
		lCnt += 1
	
	return True
	
# end chkRCS


def updateGame(dLevel):
	# this function sweeps through all the cells. if the cell has a value !=
	# 0, it will pull the intersecting lists and remove that value from the 
	# list of possible values for all the cells in those lists
	chgs = False # changed to true if there are any changes
	cell = 1
	while cell < 82:
		l = m[cell] # get the lists for the current cell,
		if l[0] != '0':
			rw = l[1][0] # list of cells in intersecting row
			cl = l[1][1] # columns
			sq = l[1][2] # square
			v = l[0] # value to remove from possible lists
			# ls is a list of cells that need to be processed
			ls = rows[rw]+cols[cl]+sqs[sq] # all the cells in one list
													 # obviously some duplicates

			for c in ls: # process all cells in ls
				d = m[int(c)] # trying to get the lists for cell c

				if d[0] == '0' and int(c) != cell: # if the value is 0
					e = d[2] # possible list of cell under consideration
					f=d[1] # rcs of cell under consideration
					try:
						e.remove(v)
						m[int(c)] = ['0',f,e] # 0 because that's what the original value was
						chgs=True
						if dLevel=='1':
							with open("debug.dat","a") as file:
								file.write("updateGame cell "+str(cell) + " changing "+ str(c)+'=')
								file.write("value " +v+' possibles '+str(e)+'\n')
								file.close()
					except ValueError:
						pass
					# print(m[int(c)])
			# now go through all cells referenced in ls and remove
		cell += 1
	return chgs
# end updateGame

def updateLval (dLevel):
	# this function goes through the matrix. for each non zero value, if 
	# there is exactly one element in the possible list, it becomes the value
	chgs = False
	cell = 1
	while cell < 82:
		l = m[cell]
		v = l[0] # current value of cell.it's a string
		rcs = l[1]
		poss = l[2] # possibles list
		if len(poss) == 1 and v == '0':
			v = poss[0]
			check = True
			check = chkRCS(cell,v,dLevel)
			if check == False:
				print("Trying to make an illegal move on cell "+str(cell))
				print("program failure, returning False")
				chgs = False
				errFlag = True
			else:
				chgs = True
				m[cell] = [v,rcs,[]]
		cell += 1
	return chgs
# end updateLval
	
def sPuzzle():
	# print("launch the solve process here")
	lvChg = True
	upChg = True
	iCnt=0
	dLevel = 0 # for now
	x2 = 0 # I think we quit too soon
	while errFlag == False and lvChg and upChg and x2 < 2:
		ugChg = updateGame(dLevel)
		lvChg = updateLval(dLevel)
		if ugChg==False and lvChg==False:
			x2 += 1
		# This prints each step so the 'logic' can be followed
		if dLevel == '1':
			print("iteration "+ str(iCnt))
		#printGrid(m,rows)
		iCnt+=1
	return
	
# end sPuzzle

def readFile(fname):
	rowList=[]
	with open(fname) as file:
		for rw in file:
			rowList.append(list(rw.rstrip()))
	return rowList
	
#end readFile
	
def postUserInput(mouseLoc, keyVal):
	# translate mouseLoc into the cell, keyVal is what the user pressed
	# store it in m
	print(mouseLoc)
	# keyVal is an int and is the same for all numbers pressed on the keypad
	print(keyVal)
	if keyVal == 1073741922:
		keyVal = 48
		kv=48
	elif keyVal > 100000000:
		kv = keyVal - 1073741864
		print(kv)
	else:
		kv = keyVal
	
	if kv >= 48 and kv <= 58:
		# figure out what to do with stuff from outside the number keys
		# need to identify and normalize keypad presses.
		print(chr(kv))
		cell = findCell(mouseLoc)
		if cell > 0 and cell <82:
			ml = m[cell]
			ml[0]=chr(kv)
			m[cell]=ml
			print("updated cell " + str(cell))
			return
	return
# end postUserInput

def findCell(mouseLoc):
	cellNo = 84 # invalid cell
	# mouseLoc is the location clicked (col, row), this function converts
	# that to a cell number
	c = xlate(mouseLoc[0])
	r = xlate(mouseLoc[1])
	# then search rcs values in m for the cell
	i=1
	while i<82:
		ml=m[i]
		rcs=ml[1]
		if rcs[0]==r and rcs[1]==c:
			return i
		i+=1
	return cellNo
# end findCell

def xlate(n):
	# not the most portable way if figuring this out, but it works for now.
	if n>56 and n<108:
		return 0
	if n>115 and n< 158:
		return 1
	if n>167 and n<213:
		return 2
	if n>220 and n<268:
		return 3
	if n>274 and n< 320:
		return 4
	if n>330 and n<375:
		return 5
	if n>384 and n<430:
		return 6
	if n>435 and n<485:
		return 7
	if n>490 and n<539:
		return 8
	return 10
# end xlate

def main(args):
	mode = ''
	fname = ''
	if len(args)== 1:
		mode = 'default'
		#print("default mode not implemented")
	elif args[1] == 'F'and len(args) == 3:
			mode = 'file'
			fname = args[2]
			gameList = readFile(fname)
			loadGame(gameList)
	elif args[1] == 'i' or args[1] == 'I':
		gameList = iGame()
		loadGame(gameList)
	else:
		print("unrecognized mode")
		print(args)
		return 0

	
	clock = pygame.time.Clock()
	run = True
	mouseClicked = False
	while run:
		WIN.fill(BLACK)
		drawGrid()
		clock.tick(30) # frame rate 30 frames per second
		mousePress = []
		#event handler
		for event in pygame.event.get():
			button.listen(event)
			button.draw()
			if event.type == pygame.QUIT: # click close window
				run = False
			if errFlag == False and event.type == pygame.MOUSEBUTTONDOWN:
				mousePress = pygame.mouse.get_pressed()
				mouseClicked = True
				mouseLoc=pygame.mouse.get_pos()
				print("mouse clicked")
			if errFlag == False and mode == 'default' and mouseClicked and event.type == pygame.KEYDOWN:
				print(str(event.key)) # valuse 49 - 57 are the integers
				postUserInput(mouseLoc, event.key)
				mouseClicked = False
					# cellNo=idCell(mouseLoc) # cell user wants to putdata in
		drawValues()
		pygame_widgets.update(event)  # Call once every loop to allow widgets to render and listen
		pygame.display.update() # need to refresh screen with every iteration
	pygame.quit()
	return 0

# end main function

# global variables. I don't like using global variables. do better next time

#initialize non pygame structures used everywhere.
m=initGrid()
# rows, cols, sqs are static lists that point into the grid m. m changes dynamically through the game
rows=iniRows()
cols=iniCols(rows)
sqs=iniSqs()

errFlag = False

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
