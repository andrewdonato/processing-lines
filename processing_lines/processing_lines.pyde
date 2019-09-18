from random import *

lineArray = []

isFirstpointSet = False
firstPoint = int()

def setup():
    # size (1280, 750)
    size (500, 500)
    background(0)
    stroke(255)
    strokeWeight(10)
    
    line(0,0,300,400)

    
def mouseClicked():
    global lineArray, isFirstpointSet, firstPoint
    
    if isFirstpointSet == False :
        firstPoint = [mouseX, mouseY]
        isFirstpointSet = True
        line(mouseX, mouseY, mouseX, mouseY)
    else :
        secondPoint = [mouseX, mouseY]
        isFirstpointSet = False

        newLineSegment = LineSegment(len(lineArray), firstPoint, secondPoint)
        newLineSegment.findMagnitude(newLineSegment.x1, newLineSegment.y1, newLineSegment.x2, newLineSegment.y2)
        lineArray.append(newLineSegment)
        
        print "Line Segment: %s" %(newLineSegment.i)
        print "Coordinates : %s, %s" %(newLineSegment.a, newLineSegment.b)
        print "Magnitude   : %s" %(newLineSegment.magnitude)

def draw():
    global lineArray
    for segment in lineArray:
        line(segment.x1, segment.y1, segment.x2, segment.y2)        
        
class LineSegment():
    def __init__(self, creationIndex, pointA, pointB):
        
        self.i = creationIndex
        self.a = pointA
        self.b = pointB
        self.x1 = self.a[0]
        self.y1 = self.a[1]
        self.x2 = self.b[0]
        self.y2 = self.b[1]
        self.magnitude = int()
        
    def findMagnitude(self, x1, y1, x2, y2):
        # line(0,100,345,100)
        # line(0,0,400,300)
        # print mag(400,300)
        
        zeroedX2 = abs(self.x2 - self.x1)
        zeroedY2 = abs(self.y2 - self.y1)
        self.magnitude = mag(zeroedX2,zeroedY2)
        
