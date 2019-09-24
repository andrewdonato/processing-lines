# processing-lines

An art program built with Processing.py

Mouse click to set line segment points.
Mouse drag to draw.
Press 'd' to delete the last line.

Created by Andrew Donato.


Next step is to calculate intersection objects
	https://www.mathopenref.com/coordintersection.html

	whenever a line segment is created, 
		it will look for intersections
		if it finds an intersection, 
			it will create an intersection object

	intersection objects will need to know the lines they are connected to (and lines their intersections)
		an intersection should be able to ask its lines about their intersections (and lines their intersections)