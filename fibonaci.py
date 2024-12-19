fib = [0,1]
# Range starts from 0 by default

# In this for loop we are taking the sum last mumber and second last number in the list. 

for i in range(50):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))

