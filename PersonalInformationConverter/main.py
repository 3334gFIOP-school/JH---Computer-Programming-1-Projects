# Jackson Hauley - Personal Information Converter

name = input('What is your name?: ')
age = input('What is your age?: ')
height = input('How tall are you?(meters): ')
favnum = input('What is your favorite number?: ')

print('Original Output: name',name,'age:',age,'height:',height,'favorite number:',favnum)
print('Converted Output: name',str(name),', age:',int(age),', height:',float(height),', favorite number:',int(favnum))