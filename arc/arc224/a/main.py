import sys
input=sys.stdin.readline

for _ in range(int(input())):
    k=int(input())
    for i in range(1,101):
        t=i*k
        if "00" in str(t):
            print(t)
            break

