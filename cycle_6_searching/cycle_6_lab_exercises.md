# Cycle 6 CS1PX Lab - Searching


This week you will work with the algorithms the searching algorithms we discussed in lecture.  I want you to write some new code, as well as to try to produce code that we worked on in class.  I will also ask you to try to identify bugs in a binary search implementation.  It may help to trace the operation of the code by hand, to see where it goes wrong.  




### Task 1 - Counting comparisons in linear search
1. Implement a simple linear search that takes a list and a value, and returns the index of the value if it is present in the list.  
2. Now, add a counter to your function that counts how many items in the list are compared to your target item.
3. Generate a 100-item list containing the number 0 to 99.  Then generate 100 shuffles of this list (you may with to use the random.shuffle function within the random library - look up what it does and try it out.), and use your code from (b) to count how many comparisons are used to find the item 42 in each of your shuffled lists.  What is the mean of these numbers? Is it as you expect?


### Task 2 - Finding bugs in binary search
In the file `lab_code_search.py` there are three copies of iterative binary search, each of which has a bug.  Trace each of these pieces of code, identify the bug, and fix it.  You will learn more from this exercise if you don’t look at a correct copy of binary search while doing it, and don’t compare across buggy versions until you are done.  I suggest you work on them one at a time.  You should be able to give an input to each piece of buggy code that shows the problem when you trace the operation on that input.


### Task 3 - Implementing a recursive binary search
Using your debugged version of an iterative binary search, try to produce a recursive version of binary search. You will learn more from this exercise if you don’t look at a copy of recursive binary search while doing it.  If you feel stuck, remember how we approached recursive functions in cycle 2 - what are the base cases?  What are the recursive cases? 


### Task 4 - Stretch tasks
1. Using your plotting code from last week, plot the running time of your two binary search implementations on a number of sorted lists of random numbers, both when the target is present in the list and when it is not.
2. Say we are given a list that is composed of an increasing sequence of numbers followed by a decreasing sequence.  (e.g. [1, 2, 3, 6, 29, 13, 12, 11, 6]) Can you write an adaptation of binary search that finds the index of the last number in the increasing sequence (here it would be the index of 29)?
