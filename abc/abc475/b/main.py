n = int(input())
a = list(map(int, input().split()))
x = y = z = 0
for i in a:
    i %= 1000
    i = (1000 - i) % 1000
    x += i // 100
    y += (i % 100) // 10
    z += i % 10
print(z, y, x)
