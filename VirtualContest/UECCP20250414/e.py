s=input()
n=len(s)
c=[[0]*n for _ in range(10)]
x=[0]*(2**10)
x[0]+=1
for i in range(n):
    t=1
    m=0
    for j in range(10):
        c[j][i]=c[j][i-1]
        if s[i]==str(j):
            c[j][i]^=1
        m+=c[j][i]*t
        t*=2
    x[m]+=1
ans=0
for i in range(2**10):
    ans+=x[i]*(x[i]-1)//2
    #if x[i]:print(bin(i)[2:].zfill(10),x[i])
print(ans)