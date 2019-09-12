import os
import csv
from pathlib import Path 

print("Election Results")
print("-----------------------------------")

filepath = os.path.join('python-challenge/PyPoll/Resources/election_data.csv')

#Total Voters
voters = 0
with open(filepath, newline='') as the_file1:
    csv_reader = csv.reader(the_file1)
    csv_header = next(csv_reader)
    for row in csv_reader:
        voters += 1
    print(f'Total Votes : {voters}')

candidates = []
vote_count = []
vote_percent = []
#Candidate list
voters=0
with open(filepath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        voters += 1                 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1
    
    #Calculate percentages
    for votes in vote_count:
        percentage = (votes/voters) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        vote_percent.append(percentage)
    
    #Find the winning candidate
    winner = max(vote_count)
    index = vote_count.index(winner)
    winner = candidates[index]

print("-----------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percent[i])} ({str(vote_count[i])})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

#Place to save
txt_file = Path('python-challenge/PyPoll/PyPoll.txt')

with open(txt_file,"w") as txtfile:
    
#Write the result in txt file 
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-----------------------------------")
    txtfile.write("\n")
    txtfile.write(f'Total Votes : {voters}')
    txtfile.write("\n")
    txtfile.write("-----------------------------------")
    txtfile.write("\n")
    for i in range(len(candidates)):
        line = str(f"{candidates[i]}: {str(vote_percent[i])} ({str(vote_count[i])})")
        txtfile.write('{}\n'.format(line))
    txtfile.write("-----------------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n")
    txtfile.write("-----------------------------------")
