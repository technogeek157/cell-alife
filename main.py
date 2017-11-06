# -*- coding: utf-8 -*-

"""
Created by Lucas Thelen of NGHS
"""

global xy, buffArr

def initList(depth):#ONLY USE AT THE BEGINNING    
    return [[0]*depth for _ in range(depth)]

def clear():
    print '\n' * 1000

def printList(l):
    for i in l:
        print i

def setPos(v, x, y):
    xy[y-1][x-1] = v

def changePos(v, x1, y1, x2, y2):
    if xy[y2-1][x2-1] == 0:#checks is move to space is unnocupied
        if xy[y1-1][x1-1] == v:#checks if move from space is occupied with v
            if x2 - x1 <= 1 or x1 - x2 <= 1:#makes sure that the distance is one or less
                if y2 - y1 <= 1 or y1 - y2 <= 1:
                    setPos(v, x2, y2)#sets positions
                    setPos(0, x1, y1)

xy = initList(5)

clear()

printList(xy)
print '\n'
xy[2][2-1] = 1
printList(xy)