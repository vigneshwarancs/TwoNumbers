import math
T=int(input())
input_numbers=[]
for i in range(T):
    x=int(input())
    input_numbers.append(x)

def minimumSum(N):
     
    ans = math.ceil(2 * math.sqrt(N))
     
    
    print( math.trunc(ans))
for i in input_numbers:
    minimumSum(i)
