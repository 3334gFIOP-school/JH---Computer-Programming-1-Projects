# Jackson Hauley - Pig Latin Converter

# Checking for vowels
vowels = ["a","e","i","o","u"]

# Function Created
def convert(pig):
    output = ""
    piglist = list(pig)
    if piglist[0] == vowels:
        testing = piglist[0]
        piglist.remove[0]
        print(piglist)
        piglist.append(testing)
    output = "".join(piglist)
    output = output + "ay"
    return(output)

# Testing
print(convert(input("What do you want to convert?: ")))