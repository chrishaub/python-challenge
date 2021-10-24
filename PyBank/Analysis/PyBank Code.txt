import csv
import numpy as np

path = r"03-Python\Instructions\PyBank\Resources\budget_data.csv"

print(path)

total_months = 0
total_profit = 0

isFirstRow = True
lastRowProfit = 0
changeDict = {}

# open source data
with open(path, "r") as csvPyBank:
    csvreader = csv.reader(csvPyBank, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

        total_months += 1
        total_profit += int(row[1])

        #if first row, do nothing, but set lastRowProfit
        #otherwise, get the change
        #row - last row profit
        #add to dictionary with month as key
        #update last row profit
        #continue loop

        if isFirstRow:
            lastRowProfit = int(row[1])
            isFirstRow = False
        else:
            change = int(row[1]) - lastRowProfit
            changeDict[row[0]] = change
            lastRowProfit = int(row[1])

averageChange = np.mean(list(changeDict.values()))

maxChangeMonth = max(changeDict, key=changeDict.get) #Taken from StackOverflow
maxChangeValue = changeDict[maxChangeMonth]

minChangeMonth = min(changeDict, key=changeDict.get) #Taken from StackOverflow
minChangeValue = changeDict[minChangeMonth]



summaryString = f"""Financial Analysis
------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${(round(averageChange, 2))}
Greatest Increase in Profits: {maxChangeMonth} (${maxChangeValue})
Greatest Decrease in Profits: {minChangeMonth} (${minChangeValue})
"""

#write summary string
with open("bank_results.txt", "w") as file1:
    file1.write(summaryString)
