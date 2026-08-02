n=int(input())
s=input()
if n==1:
    print(1 if s=="x" else 0)
    exit()
ans=0
for i in range(1,n-1):
    if s[i-1:i+2]=="xxx":
        ans+=1
if s[:2]=="xx":
    ans+=1
if s[-2:]=="xx":
    ans+=1
print(ans)