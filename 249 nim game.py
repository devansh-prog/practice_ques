# def letstart(n):
#     l=[x for x in range(1,n+1)]
#     turn=1
#     while l:
#         inp=int(input(f"player{turn},enter ur move between 1-3: "))
        
#         if inp < 1 or inp > 3 or inp>len(l):
#             print(f"Wrong move, must be between 1 and 3")
#             continue
        
#         l = l[inp:]
#         if not l:
#             if turn==1:
#                 print("p1 wins")
#                 return False
#             if turn==2:
#                 print("p2 wins")
#                 return True
            
       
#         turn = 2 if turn == 1 else 1
        
# result = letstart(2)
# print(result)
a=["hey"]
b=''.join(a)
x=[]
for i in b:
    x.append(i)
    
c=''.join(x[::-1])
if c==b:
    print(True)
else:
    print(False)
