n,m,k = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(n):
    if i-m >= 0:
        c -= a[i-m]
    if c + a[i] <= k:
        c += a[i]
    else:
        a[i] = 0
for i in a:
    if i:print("Yes")
    else:print("No")
