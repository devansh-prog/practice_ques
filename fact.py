# n=int(input("enter a number:"))
# def factn(n):
#     if n==1:
#         return 1
#     return n*factn(n-1)
# ans=str(factn(n))
# print(f"factorrial of {n} is:{ans}" )
# c=0
# for ch in ans:
#     if ch=='0':
#         c+=1
# else:
#     print("no zero found")
# print(f"number of zero in factorial of {n} is {c}")
class factorial:
    def fact(self,a):
        self.a=a
        if self.a==1:
            return 1,0
        f=a*self.fact(a-1)[0]
        x=self.count(f)
        return f,x
    def count(self,a):
        self.a=str(a)
        c=0
        for ch in self.a:
            if ch=='0':
                c+=1
        # print(f"no of zero in {a} are {c}")
        return c
calculate=factorial()
result,count=calculate.fact(5)
print(result,count)
# calculate.count(result)
