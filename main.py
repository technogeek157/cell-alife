# -*- coding: utf-8 -*-

"""
Created by Lucas Thelen of NGHS
"""

global xy, buffArr

def initList(depth):#ONLY USE AT THE BEGINNING    
    return [['0']*depth for _ in range(depth)]

def clear():
    print '\n' * 1000

def printList(l):
    for i in l:
        print i

def setPos(v, x, y):
    xy[y-1][x-1] = v

def changePos(v, x, y, xChange, yChange):
    if xy[y+yChange-1][x+yChange-1] == 0:#checks is move to space is unnocupied
        if xy[y-1][x-1] == v:#checks if move from space is occupied with v
            if yChange == -1 or yChange == 1 or xChange == 0:
                if xChange == -1 or xChange == 1 or xChange == 0:
                    setPos(v, x+xChange, y+yChange)#sets positions
                    setPos('0', x, y)

class lipid(object):
    """
    A lipid tile on a grid.
    """
    
    def __init__(self, xPos, yPos):
        """
        Initiates where this object is
        """
        self.x = xPos
        self.y = yPos
        
        setPos('l', self.x, self.y)
        
    def move(self, xMove,yMove):
        """
        Moves the item according to these values
        """
        changePos('l', self.x, self.y, xMove, yMove)
        
        self.x = self.x + xMove
        self.y = self.x + yMove

xy = initList(5)

clear()

myLipid = lipid(3,3)

printList(xy)

myLipid.move(1,1)
print '\n'
printList(xy)