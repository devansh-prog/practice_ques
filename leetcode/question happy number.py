n = 23
seen = []
while n != 1 and n not in seen:
    
    seen.append(n)    
    s = 0
    temp = n
    while temp > 0:
        r = temp % 10    
        s = s + r**2     
        temp = temp // 10  
    n = s 
    # print(f"Next number: {n}")
    
if n == 1:
    print("Happy Number! 🎉")
else:
    print("Not a happy number (cycle found)")