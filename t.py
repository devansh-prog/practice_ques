a={1,2,3,4,5}
l=list(a)
n=5
for index,value in enumerate(l):
    if value==n:
        print(f"index of elemnt {n} is {index}")
        break
else:
    print("nn")
