t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=1)
    if n == 1:
        print("Aoba")
    else:
        if a[0] == a[1]:
            print("Hirose")
        else:
            print("Aoba")