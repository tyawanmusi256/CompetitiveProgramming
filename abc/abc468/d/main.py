s=input()
n=len(s)
ans=0
for i in range(n):
    tmp=0
    cnt=0
    while 0<=i-tmp and i+tmp<n:
        if s[i-tmp]!=s[i+tmp]:
            cnt+=1
        if cnt==2:
            break
        ans+=1
        tmp+=1
for i in range(n-1):
    tmp=0
    cnt=0
    while 0<=i-tmp and i+tmp+1<n:
        if s[i-tmp]!=s[i+tmp+1]:
            cnt+=1
        if cnt==2:
            break
        ans+=1
        tmp+=1
print(ans)