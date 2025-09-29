nums=[1,3,5,6] 
t=7
pos=None
for i in range(len(nums)):
    if nums[i]==t:
        pos=i
        break
    elif nums[i]>t:
        pos=i
        break
if pos is None:
    pos=len(nums)
    
print (pos)               

            
        