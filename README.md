# Python - Py Bank

## Background

* Inside folder added the following:

  * A file called `main.py`. This is the main script ran for analysis.
  * A "Resources" folder that contains the CSV file used. Script with correct path to the CSV file.
  * An "Analysis" folder that contains the text file that has the results from the analysis.


## PyBank

![Revenue](Images/revenue-per-lead.png)

* Created a Python script for analyzing the financial records the company. Used a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* Created Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Final analysis:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, the final script both printed the analysis to the terminal and exported a text file with the results.

