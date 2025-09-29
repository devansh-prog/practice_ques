l=[[1,2],[3,[4,5]],6]
b=[]
# def f(l):
#      return [item for sublist in l for item in (f(sublist) if isinstance(sublist, list) else [sublist])]
# print(f(l))
for sublist in l:
    for item in sublist:
        if isinstance(item,list):
            for innet_item in item:
                b.append(innet_item)
        else:
            b.append(item)
print(b)
