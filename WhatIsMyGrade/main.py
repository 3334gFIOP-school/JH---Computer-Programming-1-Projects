# Jackson Hauley - What Is My Grade

# Defining 
classlist = []
gradelist = []
letters = []

def start():
    global classes
    print("======================\nGrade Calculator\n======================")
    classes = int(input("How many classes do you have?: "))
    request_details()
    for x in range(classes):
        appending = convert(gradelist[x])
        letters.append(appending)
    print("\nHere are your final grades:")
    print_grades()
    print(f"Your average grade is a {average():.2f}% or a(n) {convert(average())}\n")
    

def request_details():
    global classlist, gradelist, letters
    classlist = []
    gradelist = []
    for x in range(classes):
        try:
            class_name = input(f"What is class number {x+1}'s name?: ")
            classlist.append(class_name)
        except ValueError:
            print("Invalid Input!")
            request_details()
        try:
            grade = int(input(f"What is your percent grade in {classlist[x]}?: "))
            gradelist.append(grade)
        except ValueError:
            print("Invalid Input!")
            request_details()

def convert(converting):
    if converting >= 1000000000000000000:
        output = "∞"
    elif converting >= 1000000000:
        output = "A++++++"
    elif converting >= 1000000:
        output = "A+++++"
    elif converting >= 100000:
        output = "A++++"
    elif converting >= 10000:
        output = "A+++"
    elif converting >= 1000:
        output = "A++"
    elif converting >= 100:
        output = "A+"
    elif converting >= 96:
        output = "A"
    elif converting >= 90:
        output = "A-"
    elif converting >= 87:
        output = "B+"
    elif converting >= 84:
        output = "B"
    elif converting >= 80:
        output = "B-"
    elif converting >= 75:
        output = "C+"
    elif converting >= 70:
        output = "C"
    elif converting >= 68:
        output = "C-"
    elif converting >= 66:
        output = "D+"
    elif converting >= 63:
        output = "D"
    elif converting >= 60:
        output = "D-"
    else:
        output = "F"
    return output 

def print_grades():
    for x in range(classes):
        print(f"Your grade for {classlist[x]} is a(n) {letters[x]}")

def average():
    combine = 0
    for grade in gradelist: 
        combine += grade 
    return combine/classes  

# Startup
start()