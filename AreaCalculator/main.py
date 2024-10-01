# Jackson Hauley - Area Calculator RAID
import math
def calculateSquare(side): return side*side
def calculateRectangle(height,width): return height*width
def calculateTriangle(height,base): return base*height*1/2
def calculateCircle(radius): return math.pi*radius**2
def calculateTrapezoid(base1,base2,height): return (base1+base2)/2*height
def ask():
    print("What do you need to calculate?\n1. Area of a Square\n2. Area of a Rectangle\n3. Area of a Triangle\n4. Area of a Circle\n5. Area of a Trapezoid\n(wrong int will default to trapezoid)")
    selection = int(input("Select which number: "))
    if selection == 1: return calculateSquare(int(input("What is the side length of the square?: ")))
    elif selection == 2: return calculateRectangle(int(input("What is the heigth of the rectangle?: ")),int(input("What is the width of the rectangle?: ")))
    elif selection == 3: return calculateTriangle(int(input("What is the heigth of the triangle?: ")),int(input("What is the base of the triangle?: ")))
    elif selection == 4: return calculateCircle(int(input("What is the radius of the circle?: ")))
    else: return calculateTrapezoid(int(input("What is the first base of the trapezoid?: ")),int(input("What is the second base of the trapezoid?: ")),int(input("What is the height of the trapezoid?: ")))
print("The output is",ask())