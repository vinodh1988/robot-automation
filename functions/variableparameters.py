#sometimes you may want a function to be flexible in terms of number of parameters passed
#Such requirement in a way could be managed with the following approach

def sum(*a):
    result=0
    for x in a:
        result+=x
    return result

# if I use * befor the variable a, a becomes a tuple and while the function
# i can pass any number of parameter

print(sum(1,2))
print(sum(1,2,3))
print(sum(34,35,36,6,64))
print(sum())