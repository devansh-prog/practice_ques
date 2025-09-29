# s="helloheyheyheyhello"
# b="hey"
# for i in range(len(s)):
#     if (s[i:len(s)][:len(b)]==b):
#         print(i)
#         break
# else:
#     print(-1)
n=input("enter a no:")
b="02468"
if n[-1] in b:
    print("e")
else:
    print("odd")

