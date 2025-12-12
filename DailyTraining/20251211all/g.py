def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a,b,c,d=map(int,input().split())
for n in range(a,b+1):
    flag=True
    for m in range(c,d+1):
        if is_prime(n+m):
            flag=False
            break
    if flag:
        print("Takahashi")
        exit()
print("Aoki")