dp=[10**6]*2001
ans=[(-1,-1,-1)]*2001
anss=[""]*2001
# ans[i]=(flag,x,y) x?y
# f --- -1:none, 0:root, 1:+, 2:*
dp[1],ans[1]=1,(0,0,0)
dp[11],ans[11]=2,(0,0,0)
dp[111],ans[111]=3,(0,0,0)
dp[1111],ans[1111]=4,(0,0,0)
for i in range(2,2001):
    for j in range(1,i//2+1):
        s=dp[j]
        t=dp[i-j]

        # +
        if dp[i]>dp[j]+dp[i-j]+1:
            dp[i]=dp[j]+dp[i-j]+1
            ans[i]=(1,j,i-j)
        
        if i%j:
            continue
        s=dp[j]
        t=dp[i//j]
        # *
        c=1
        if ans[j][0]==1:
            c+=2
        if ans[i//j][0]==1:
            c+=2
        if dp[i]>dp[j]+dp[i//j]+c:
            dp[i]=dp[j]+dp[i//j]+c
            ans[i]=(2,j,i//j)
n=int(input())
for i in range(1,n+1):
    flag,x,y=ans[i]
    if flag==0:
        anss[i]=str(i)
    elif flag==1:
        anss[i]=anss[x]+"+"+anss[y]
    elif flag==2:
        s=anss[x]
        t=anss[y]
        if ans[x][0]==1:
            s="("+s+")"
        if ans[y][0]==1:
            t="("+t+")"
        anss[i]=s+"*"+t
print(anss[n])