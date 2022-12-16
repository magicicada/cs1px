# Cycle 4 Lab Exercises - Functions for Data Structures and Plotting

### Objectives:

1. To get more practice devising a data structure, and writing functions to process it
2. To make use of a library (`matplotlib`), and practice various kinds of plotting

We’ll be working with a made-up dataset containing information about the production of a fictional vegetable called a poturnip (these data are fake, but their distribution and format are the same as some real agricultural data I have worked with). On each line of the file` poturnip.csv` are four pieces of information associated with a single sale of a shipment of poturnip:

```
Price/unit,Production cost/unit,Units produced nationally in month, month,region of sale
```

### Task 0: Designing your data structure

1. Look at the file` poturnip.csv`
2. Devise your own data structure to store the information in this file, and hand-write out your plan.
    1. Write out an example of how your data structure might store the information in the first three lines of the file
3. Write a function to read the information in poturnip.csv and store the information in your data structure.  

### Task 1: Breaking your own code
Now a bit of fun - try to break your file reading function!  Add a line to `poturnip.csv` that causes your reading function to throw a runtime exception.  Now, add some error-checking or an exception to your function that deals with it.

### Task 2 - Writing functions to manipulate your data structure

Write several functions to deal with information stored in your data structure:



1. Write a function `filterByRegion(dataStruct, regionString)` that takes your data structure and a string specifying a region as parameters, and returns a new data structure containing only the information for sales from the region specified by `regionString`.
2. Write a function `filterByMonth(dataStruct, month)` that takes your data structure and an argument specifying the month as parameters, and returns a new data structure containing only the information for sales from the month specified.
3. Write a function` getPricesPerUnit(dataStruct)` that takes your data structure, and returns a list of the prices/unit stored in that data structure (the first column in the file).
4. Write a function` getCostsPerUnit(dataStruct)` that takes your data structure, and returns a list of the production cost/unit stored in that data structure (the second column in the file).
5. Write a function `calculateProfitPerUnit(dataStruct)` that takes your data structure, and returns a list of the profits for the sales (the difference between the price paid and the costs).

### Task 3 - Extracting information and plotting

Use the functions you wrote as part of Task 2 and any additional bits of code you need to produce a series of plots of your data using `matplotlib`

1. Produce a scatterplot of the price paid per unit vs the cost of production per unit overall.  
2. Produce a scatterplot of the price paid per unit vs the total production in the month of sale
3. Produce histograms of the profit/unit for each region.  

### Task 4 - Stretch Exercise

We could group the months into seasons, with months 12, 1, 2 as winter, 3, 4, 5 as spring, 6, 7, 8 as summer, and 9, 10, 11 as autumn.  Write code to produce new data structures with data selected in this way, and produce box-plots for profits in each region in each season.  Can you see any difference between the seasons and regions?  