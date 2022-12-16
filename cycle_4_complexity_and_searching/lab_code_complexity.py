import time
import random 
import matplotlib.pyplot as plt

def traversalFunction(myList):
    for i in range(len(myList)):
        myList[i] = myList[i] +3


def doubleTraversalFunction(myList):
    for i in range(len(myList)):
      for j in range(len(myList)):
        myList[i] = myList[i] +3


def sillyFunction(myList):
  return myList[0]

def functionAhoy(myList):
  items = []
  for item in myList:
    for i in range(len(myList)):
      for j in range(i, myList):
        items.append(str(item) + str(i*j) + 'ahoy')
  return items

def functionFoo(myList):
  newList = []
  for i in range(7):
    for j in range(len(myList)):
      newList.append(i*myList[j])



def testRuntimes(functionName, maxSize):
    maxN = int(maxSize)
    increment = int(maxSize/100)
    if increment <1:
      increment = 1
    
    inputs = []
    for i in range(0, maxN +1, increment):
        res = random.sample(range(0, maxN), i) 
        inputs.append(res)
    plotRuntimes(traversalFunction, inputs)
    

def plotRuntimes(func, listOfInputs):
    return None
        

# this call tests the runtime of the input function on some random
# lists of numbers up to maxListSize
# It won't work until you've implemented plotRuntimes
testRuntimes(functionAhoy, maxListSize)

