s="abcdefghijklmnopqrstuvwxyz"
n,x=map(int,input().split())
t=""
for i in s:
    t+=i*n
print(t[x-1].upper())