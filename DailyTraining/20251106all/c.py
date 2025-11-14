n=int(input())
a=list(map(int,input().split()))
a.sort()
print(min(sum(a[:-1]),sum(a)//2))