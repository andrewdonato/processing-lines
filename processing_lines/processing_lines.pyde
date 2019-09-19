from random import *

lineArray = []
isFirstpointSet = False
firstPoint = int()

def setup():
    # size (1280, 750)
    size (500, 500)
    background(0)
    stroke(255)
    strokeWeight(1)
    
    ## Calibration line, magnitude 500, xleg is magnitude 300, yleg is magnitude 400 
    # line(0,0,300,400)
    
    print "Mouse click to set line segment points"
    print "Mouse drag to draw"
    print "Press 'd' to delete the last line"
    print "Created by Andrew Donato"
    print ""
    text("Created by Andrew Donato", width*0.01, height*0.98)
    
def mouseClicked():
    drawLine()
def mouseDragged():
    drawLine()    

def drawLine():
    global lineArray, isFirstpointSet, firstPoint
    
    if isFirstpointSet == False :
        firstPoint = [mouseX, mouseY]
        isFirstpointSet = True
        line(mouseX, mouseY, mouseX, mouseY)
        print "First point set"
    else :
        secondPoint = [mouseX, mouseY]
        isFirstpointSet = False

        newLineSegment = LineSegment(len(lineArray), firstPoint, secondPoint)
    
        newLineSegment.findMagnitude()
        # newLineSegment.findMagnitude(newLineSegment.x1, newLineSegment.x2, newLineSegment.y1, newLineSegment.y2)
        lineArray.append(newLineSegment)
        
        print "Second point set"
        print "Line Segment: %s" %(newLineSegment.i)
        print "Coordinates : %s, %s" %(newLineSegment.a, newLineSegment.b)
        print "Magnitude   : %s" %(newLineSegment.magnitude)
    
def keyPressed():
    global lineArray
    
    if len(lineArray) > 0 :
        print len(lineArray)
        print lineArray[len(lineArray)-1]
        print str(lineArray)
        
        if key == 'd' or key == 'D' :
            print key
            del lineArray[len(lineArray)-1]
    
def draw():
    global lineArray
    
    background(0)
    for segment in lineArray:
        segment.segmentDraw()        
        
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
        
    def findMagnitude(self):
        zeroedX2 = abs(self.x2 - self.x1)
        zeroedY2 = abs(self.y2 - self.y1)
        self.magnitude = mag(zeroedX2,zeroedY2)
        
    def segmentDraw(self):
        line(self.x1, self.y1, self.x2, self.y2)
        
