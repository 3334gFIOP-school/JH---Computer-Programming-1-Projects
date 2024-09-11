# Jackson Hauley Average Grade Calculator

# Asking for grades
class1 = float(input("What is your first classes grade in percent?: "))
class2 = float(input("What is your second classes grade in percent?: "))
class3 = float(input("What is your third classes grade in percent?: "))
class4 = float(input("What is your fourth classes grade in percent?: "))
class5 = float(input("What is your fifth classes grade in percent?: "))
class6 = float(input("What is your sixth classes grade in percent?: "))
class7 = float(input("What is your seventh classes grade in percent?: "))
class8 = float(input("What is your eighth classes grade in percent?: "))

# Calculating average
average = (class1+class2+class3+class4+class5+class6+class7+class8)/8
average = (round(average,2))

# Printing average
print("Your average grade is",average)