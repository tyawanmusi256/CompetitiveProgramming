s=input()
if len(s)<=2 and s!="oo":
    print("Yes")
    exit()
if s=="oo":
    print("No")
    exit()
if s[0]=="x":
    s=s[1:]
    if s[0]=="x":
        s=s[1:]
s+="x"*((3-len(s))%3)
if s!="oxx"*(len(s)//3):
    print("No")
else:
    print("Yes")