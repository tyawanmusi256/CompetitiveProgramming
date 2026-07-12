import sys
input = sys.stdin.readline
#1e18なのにint(n**0.5)使ってごめんなさい！！
import math

for _ in range(int(input())):
    n=int(input())
    t=math.isqrt(n)
    # print(n,t**2)
    ans=(t-1)*t*2
    n-=t**2
    if n>t:
        ans+=t+t-1
        n-=t
        ans+=1
        n-=1
        ans+=n*2
    else:
        if n:
            ans+=n*2-1
    print(ans)
