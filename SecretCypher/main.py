# Jackson Hauley - Secret Cypher

# List of all the letters
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabetString = "abcdefghijklmnopqrstuvwxyz"

# Creating function
def encode(secret):
    secretlist = list(secret)
    for x in range(7):
        print(secretlist) # temporary 
        firstLetter = secretlist[0]
        # THIS IS THE MOST BROKEN CRAP THAT EVER EXISTED
        print(firstLetter) # temporary
        position = secretlist.index(firstLetter)
        secretlist.pop(0)
        secretlist.append(position)
    word2 = "".join(secretlist)
    return(word2)


# Testing function
word = input('What word do you want to encode?: ')
print(encode(word))