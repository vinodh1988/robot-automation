def filterCustom(listx,callback):
    return [ x for x in listx if callback(x)]

def mapCustom(listx,callback):
    return [callback(x)  for x in listx]

def bigNum(x):
    return True if x>1000 else False

def evenNum(x):
    return True if x%2==0 else False

def greetName(x):
    return "Hello! "+x

numlist=[3,53,6,36,36,6909,3543,34,36,60,36,9001,1005]
namelist=["Arvind","Gary","Sanjay","Nicholas","Robert"]
print(filterCustom(numlist,bigNum))
print(filterCustom(numlist,evenNum))
print(filterCustom(numlist,lambda x: True if x%5==0 else False))
print(filterCustom(numlist,lambda x: True if x>=10 and x<=99 else False))
print(mapCustom(namelist,greetName))
print(mapCustom(namelist,lambda x: x+" is aBig Name" if len(x)>6 else x+" is SmallName" ))

