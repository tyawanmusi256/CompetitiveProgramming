n=int(input())
s=input()
ss=[[i,-1]for i in s]
q=int(input())
query=[input().split()for _ in range(q)]
flag=(-1,0)
for i in range(q):
    t,x,c=query[i]
    if t=="1":
        x=int(x)-1
        ss[x]=[c,i]
    if t=="2":
        flag=(i,1)
    if t=="3":
        flag=(i,2)
ans=[]
for i in range(n):
    c,idx=ss[i]
    if flag[0]<idx:
        ans.append(c)
    else:
        if flag[1]==1:
            ans.append(c.lower())
        elif flag[1]==2:
            ans.append(c.upper())
        else:
            ans.append(c)
print("".join(ans))