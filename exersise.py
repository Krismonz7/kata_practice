#Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.
#(In this case, all triangles must have surface greater than 0 to be accepted).
import math
def is_triangle(a, b, c):
    def aviable(a,b,c):
        a = a/2
        b = b
        height = a*a + b*b
        height = height - b*b
        height = math.sqrt(height)
        area = (a * height) / 2
        print(area)
        if area > 0:
            return True
        
        else:
            return False
    available = aviable(a,b,c)
    return available