n, m = map(int, input().split())
b = list(map(int, input().split()))
if len(set(b)) == 1 and b[0] == 1:
    print("No")
else:
    print("Yes")
    print(*[max(b)]*n)