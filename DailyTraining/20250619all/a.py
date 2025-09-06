n=int(input())
s=[input()for _ in range(n)]
if s.count("For")>s.count("Against"):
    print("Yes")
else:
    print("No")