# Cycle 1 Exercises – Python data structures, performing calculations
## Aims and objectives
* Familiarise yourself with Jupyter notebooks if you haven’t used it in the last semester
* Refresh Python fundamentals, such as lists, tuples, dictionaries


## This week’s exercises
These exercises involve refreshing Python data structures such as lists, and dictionaries.
### Task 0 – Jupyter (for those who have not used it before)
The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.


We can use Jupyter notebooks on the lab machines or on the virtual GlasgowAnywhere machines.
To use Jupyter, please follow [this guide](https://moodle.gla.ac.uk/pluginfile.php/2538141/mod_resource/content/1/JupyterGuide2016%20%281%29.pdf) (I know it is written refering to a lab machine, please just pretend it says 'your machine'). To run Jupyter on your own machine, I suggest you install via [Anaconda](https://www.anaconda.com/) - I'll do a demo of running a notebook this way in one of our first lectures.  
It is possible to run notebooks entirely online using on non-university resources via (for example) [Google's colab](https://colab.research.google.com) or [Cocalc](https://cocalc.com/)


### Task 1 – Review your notes from CS1CT or the online text
Review what you've learned about lists, dictionaries, and tuples, as well as traversing them with looks and using if/then control structures.  

### Task 2 – List manipulations

Write the following functions in Python. If you can, try to present multiple implementation for the same problem. 
1.	`howManyZeroes(a)`: Write a function that counts the number of entries in list a that are equal to the number 0
2.	`getTheOddNumbers(a)`: Write a function that returns a list containing only the odd-number entries of a list.



### Task 3 – Tuple manipulations

Write the following functions in Python. If you can, try to present multiple implementations for the same problem. 
1.	`pairTogether(list1, list2)`:  Write a function that takes two lists of the same length, and returns a new list that contains 2-tuples where the ith item in the new list is a pair composed of a 2-tuple of (ith item in list1, ith item in list2).

```
pairTogether([‘a’, ‘b’, ‘c’, ‘d’], [1, 2, 3, 4]) 

output: [(a, 1), (b, 2), (c, 3), (d, 4)]  
```
### Task 4 – Dictionary manipulations

Write the following functions in Python. If you can, try to present multiple implementation for the same problem. 
1.	`comparedicts(dict1, dict2`): Write a function that compares two dictionaries by both their keys and values and return a Boolean – loop through the dictionaries, do not simply directly compare the dictionaries with ==.

```
Input: {'a': 1, 'b': 2}, {'a': 1, 'b': 2}
Output: True	

Input: {'a': 2, 'b': 2}, {'a': 1, 'b': 2}
Output: False


Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 2}
Output: False
```

2.	`differences(dict1, dict2)`: Write a function that displays the differences between two dictionaries by returning a set of tuples.   You can assume that the dictionaries have the same set of keys.  (Extra exercise: think about how you would deal with it if they had different sets of keys?)
```

Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 2}
Output: {('b', 3), ('b', 2)}

Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 3}
Output: an empty dictionary, or None
```
