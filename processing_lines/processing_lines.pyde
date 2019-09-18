from random import *

lineArray = []

isFirstpointSet = False
firstPoint = int()

def setup():
    size (1280, 750)
    background(0)
    
def mouseClicked():
    global lineArray, isFirstpointSet, firstPoint
    
    if isFirstpointSet == False :
        firstPoint = [mouseX, mouseY]
        isFirstpointSet = True
    else :
        secondPoint = [mouseX, mouseY]
        isFirstpointSet = False
        newLine = [firstPoint, secondPoint]
        print newLine
        
        
    
    
def draw():
    pass
