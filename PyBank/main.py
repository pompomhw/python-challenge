import os
import csv

#------------  Import/Read the csv dataset  -------------------------------------------
CSVpath = os.path.join('.', 'budget_data.csv')
date=[]
profit=[]
with open(CSVpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

#------- create a list of diff (monthly change of profit) and calculation --------------
diff=[]
length=len(profit)
t_months=1 # since I am not counting the last month inthe for loop later
net_t_amt = 0 
for k in range(length-1):
    t_months += 1
    net_t_amt += int(profit[k])  # net total amt    
    i=k+1                        
    d_diff=profit[i]-profit[i-1]
    diff.append(d_diff)
net_t_amt+=int(profit[length-1]) # adding the last month's profit
avg_change=round((profit[t_months-1]-profit[0])/(t_months-1),2)

#--------- create a dataset with diff and date ---_________________________----------------
del date[0]
result={i:j for i,j in zip(diff,date)}
s_result=dict(sorted(result.items(), reverse=True))

#---------- print the analysis to the terminal -------------------------------------------
print("\n Financial Analysis")
print('-----------------------------------------------')
print(f"Total Months    :  {str(t_months)}")
print(f"Total           : ${str(net_t_amt)}")
print(f"Average Change  : ${str(avg_change)}")
print(f"Greatest Increase in Profits:  {str(s_result[max(diff)])}  ($ {max(diff)})  ")
print(f"Greatest Decrease in Profits:  {str(s_result[min(diff)])}  (${min(diff)})\n") 

#--------- export a text file with the results -----------------------------
csv_path = os.path.join(".", "PyBank_stat.txt")
with open(csv_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write(f'--------------------------------------------------\n')
    txtfile.write(f'Total Months   : {str(t_months)}    \n')
    txtfile.write(f'Total          : ${str(net_t_amt)}  \n')
    txtfile.write(f'Average  Change: ${str(avg_change)} \n')
    txtfile.write(f'Greatest Increase in Profits: {str(s_result[max(diff)])}  ($ {max(diff)}) \n')
    txtfile.write(f'Greatest Decrease in Profits: {str(s_result[min(diff)])}  (${min(diff)})   \n') 
