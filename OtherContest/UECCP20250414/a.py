s=input()
t=list("atcoder")
a=[t.index(i)for i in s]
ans=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            ans+=1
            a[i],a[j]=a[j],a[i]
print(ans)
