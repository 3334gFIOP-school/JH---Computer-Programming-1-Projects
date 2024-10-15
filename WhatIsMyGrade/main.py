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

def request_details():
    for x in range(classes):
        class_name = input(f"What is class number {x+1}'s name?: ")
        classlist.append(class_name)
        grade = input(f"What is your percent grade in {classlist[x]}?: ")
        gradelist.append(grade)

def convert_grades():
    for x in range(gradelist):
        converting = gradelist[x]
        if converting >=100:
            letters.append("A+")
        elif converting >= 96:
            letters.append("A")
        elif converting >=90:
            letters.append("A-")
        elif converting >=87:
            letters.append("B+")
        elif converting >=84:
            letters.append("B")
        elif converting >=80:
            letters.append("B-")
        

    
# Startup
start()