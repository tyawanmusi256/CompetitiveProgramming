s=list(input())
t=list(input())
n=len(s)
good=[]
bad=[]
for i in range(n):
    if s[i]!=t[i]:
        if s[i]>t[i]:
            good.append(i)
        else:
            bad.append(i)
change=good+bad[::-1]
x=[]
for i in change:
    s[i]=t[i]
    x.append("".join(s))
print(len(x))
for i in x:
    print(i)