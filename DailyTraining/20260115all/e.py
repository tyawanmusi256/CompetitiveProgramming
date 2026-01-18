n,q=map(int,input().split())
s=input()
c=[0]
for i in range(n-1):
    if s[i]==s[i+1]:
        c.append(c[-1]+1)
    else:
        c.append(c[-1])
for _ in range(q):
    l,r=map(int,input().split())
    print(c[r-1]-c[l-1])