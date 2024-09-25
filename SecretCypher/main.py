# Jackson Hauley - Secret Cypher

# List of all the letters
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Creating function
def encode(secret):
    secretlist = list(secret)
    for x in range(7):
        secretlist.append(secretlist[0])
        secretlist.pop(0)
    return("".join(secretlist))



# Testing function
word = input('What word do you want to decode?: ')
print(encode(word))