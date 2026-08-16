#最大値の最小値はにぶたんすぎる
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    ok=0
    for i in range(m):
        ok+=a[i]*(2**i)
    ng=-1
    while ng+1<ok:
        mid=(ng+ok)//2
        #容量midがn個
        able=[0]*m
        able[m-1]=(mid>>(m-1))*n
        for bit in range(m-2,-1,-1):
            if mid&(1<<bit):
                able[bit]+=n
        can=True
        for i in range(m-1,-1,-1):
            if able[i]<a[i]:
                can=False
                break
            able[i-1]+=(able[i]-a[i])*2
        if mid==624805:
            print(able)
        if can:
            ok=mid
        else:
            ng=mid
    print(ok)