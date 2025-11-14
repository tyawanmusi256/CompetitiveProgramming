t="atcoder"
d={}
for i in range(len(t)):
    d[t[i]]=i
s=input()
a=[d[c] for c in s]
ans=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            ans+=1
print(ans)
