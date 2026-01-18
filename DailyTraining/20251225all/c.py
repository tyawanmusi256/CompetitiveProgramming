n=int(input())
s=set()
for _ in range(n):
    a=input()
    if not a[0] in "HDCS":
        print("No")
        exit()
    if not a[1:] in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
        print("No")
        exit()
    if a in s:
        print("No")
        exit()
    s.add(a)
print("Yes")