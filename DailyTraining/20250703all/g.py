n=int(input())
if n==0:
    exit(print(0))
s=[]
for i in range(10**6+1):
    ng=-1
    ok=10**6+1
    while ng+1<ok:
        mid=(ng+ok)//2
        if i**3+mid*i**2+i*mid**2+mid**3>=n:
            ok=mid
        else:
            ng=mid
    s.append(i**3+ok*i**2+i*ok**2+ok**3)
print(min(s))
