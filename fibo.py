def fib(n):
    dp = {1:1, 2:1}
    if dp.get(n, None):
        return dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    
current_fib = {"value": 1,
               "key": 1
              }
def f(x):
    global current_fib
    if current_fib["value"] >= x:
        return current_fib["value"]
    
    i = current_fib["key"] + 1
    while True:
        num = fib(i)
        if num>=x:
            current_fib["key"] = i
            current_fib["value"] = num
            return num
        else:
            i+=1
            continue
            
l, r = input().split(" ")
s = 0
for i in range(int(l), int(r)+1):
    s+=f(i)
    
print(s)
