for _ in range(int(input())):
    n=int(input())
    a,b,mid=0,0,0
    for i in range(n):
        x,y,z=map(int,input().split())
        if x+z<=y:
            a+=x
            b+=z
        elif min(x,y,z)==y:
            mid+=y
        else:
            a+=max(y-z,0)
            b+=max(y-x,0)
            mid+=y-max(y-x,0)-max(y-z,0)
    print(min(min(a,b)+mid, (a+b+mid)//2))