import sys
input=sys.stdin.readline
for _ in range(int(input())):
    h,w=map(int,input().split())
    s=[[1 if i=="#" else -1 for i in input()]for _ in range(h)]
    if h>w:
        s=list(zip(*s))
        h,w=w,h
    x=[[0]*(h+1)for j in range(w)]
    for j in range(w):
        for i in range(h):
            x[j][i+1]=x[j][i]+s[i][j]
    # for i in s:print(i)
    ans=0
    for i1 in range(h):
        for i2 in range(i1,h):
            # print(i1,i2)
            # a[j]=x[j][i2+1]-x[j][i1]のゼロサム
            c=dict()
            c[0]=1
            t=0
            for j in range(w):
                t+=x[j][i2+1]-x[j][i1]
                # print("-",t)
                if t in c:
                    ans+=c[t]
                    c[t]+=1
                else:
                    c[t]=1
            # print("--",ans)
    print(ans)
    