# X=x1+(中央値)+x2とすると、B_jの挿入操作によってx1の上限とx2の下限は単調減少/下降する
# 変更後のA+Bの小さいN/2個と大きいN/2個の和でサンプルが合う
# そんなギャグでいいんですか？

n,m,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from sortedcontainers import SortedList
s=SortedList(a+b)
ans=sum(s[:n//2])+sum(s[-n//2:])
for _ in range(q):
    t,i,x=map(int,input().split())
    i-=1
    if t==1:
        c=a[i]
        a[i]=x
    else:
        c=b[i]
        b[i]=x
    # cをremove, xをadd

    if c<=s[n//2-1]:
        ans-=c
        ans+=s[n//2]
    elif c>=s[-(n//2)]:
        ans-=c
        ans+=s[-(n//2)-1]
    s.remove(c)
    
    if x<=s[n//2-1]:
        ans+=x
        ans-=s[n//2-1]
    elif x>=s[-(n//2)]:
        ans+=x
        ans-=s[-(n//2)]
    s.add(x)
    print(ans)