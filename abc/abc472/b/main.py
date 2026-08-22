n = int(input())
l = list(map(int, input().split()))
x = sum(l)
ans = x
t = 0
for i in l:
    t += i
    ans = min(ans, abs(t-(x-t)))
print(ans)
