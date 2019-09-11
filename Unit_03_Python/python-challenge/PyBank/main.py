import os
import csv
from pathlib import Path 

print("Financial Analysis")
print("-----------------------------------")

filepath = os.path.join('Instructions/PyBank/Resources/budget_data.csv')

#Total month
month = 0
with open(filepath, newline='') as the_file1:
    csv_reader = csv.reader(the_file1)
    csv_header = next(csv_reader)
    for row in csv_reader:
        month += 1
print(f'Total Months : {month}')

#Netloss or Profit?
total = 0
with open(filepath, newline='') as the_file2:
    csvreader = csv.reader(the_file2, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        float_profit = int(row[1])
        total += float_profit
print(f'Total: ${total}')

#Average Change
with open(filepath, newline='') as the_file3:
    csvreader = csv.reader(the_file3, delimiter=',')
    csv_header = next(csvreader)
    profit_loss = []
    months = []
    for rows in csvreader:
        profit_loss.append(int(rows[1]))
        months.append(rows[0])
    profit_loss_change = []
    for variance in range(1, len(profit_loss)):
        profit_loss_change.append((int(profit_loss[variance]) - int(profit_loss[variance-1])))
  
    #Average change calculation
    average_change = round(sum(profit_loss_change) / len(profit_loss_change),2)
    
    #Greatest increase 
    greatest_increase = max(profit_loss_change)
    #Greatest decrease 
    greatest_decrease = min(profit_loss_change)
print(f'Average Change:${average_change}')  
print(f'Greatest Increase in Profits: {months[profit_loss_change.index(max(profit_loss_change))+1]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {months[profit_loss_change.index(min(profit_loss_change))+1]} (${greatest_decrease})')

#Place to save
txt_file = Path('python-challenge/PyBank/PyBank.txt')

with open(txt_file,"w") as txtfile:
    
#Write the result in txt file 
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("-----------------------------------")
    txtfile.write("\n")
    txtfile.write(f'Total Months : {month}')
    txtfile.write("\n")
    txtfile.write(f'Total: ${total}')
    txtfile.write("\n")
    txtfile.write(f'Average Change:${average_change}')
    txtfile.write("\n")
    txtfile.write(f'Greatest Increase in Profits: {months[profit_loss_change.index(max(profit_loss_change))+1]} (${greatest_increase})')
    txtfile.write("\n")
    txtfile.write(f'Greatest Decrease in Profits: {months[profit_loss_change.index(min(profit_loss_change))+1]} (${greatest_decrease})')
