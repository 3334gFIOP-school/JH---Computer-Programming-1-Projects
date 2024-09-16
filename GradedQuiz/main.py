# Jackson Hauley - Graded Quiz

# Declaring score
score = 0

# Questions
answer1 = int(input("What is 1 + 1?: "))
if answer1 == 2:
    score += 1

answer2 = int(input("What is 1 + 5?: "))
if answer2 == 6:
    score += 1

answer3 = int(input("What is 10 + 11?: "))
if answer3 == 21:
    score += 1

answer4 = int(input("What is 2 ** 10?: "))
if answer4 == 1024:
    score += 1

answer5 = int(input("What is 1 + 122?: "))
if answer5 == 123:
    score += 1

# Printing final score
print("You got a final score of",str(score)+"!")