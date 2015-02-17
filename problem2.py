a = 1

b = 2

i = 3

total = 2 

while (i <= 4000000):
   
    i  = a + b
    
    if i % 2 == 0:
        
       total = total+i
    
    a = b
    
    b = i 

print (total)