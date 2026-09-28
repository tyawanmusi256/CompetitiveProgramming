q=int(input())
s=input()
t=input()
a=[0]*len(s)
for i in range(len(s)):
    if s[i:i+len(t)]==t:
        a[i]=a[i-1]+1
    else:
        a[i]=a[i-1]
for i in range(q):
    l,r=map(int,input().split())
    l-=1
    r-=1
    print("Yes" if a[r-len(t)+1]-(a[l-1] if l>0 else 0) else "No")