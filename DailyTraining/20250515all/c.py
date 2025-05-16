n=int(input())
a=list(map(int,input().split()))
b=sorted(a)[::-1]
print(a.index(b[1])+1)