# PyBank



from pathlib import Path
import csv

csvpath = Path('/Users/bookz/Documents/CU_Fintech/python-homework/PyBank/budget_data.csv')

month = []
profit_losses = 0
total_months = 0
total = 0
diff_amount = 0
diff_total = 0
diff_count = 0
average_change = 0

decrease = 0
increase = 0


line_num = 0


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    

    header = next(csvreader)
    line_num +=1
   
    first_row = next(csvreader)
    '''print(first_row) - testing variable'''
    previous_month = (first_row[1])
    '''print(previous_month) testing variable value'''
    previous_month = int(previous_month)


    for row in csvreader:
        month = row[0]
        profit_losses = row[1]
        profit_losses = int(profit_losses)

        diff_amount = profit_losses - previous_month
        '''print(diff_amount) testing output of variable'''

        if decrease == 0:
            decrease = profit_losses
        
        elif profit_losses > increase:
        
            increase = profit_losses
            greatest_increase = [month,increase]

            

        elif profit_losses < decrease:
            
            decrease = profit_losses
            greatest_decrease = [month,decrease]

            
        
        total_months += 1
        total += (profit_losses)

        previous_month = profit_losses
        diff_total += diff_amount
        diff_count +=1
            

 
average_change = diff_total / diff_count 
average_change = int(average_change)   
        
print("Financial Analysis") 
print("------------------")      

print("Total Months:",total_months)

'''print("Total: $" + format(total,'.2f')) '''

print(f"Total: ${total}")
print(f"Average Change: ${average_change}")  
print(f"Greatest Increase in Profits: {greatest_increase[0]}, ${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, ${greatest_decrease[1]}")

output_path = Path('/Users/bookz/Documents/CU_Fintech/python-homework/PyBank_Output.txt')

with open(output_path, "w") as f:

        print("Financial Analysis", file=f) 
        print("------------------", file=f)      
        print("Total Months:",total_months, file=f)
        print(f"Total: ${total}",file=f)
        print(f"Average Change: ${average_change}",file=f)  
        print(f"Greatest Increase in Profits: {greatest_increase[0]}, ${greatest_increase[1]}",file=f)
        print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, ${greatest_decrease[1]}",file=f)




