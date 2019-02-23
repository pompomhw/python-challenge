import os
import csv

CSVpath = os.path.join('.', 'election_data.csv')

candidate=[]
#------------------------------------------------
with open(CSVpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    can_count=0
    for row in csvreader:
        candidate.append(row[2])
t_votes=len(candidate)
#--------------------------------------------------------------------------
s_cand=sorted(candidate)
e_vote=1
name=[]
votes=[]
percent=[]
k=0
for i in range(len(s_cand)-1):
    if s_cand[i] != s_cand[i+1]:
          win_percent=format(round(e_vote/t_votes*100),'.3f')
          name.append(s_cand[i])
          votes.append(e_vote)
          percent.append(win_percent)
          e_vote=1
          k+=1
    else:
         e_vote += 1
win_percent=format(round(e_vote/t_votes*100),'.3f')    
name.append(s_cand[i])
votes.append(e_vote)
percent.append(win_percent)

#----------------------------------------------------------------------------   
result={i:[j,k] for i,j,k in zip( votes,name, percent)}
s_votes=sorted(votes, reverse=True)

print(f' -------------------------')
print(f' Election Results ')
print(f' -------------------------')
print(f' Total Votes: {str(t_votes)} ')
print(f' -------------------------')
for i in s_votes:
    print(f' {str(result[i][0])} : {str(result[i][1])}%  ({str(i)}) ')
print(f' -------------------------')
print(f'  Winner : {result[max(votes)][0]}')
print(f' -------------------------')

#------------------------------------------------------------------------
csv_path = os.path.join(".", "PyPoll_stat.txt")
with open(csv_path, 'w', newline='') as csvfile:
    #csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write("   Election Results \n")
    csvfile.write('----------------------------\n')
    csvfile.write(f'Total Votes: {str(t_votes)} \n')
    for i in s_votes:
        csvfile.write(f' {str(result[i][0])} : {str(result[i][1])}%  ({str(i)}) \n')
    csvfile.write(f' -------------------------\n')
    csvfile.write(f'  Winner : {result[max(votes)][0]} \n')
    csvfile.write(f' -------------------------')

 