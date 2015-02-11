from math import sqrt

def func1(x):
    
    s=str(x)
    
    n=int(len(s)/2)
    
    for i in range(0,n):
       
        if s[i]!=s[-(i+1)]:
          
           return 0
    
    return 1

def func2(x):
    
    for i in range(100,1000):
       
        if x%i==0:
           
           if x/i<1000:
                
              return 1
    
     return 0

for i in range(10000,1000000)[::-1]:
    
    if func1(i)==1:
        
       if func2(i)==1:
           
          print(i)
           
          break