# CS1PX Lab Exercises Cycle 2: Recursion and higher-order functions

Aims:
1.	Practice writing recursive functions 
    a.	Make sure you can identify the base case and the recursive case
    b.	Tracing recursion - be sure you can trace your code
2.	Practice using higher-order functions 

## This week’s exercises 
This week may be challenging - both recursion and higher-order functions can be tricky to get your head around the first time!  Practice will help.  Task 1 is the most fundamental of the three tasks, so focus on getting those done if you are struggling for time.  
You may find it useful to do some planning on paper before you start working on your machine. 
 
### Task 1 - Recursive functions

In all three cases, think about your base case and recursive case, then write your code (on paper first if that helps you), and be sure you can trace your code and draw stack traces.  

1.	Write a function `recursive_exponent(base, exp)` that takes in a base and an exp as parameters and recursively computes baseexp. You are not allowed to use the ** operator! 

2.	Write a function `recursive_countdown(n)` using recursion to print numbers from n to 0.  (Where n will be a positive integer parameter) 

3.	We can determine how many digits a positive integer has by repeatedly dividing by 10 (without keeping the remainder) until the number is less than 10, consisting of only 1 digit.
Write down a recursive algorithm to implement this approach, and implement it in Python. 
 (Hint:  If n is an integer, n//10 will be an integer without the fractional part in Python.)  

 
### Task 2 – Higher-Order Functions  

Write the following higher-order function in Python:

 
1.	`apply_fun_on_dict(a, myfun)`: Write a function that applies a function on the values of a dictionary (e.g., calculates power of each value). 
 
Let’s create this function that we would like to apply on the values of the dictionary: 
```
def myfun(elem): 
   return elem**2 
```
 
Then 
```
a = {'apple': 6, 'banana': 2, 'hello': 5, 'world': 4} 
applyfunondict(a, myfun)
```

Should give:
`{'apple': 36, 'banana': 4, 'hello': 25, 'world': 16} `
 
### Task 3 - Challenge task
Let's combine recursion and higher-order functions to do something a little more challenging.  

Write the following higher-order function in Python:

-	`recursive_apply_fun_on_dict(a, myfun)`: Write a function that applies a function on the values of a dictionary (e.g., calculates power of each value) if the values are integers, but if the values of the dictionary are themselves dictionaries then it applies the function on the values of that dictionary recursively.  So, for example: 

```
a = {'apple': 6, 'banana': 2, 'hello': 5, 'world': 4, 'suzanne': {'orange': 10, 'gerald': {'cat': 6}}} 
applyfunondict(a, myfun)
```

Should give:
`{'apple': 36, 'banana': 4, 'hello': 25, 'world': 16, 'suzanne': {'orange': 100, 'gerald': {'cat': 36}}} `
