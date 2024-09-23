# Jackson Hauley - Anagram Creator RAID

# Importing
import random

# Function
def anagram(mainword):
    generate = list(mainword)
    random.shuffle(generate)
    return("".join(generate))
    
# Inputting
mainword = input("What do you want the anagramed word to be?: ")

# Outputting
for x in range(5):
    print(anagram(mainword))