CS-1117 : 2016-2017 : Assignment #1 : Functions

def BoxVolume( length, breadth, height ) :
# The volume of a (cuboid) box of dimensions 'length', 'breadth',
# and 'height', where each of these is a positive number
return length * breadth * height

def Perimeter( width, height ) :
# The length of the perimeter of a rectangle of dimensions 'width'
# and 'height', where each of these is a positive number
return 2 * ( width + height )

def ToSeconds( days, hours, minutes, seconds ) :
# The total number of seconds in 'days' days, 'hours' hours,
# 'minutes' minutes, and 'seconds' seconds, where each of these
# is a non-negative integer
return ( ( days * 24 + hours ) * 60 + minutes ) * 60 + seconds
