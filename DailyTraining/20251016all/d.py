n=int(input())
for i in range(n,1000):
    a,b,c=map(int,str(i))
    if a*b==c:
        print(i)
        break