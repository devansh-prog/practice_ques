# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,-1,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(" ", end="")
#     for j in range(0, i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,-1,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# n=4
# s=n*n
# for i in range(1,n+1):
#     print(i,end=" ")
# print() 
# for j in range(n+1,n+2):
#     print(" "*(n+1),j)
# for j in range(n+1,n+2):
    # print()
# n=4
# num=1
# for i in range(1,n+1):
#     print(" ",i,end="")
# print()
# for j in range(n,0):
#     num+=1
#     print(" "*(n+1),j)
n=4
print("* "*n)
for i in range(n-2):
    print("* " + "  " * (n - 2) + "* ")
print("* "*n)


