def solve(n):
    udfblr = []
    for i in range(n):
        udfblr.append(list(map(int, input().split())))
    # [1:x1],[x1+1:x2],[x2+1:x3],[x3+1:6*n]
    ans = 0
    for x1 in range(6*n):
        for x2 in range(x1+1, 6*n):
            for x3 in range(x2+1,6*n+1):
                tmp = [(1, x1), (x1+1, x2), (x2+1, x3)]
                for p in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
                    l1, r1 = tmp[p[0]]
                    l2, r2 = tmp[p[1]]
                    l3, r3 = tmp[p[2]]
                    l4, r4 = x3+1, 6*n
                    score = 0
                    for u, d, f, b, l, r in udfblr:
                        if l1 <= f <= r1 and l2 <= r <= r2 and l3 <= b <= r3 and l4 <= l <= r4:
                            score += 1
                            continue
                        if l1 <= r <= r1 and l2 <= b <= r2 and l3 <= l <= r3 and l4 <= f <= r4:
                            score += 1
                            continue
                        if l1 <= b <= r1 and l2 <= l <= r2 and l3 <= f <= r3 and l4 <= r <= r4:
                            score += 1
                            continue
                        if l1 <= l <= r1 and l2 <= f <= r2 and l3 <= r <= r3 and l4 <= b <= r4:
                            score += 1
                            continue

                        if l1 <= l <= r1 and l2 <= b <= r2 and l3 <= r <= r3 and l4 <= f <= r4:
                            score += 1
                            continue
                        if l1 <= f <= r1 and l2 <= l <= r2 and l3 <= b <= r3 and l4 <= r <= r4:
                            score += 1
                            continue
                        if l1 <= r <= r1 and l2 <= f <= r2 and l3 <= l <= r3 and l4 <= b <= r4:
                            score += 1
                            continue
                        if l1 <= b <= r1 and l2 <= r <= r2 and l3 <= f <= r3 and l4 <= l <= r4:
                            score += 1
                            continue

                        if l1 <= u <= r1 and l2 <= r <= r2 and l3 <= d <= r3 and l4 <= l <= r4:
                            score += 1
                            continue
                        if l1 <= r <= r1 and l2 <= d <= r2 and l3 <= l <= r3 and l4 <= u <= r4:
                            score += 1
                            continue
                        if l1 <= d <= r1 and l2 <= l <= r2 and l3 <= u <= r3 and l4 <= r <= r4:
                            score += 1
                            continue
                        if l1 <= l <= r1 and l2 <= u <= r2 and l3 <= r <= r3 and l4 <= d <= r4:
                            score += 1
                            continue

                        if l1 <= l <= r1 and l2 <= d <= r2 and l3 <= r <= r3 and l4 <= u <= r4:
                            score += 1
                            continue
                        if l1 <= u <= r1 and l2 <= l <= r2 and l3 <= d <= r3 and l4 <= r <= r4:
                            score += 1
                            continue
                        if l1 <= r <= r1 and l2 <= u <= r2 and l3 <= l <= r3 and l4 <= d <= r4:
                            score += 1
                            continue
                        if l1 <= d <= r1 and l2 <= r <= r2 and l3 <= u <= r3 and l4 <= l <= r4:
                            score += 1
                            continue
                        
                        if l1 <= u <= r1 and l2 <= b <= r2 and l3 <= d <= r3 and l4 <= f <= r4:
                            score += 1
                            continue
                        if l1 <= b <= r1 and l2 <= d <= r2 and l3 <= f <= r3 and l4 <= u <= r4:
                            score += 1
                            continue
                        if l1 <= d <= r1 and l2 <= f <= r2 and l3 <= u <= r3 and l4 <= b <= r4:
                            score += 1
                            continue
                        if l1 <= f <= r1 and l2 <= u <= r2 and l3 <= b <= r3 and l4 <= d <= r4:
                            score += 1
                            continue
                        
                        if l1 <= f <= r1 and l2 <= d <= r2 and l3 <= b <= r3 and l4 <= u <= r4:
                            score += 1
                            continue
                        if l1 <= u <= r1 and l2 <= f <= r2 and l3 <= d <= r3 and l4 <= b <= r4:
                            score += 1
                            continue
                        if l1 <= b <= r1 and l2 <= u <= r2 and l3 <= f <= r3 and l4 <= d <= r4:
                            score += 1
                            continue
                        if l1 <= d <= r1 and l2 <= b <= r2 and l3 <= u <= r3 and l4 <= f <= r4:
                            score += 1
                            continue
                    ans = max(ans, score)
    print(ans)

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)