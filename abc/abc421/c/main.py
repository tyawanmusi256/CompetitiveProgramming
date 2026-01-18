n=int(input())
s=input()
a,b=0,0

c=0
d=0
for i in range(2*n):
    if s[i]=="A":
        a+=abs(i-2*c)
        c+=1
    if s[i]=="B":
        b+=abs(i-2*d)
        d+=1
print(min(a,b))
