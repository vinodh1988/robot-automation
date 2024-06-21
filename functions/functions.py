
#function can have functions as parameters
def doTaskWithCallback(fun):
    print("The function started its execution")
    fun("processed data") #fun is a function
    print("Finishing the function doTask")


def callbackProcessor(data):
    print("User logic")
    print("received ",data)
    print("Concluding User logic")

def processor2(x):
    print("One more user process")
    print("We process the received ",x)
    print("we are done")

doTaskWithCallback(callbackProcessor) # execution starts here
print("---------------------------------------------------")
doTaskWithCallback(processor2)



