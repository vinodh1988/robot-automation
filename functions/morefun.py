# function is also an object in object
# it is first class citizen in python language , like any other literal,
# function is also assignable to variable

def original():
    print("Hey I am original version")

duplicate=original #assigning a function to another variable

duplicate()

def sum(a,b):
    return a+b

add=sum

print(add(23,345))