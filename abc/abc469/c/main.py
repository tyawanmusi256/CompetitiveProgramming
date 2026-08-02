n=int(input())
s=input()
x=[n]*(n+1)
tmp=0
for i in range(n):
    if s[i]=="x":
        tmp+=1
        x[tmp]=i+1
for i in range(n):
    print(x[i+1])