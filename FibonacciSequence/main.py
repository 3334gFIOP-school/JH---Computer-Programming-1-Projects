# Jackson Hauley - Fibonacci Sequence RAID

# Ask for how long fibonacci sequence should go
timer = int(input("How many times do you want this to go?: "))

# Declaring Variables
num1 = 0
num2 = 1
num3 = 0
output = ""

# Calculating
output = str(num1) + ", " + str(num2)
while timer > 0:
    timer = timer - 1
    num3 = num2 + num1
    output += ", " + str(num3)
    num1 = num2
    num2 = num3
    
# Printing
print(output)