import sys
input = lambda:sys.stdin.readline().rstrip()

# sumAを求める +1
# A[1:i],x,A[i+1:n] から sumA[1:i],sum[i+1:n]がわかる 1分割あたり+2

n = int(input())
d = dict()
print("?", 1, flush=True)
c = int(input()) # sumA-n
leftd = dict()
rightd = dict()
suma = c + n
leftd[n] = rightd[1] = suma
d[(1, n)] = suma
stack = [(1, n)]
ans = [0] * n
for l, r in stack:
    # print("test",l,r)
    if l == r:
        if l == 1:
            ans[l-1] = leftd[1]
        elif r == n:
            ans[r-1] = rightd[n]
        else:
            ans[l-1] = leftd[l] - leftd[l-1]
        continue
    s = d[(l, r)]
    ave = s//(r-l+1)
    print("?", ave, flush=True)
    c = int(input())
    print("?", ave+1, flush=True)
    c_new = int(input())
    # c - c_new = N - 2i
    i = (n - c + c_new) // 2
    # ave と ave+1 の境目 = [l,i],[i+1,r]の境目
    # c = sumA[i+1:N] - sumA[1:i] - nx + 2ix
    # c + sumA = 2sumA[i+1:N] - nx + 2ix
    # c - sumA = - 2sumA[1:i] - nx + 2ix
    rightsum = (c + suma + n * ave - 2 * i * ave) // 2
    leftsum = (suma - c - n * ave + 2 * i * ave) // 2
    leftd[i] = leftsum
    rightd[i+1] = rightsum
    d[(l, i)] = leftd[i] - (leftd[l-1] if l > 1 else 0)
    d[(i + 1, r)] = rightd[i + 1] - (rightd[r+1] if r < n else 0)
    stack.append((l, i))
    stack.append((i + 1, r))
print("!", *ans, flush=True)


"""
19
[130312082, 192013484, 223645409, 382180561, 400420733, 524410958, 653014062, 681379133, 699653440, 759228308, 788902649, 815698901, 845020345, 861731253, 884598133, 904405586, 918394096, 928410380, 966518541]

"""