# Cycle 3 CS1PX Lab Exercises: Reading from Files, Errors and Exceptions


## Aims:
1. Practice reading data from files
2. Practice checking for malformed input and throwing and catching exceptions


## This week’s exercises 
This week you’ll be building the biggest piece of code we’ve worked on yet - a birthday book that reads information from a file, and, if you have time to work on the last task, lets us retrieve information from the command line.  You will probably want to use IDLE or another python interpreter to work on the tasks this week.  


Resources: Chapters 13 and 19 of How to Think Like a Computing Scientist contain information on files and exceptions, and you working on file reading in CS1CT.  
 
### Task 1 - Data structure and processing
The idea of this exercise is to store people’s birthdays and produce reminders of birthdays that are coming up. 


A birthday consists of a month and a date, which can be represented by a dictionary such as
{ "month":"Sep", "day":17 }


The birthday book is a dictionary in which the keys are people’s names, and the values are birthdays, with each birthday represented as a dictionary as above. 


I want you to define a number of functions for dealing with a birthday book. Write all of this code in a file that is called birthday.py


**Task 1.1:** Set up a hard-coded sample birthday book dictionary so that you can test out the functions you will write.  Here is a sample of a dictionary that has only my birthday in it:
`birthdayBook = {Jess : {"month": "Dec", "day": 10}} `
Create your own, or add more to this one.  


**Task 1.2:** Define a function which, given a person’s name, prints his or her birthday. You function should take both the birthday book and the name as arguments.  


**Task 1.3:** Define a function which, given a month, prints a list of all the people who have birthdays in that month, with the dates.


### Task 2 -  Reading information from a file


Now we are going to read information about the birthdays from a file.  **We will add error-checking later.**


The  aim of this task is to define a function: getBirthdays which takes a filename as a parameter and reads birthdays from the file, storing them in a dictionary which should also be a parameter of the function. The first line of the function definition should therefore be


`def getBirthdays(fileName,book):`


The file should contain a number of lines with one birthday per line, in the following format:


```
John,Mar,23
Susan,Feb,16
```


and so on. 
The file `birthdays.txt` (on Moodle) contains some data that you can use for testing; you can also create your own files using the normal Python editor.  For this task, don't worry *yet* about handling errors: assume that the file exists, that it has the correct format, that every line gives a valid date, etc. 


The following points might be useful:-
* remember to open the file and then call methods to read data
* the easiest way to read data from this file is to use the readline function, but note that it gives you a string with a newline character at the end, so you will need to discard extra whitespace. You may want to look up the strip() function
* remember the `split()` function from the string module: the call `line.split(",")` will be useful. It converts a string into a list 
* Test your function (how should you do this?)


Once you have written this code to read in a file, read in the birthdays from file and try out your functions from Task 1. 


### Task 3 -  Handling errors
Now we will try to make our code more robust, and deal with malformed input files.  


In lecture we talked about both exceptions and more hand-written error checks using if statements.  Be sure to try out both in this task.  


There are many things that could go wrong in this program!  The filename might be for a file that does not exist.  The lines in a file might be missing commas, the functions you write as part of Task 1 might be given faulty input (months that don’t exist, etc).


Modify the birthday book program so that as many errors as you can think of are detected. In some cases, for example, trying to open a non-existent file, you should handle the exception raised by the built-in Python function. In other cases, you might like to process other built-in exceptions or do input checks using if statements (for example, to check for valid months, or valid dates).  Advanced option: you might even like to raise and handle your own exceptions.




### *Extra Challenge if you have time*: Task 4 - A command-line menu
The task now is to combine the functions you have implemented so far into a complete application that takes user input from the command line.


Write a program which repeatedly asks the user to enter a command, asks for further details if necessary, and carries out the corresponding operation. For example, one command could be "read";  in this case the program should ask the user to enter a filename, and then read birthdays from that file into the birthday book. There should be a textual menu with a command for each of the operations from Task 1 and 2, as well as a command "quit" which terminates the program.  


You might use a while loop to repeatedly as for input so long as the input is not ‘quit’.
