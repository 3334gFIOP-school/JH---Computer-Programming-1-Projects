# Jackson Hauley - Secret Cypher

# Declaring alphabet string
alphabetString = "abcdefghijklmnopqrstuvwxyz"

# Defining functions
def encode(secret):
    secret = secret.lower()
    secretlist = list(secret)
    encoded = [""]
    for firstLetter in secretlist:
        if firstLetter in alphabetString:
            position = alphabetString.index(firstLetter)
            position2 = (position + decodeAmount) % 26
            encoded.append(alphabetString[position2])
        else:
            encoded.append(firstLetter)
    word2 = "".join(encoded)
    return word2

def decode(secret2):
    secret2 = secret2.lower()
    secretlist2 = list(secret2)
    encoded2 = [""]
    for firstLetter in secretlist2:
        if firstLetter in alphabetString:
            position3 = alphabetString.index(firstLetter)
            position4 = (position3 - decodeAmount) % 26
            encoded2.append(alphabetString[position4])
        else:
            encoded2.append(firstLetter)
    word2 = "".join(encoded2)
    return word2

def ask():
    decide = input("Do you want to encode or decode?: ")
    if "encode" in decide:
        sentence = input("What sentence do you want to encode?: ")
        print("Encoded sentence:", encode(sentence))
    elif "decode" in decide:
        sentence = input("What sentence do you want to decode?: ")
        print("Decoded sentence:", decode(sentence))
    else:
        print('That is not a choice! Type either "encode" or "decode"!') 
        ask()

# Starting Code
decodeAmount = int(input("How many letters do you want to decode/encode by? "))
ask()