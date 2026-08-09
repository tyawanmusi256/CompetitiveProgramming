from sortedcontainers import SortedList
n,q=map(int,input().split())
a=[0]*n
s=SortedList()
ans=0
for _ in range(q):
    query=input().split()
    if query[0]=="1":
        x=int(query[1])-1
        if a[x]==0:
            a[x]=1
            s.add((1,x))
            ans^=1
        else:
            s.discard((a[x],x))
            ans^=a[x]
            a[x]+=1
            s.add((a[x],x))
            ans^=a[x]
        print(ans)
    else:
        news=SortedList()
        ans=0
        for i,x in s:
            ans^=i-1
            a[x]-=1
            if i>1:
                news.add((i-1,x))
        s=news
        print(ans)