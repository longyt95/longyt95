from math import sqrt

def func(x):
    
    n=int(sqrt(x)+1)
    
    for i in range(2,n):
        
        if x%i==0:
            
           return 0
    
    return 1


number=600851475143

m=sqrt(number)+1

m=int(m)

result=0

for i in range(2,m):
   
    if number%i==0:
       
       if func(i)==1:
            
	  result=i

print(result)