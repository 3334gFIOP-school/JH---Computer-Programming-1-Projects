# Jackson Hauley - Pig Latin Converter

# Checking for vowels
vowels = ["a", "e", "i", "o", "u"]

# Function Created
def convert(pig):
    piglist = list(pig.lower())
    if piglist[0] in vowels:
        output = pig + "yay"
    else:
        for x in range(len(piglist)):
            if piglist[x] in vowels:
                output = "".join(piglist[x:]) + "".join(piglist[:x]) + "ay"
                break
        else:
            output = pig + "ay"
    return output

# Testing
word = input('What do you want to convert?: ')
print(word,"is the input, in pig latin it is")
print(convert(word))
