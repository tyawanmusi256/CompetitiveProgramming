n,m=map(int,input().split())
b=list(map(int,input().split()))
w=list(map(int,input().split()))
b.sort(reverse=1)
w.sort(reverse=1)
i=0
j=0
ans=0
while i<n or j<m:
    flag=True
    if i<n and b[i]>=0:
        ans+=b[i]
        i+=1
        continue
    if j<m and w[j]<=0:
        break
    if i>j and j<m and w[j]>=0:
        ans+=w[j]
        j+=1
        continue
    if i==j and i<n and j<m:
        if b[i]+w[j]>=0:
            ans+=b[i]+w[j]
            i+=1
            j+=1
            continue
        else:
            break
    if flag:
        break
print(ans)
