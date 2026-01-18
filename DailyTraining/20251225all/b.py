s=input()
if s[-1]!="8":
    print(s[:2]+str(int(s[2])+1))
else:
    print(str(int(s[0])+1)+"-1")