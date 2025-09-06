s=input()
ss="ABCABC"
q=int(input())
for _ in range(q):
    t,k=map(int,input().split())
    k-=1
    i=k>>t
    ans=s[i]
    if i==0:
        ans=0
        while k:
            ans+=1+(k & 1)
            k>>=1
            t-=1
        ans=(ans+t)%3
        print(ss[ss.index(s[0])+ans])
        continue
    for j in range(t):
        if k & (1 << j):
            if ans=="A":
                ans="C"
            elif ans=="B":
                ans="A"
            elif ans=="C":
                ans="B"
        else:
            if ans=="A":
                ans="B"
            elif ans=="B":
                ans="C"
            elif ans=="C":
                ans="A"
    print(ans)