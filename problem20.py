
from math import sqrt

answer=1

for i in range(1,101):
   
    answer=i*answer
temp=str(answer)

answer=0

n=len(temp)

for i in range(0,n):
    
    answer=int(temp[i])+answer

print(answer)