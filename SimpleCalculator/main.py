# Jackson Hauley - Simple Calculator

# Asking for the numbers
number1 = input("What is the first number you want to calculate?: ")
number2 = input("What is the second number you want to calculate?: ")

# Makes the answer integers
number1=int(number1)
number2=int(number2)

# The actual calculations
print("Addition:",number1+number2)
print("Subtraction:",number1-number2)
print("Multiplication:",number1*number2)
print("Division:",number1/number2)
print("Exponented:",number1**number2)
print("Modulo:",number1%number2)
print("Floor Division:",number1//number2)