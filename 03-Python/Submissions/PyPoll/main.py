import csv

csvpath = r"03-Python\Instructions\PyPoll\Resources\election_data.csv"
print(csvpath)

totalVotes = 0

#candidate counts
correyCount = 0
khanCount = 0
liCount = 0
otooleyCount = 0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   
    # Read each row of data after the header
    for row in csvreader:
        
        # print(row)
        totalVotes += totalVotes + 1

        #row[0] = Voter ID
        #row[1] = County
        #row[2] = Candidate

        if row[2] == "Khan":
            khanCount += 1
        elif row[2] == "Correy":
            correyCount += 1
        elif row[2] == "Li":
            liCount += 1
        elif row[2] == "O'Tooley":
            otooleyCount += 1
        else:
            print("Candidate not found")
      
print(totalVotes)
print(f"Khan Count: {khanCount}, Li Count: {liCount}, Correy Count: {correyCount}, O'Tooley Count: {otooleyCount}")
        