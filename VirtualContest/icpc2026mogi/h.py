def solve(n):
    edge=[[] for _ in range(n)]
    for i in range(n-1):
        a,b=map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    s=list(map(int,input().split()))
    sump=sum(s)&1
    parity=[i&1 for i in s]
    childp=[0]*n
    parent=[-1]*n
    stack=[0]
    for node in stack:
        tmp=0
        for mode in edge[node]:
            if mode!=parent[node]:
                tmp^=parity[mode]
                parent[mode]=node
                stack.append(mode)
        childp[node]=tmp
    edgep=0
    for i in range(n):
        if parity[i]==1:
            edgep^=childp[i]

    q=int(input())
    for _ in range(q):
        tmp=list(map(int,input().split()))
        if tmp[0]==1:
            p,r=tmp[1]-1,tmp[2]&1
            if parity[p]!=r:
                parity[p]^=1
                sump^=1
                edgep^=childp[p]
                if parent[p]!=-1:
                    edgep^=parity[parent[p]]
                    childp[parent[p]]^=1
        else:
            k=tmp[1]
            if k==0:
                print("First" if sump==1 else "Second")
            else:
                print("First" if edgep==1 else "Second")

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)