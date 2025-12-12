n=int(input())
s=input()
a=[]
cnt=1
for i in range(1,n):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        a.append((s[i-1],cnt))
        cnt=1
a.append((s[-1],cnt))
ans=0
if "/" in s:
    ans=1
for i in range(1,len(a)-1):
    if a[i][0]=="/" and a[i][1]==1:
        if a[i-1][0]=="1" and a[i+1][0]=="2":
            ans=max(ans,min(a[i-1][1],a[i+1][1])*2+1)
print(ans)