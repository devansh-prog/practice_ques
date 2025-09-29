nums = [2,2,1,1,1,2,2]
freq={}
for val in nums:
    if val in freq:
        freq[val]+=1
    else:
        freq[val]=1
print(freq)
largest_key = max(freq, key=freq.get)
print(largest_key)