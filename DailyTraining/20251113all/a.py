s=input()
n=len(s)
if "="*(n-2) in s and s[0]=="<" and s[-1]==">":
    print("Yes")
else:
    print("No")