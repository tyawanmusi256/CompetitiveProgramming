# win/l >= p
# win - p*l >= 0
# o...1-p, x...p
n,k=map(int,input().split())
s=input()
o_counts=[0]
for i in s:
    o_counts.append(o_counts[-1]+(1 if i=="o" else 0))
ng=0
ok=1
while ok-ng>0.0000001:
    mid=(ng+ok)/2
    x=[1-mid if i == "o" else -mid for i in s]
    y=[0.0]
    for i in x:
        y.append(y[-1]+i)
    tmp=10**10
    l=0
    for r in range(1,len(y)):
        if o_counts[r]<k:
            continue
        while o_counts[r]-o_counts[l]>=k:
            tmp=min(tmp,y[l])
            l+=1
        if y[r]-tmp>=0:
            ng=mid
            break
    else:
        ok=mid
print(ok)