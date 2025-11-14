s=input()
a=[]
for i in s:
    a.append(i)
    if len(a)>=3:
        if a[-3]=="A" and a[-2]=="B" and a[-1]=="C":
            a.pop()
            a.pop()
            a.pop()
print("".join(a))