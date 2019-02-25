import os
import csv

#------------ Import/Read the csv dataset--------------------------
CSVpath = os.path.join('.', 'election_data.csv')
candidate=[]
with open(CSVpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    can_count=0
    for row in csvreader:
        candidate.append(row[2])
t_votes=len(candidate) # total number of votes cast

#------- create 3 lists of name, votes, and percent/ calculation -----------
s_cand=sorted(candidate)
e_vote=1  # total number of votes per each candidate
name=[]
votes=[]
percent=[]
for i in range(len(s_cand)-1):
    if s_cand[i] != s_cand[i+1]:
          win_percent=format(round(e_vote/t_votes*100),'.3f')
          name.append(s_cand[i])
          votes.append(e_vote)
          percent.append(win_percent)
          e_vote=1
    else:
         e_vote += 1
win_percent=format(round(e_vote/t_votes*100),'.3f')    
name.append(s_cand[i])
votes.append(e_vote)
percent.append(win_percent)
 
result={i:[j,k] for i,j,k in zip( votes,name, percent)} # zip the 3 variables
s_votes=sorted(votes, reverse=True)                     # sorting in the descending order

#--------- print the analysis to the terminal ---------------------------  
print(f'\n Election Results ')
print(f'----------------------------')
print(f' Total Votes: {str(t_votes)} ')
print(f'----------------------------')
for i in s_votes:
    print(f' {str(result[i][0])} : {str(result[i][1])}%  ({str(i)}) ')
print(f'----------------------------')
print(f'  Winner : {result[max(votes)][0]}')
print(f'----------------------------')

#---------- export a text file with the results ---------------------------
csv_path = os.path.join(".", "PyPoll_stat.txt")
with open(csv_path, 'w', newline='') as txtfile:
    txtfile.write("   Election Results \n")
    txtfile.write('----------------------------\n')
    txtfile.write(f' Total Votes: {str(t_votes)} \n')
    for i in s_votes:
        txtfile.write(f' {str(result[i][0])} : {str(result[i][1])}%  ({str(i)}) \n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'  Winner : {result[max(votes)][0]} \n')
    txtfile.write('----------------------------\n')
