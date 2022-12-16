# Cycle 5 Lab Exercises: Time complexity and big-O notation

### Objectives:
1. Write code that can generate a plot of the runtime of code.
2. Practice finding the time complexity in big-O notation of code

You may find yourself working lots on paper for this lab - that is expected!

### Task 0:
 Write a higher-order function `plotRuntimes` that takes as a parameter a function `func`, and a list of lists that will be inputs for `func`.  Your function `plotRuntimes` should call `func` on each of the provided inputs, and record the running time. You should collect those runtimes, and plot them using `matplotlib`, with the runtimes on the y-axis and the sizes of the lists on the x-axis.  Save or display the figure.

Write your code in the `lab_code_complexity.py` file, and call the `testRuntimes` function to test it.

### Task 1 - Plotting runtimes

Here you will write a few simple functions and plot their runtimes.

1. Write a function that loops over the elements of a list and finds their sum. Plot its runtime - what big-O complexity do you think this looks like?
2. Write a function that loops over the elements of a list and finds the maximum value. Plot its runtime - what big-O complexity do you think this looks like?
3. Write a function that uses a nested loop to check, for each element of a list, if it is the only occurrence of that item in the list.  Plot its runtime - what big-O complexity do you think this looks like?
4. Plot the runtime complexities of the provided functions `doubleTraversalFunction, traversalFunction, sillyFunction, functionAhoy` and `functionFoo`.  What do you think their runtime complexity is?

It can be hard to tell from the plots sometimes! We will now look at the code directly.  

Task 2 - reasoning about runtimes

1. For each of the functions you plotted runtimes for, inspect the code and try to reason about the big-O runtime complexity of that code. 
2. What is the big-O complexity of running `traversalFunction` and then `sillyFunction`?
3. What is the big-O complexity of running `functionAhoy` and then `functionFoo`?
4. What is the big-O complexity of the following function:


```
def practiceFunction(myList):
   for i in range(len(myList)):
     traversalFunction(myList)
```


### Task 3 - **Stretch Task**

Try to write functions with the following time complexities:

*   O(n<sup>5</sup>)
*   O(n!)
*   O(n log(n))

Once you have written them, plot their runtimes with increasing input size to see if the plots agree with your expectations