n=int(input())
ans=list("-"*(n+1))
for i in range(1,10):
    if n%i==0:
        for j in range(0,n+1,n//i):
            if ans[j]=="-":
                ans[j]=str(i)
print("".join(ans))
