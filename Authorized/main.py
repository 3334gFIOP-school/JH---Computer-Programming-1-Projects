# Jackson Hauley - Authorized

# Lists
allowed = ["Jackson","Pedro","Xavier","Lancer","Sans","Virus","George","Eli","Lincoln","Owen","Your Mom"]
admins = ["Jackson", "Pedro"]
operators = ["Jackson"]

# Defining Functoins
def cs():
    print("\033c")

def check_user():
    if user in operators:
        print("hi op")
    else:
        if user in admins:
            print("hi admin")
        else:
            if user in allowed:
                print("hi allowed")
            else: 
                print("Loud Incorrect Buzzer SFX")


# Start
cs()
print("Access Terminal\n===========================")
user = input("Enter Username: ")
cs()
check_user()

