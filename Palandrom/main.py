#Jackson Hauley Palandrome Assignment

print("Jacksons Palindrome Checker")

word = input("What word do you want to check?: ")

print("Reversed:",str(word)[::-1])

# Palandrome checker
if word == str(word)[::-1]:
	print("The word is a palindrome!")
else:
	print("The word is not a palindrome!")