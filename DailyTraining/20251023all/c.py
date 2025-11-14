# 3a+4ab+3b
n=int(input())
s=list(map(int,input().split()))
d=set()
for a in range(1,1000):
    for b in range(1,1000):
        d.add(3*a+4*a*b+3*b)
print(sum(not i in d for i in s))