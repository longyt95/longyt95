from math import sqrt

Prime = [n for n in range(2,21) if 0 not in [n % i for i in range(2,int(sqrt(n))+1)]]

result = 1
for i in Prime:
   
    j = 1
    
    while i ** j <= 20:
        
        j =j+1
   
    result = result * i ** (j - 1)

print(result)