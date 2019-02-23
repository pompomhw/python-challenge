import os
import csv

CSVpath = os.path.join('.', 'budget_data.csv')
date=[]
profit=[]
#------------------------------------------------
with open(CSVpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

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
net_t_amt+=int(profit[length-1]) # since i am not count the last month's amt

#----------------------------------------------------------------
avg_change=round((profit[t_months-1]-profit[0])/(t_months-1),2)
#----------------------------------------------------------------

del date[0]
result={i:j for i,j in zip(diff,date)}
s_result=dict(sorted(result.items(), reverse=True))

print("Financial Analysis")
print('----------------------------')
print(f" total months   : {str(t_months)}")
print(f"net total amount: {str(net_t_amt)}")
print(f"average change  : {str(avg_change)}")
print(f"greatest increase in profit: {max(diff)}  {str(s_result[max(diff)])}")
print(f"greatest decrease in profit: {min(diff)}  {str(s_result[min(diff)])}") 

#------------------------------------------------------------------------
csv_path = os.path.join(".", "PyBank_stat.csv")
with open(csv_path, 'w', newline='') as csvfile:
    #csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write("Financial Analysis")
    csvfile.write("\n")
    csvfile.write(f'----------------------------')
    csvfile.write("\n")
    csvfile.write(f'Total Months: {str(t_months)}')
    csvfile.write("\n")
    csvfile.write(f'Total: {str(net_t_amt)}')
    csvfile.write("\n")
    csvfile.write(f'Average  Change: {str(avg_change)}')
    csvfile.write("\n")
    csvfile.write(f'Greatest Increase in Profits: {str(max(diff))}  {str(s_result[max(diff)])}')
    csvfile.write("\n")
    csvfile.write(f'Greatest Decrease in Profits: {str(min(diff))}  {str(s_result[min(diff)])}') 
