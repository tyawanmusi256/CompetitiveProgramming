n=int(input())
ans=0
for i in range(n):
    a,b,s=input().split()
    if s=="keep":
        ans+=int(b)-int(a)
print(ans)