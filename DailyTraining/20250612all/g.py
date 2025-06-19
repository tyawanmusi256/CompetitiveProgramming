from collections import deque
que=deque([1])
q=int(input())
ans=1
mod=998244353
for _ in range(q):
    s=input()
    if s[0]=="1":
        x=int(s[2])
        que.append(x)
        ans=(ans*10+x)%mod
    elif s[0]=="2":
        x=que.popleft()
        ans=(ans-x*pow(10, len(que), mod))%mod
    else:
        print(ans)