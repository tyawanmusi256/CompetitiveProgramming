import sys
input = sys.stdin.readline

def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*n
    # b...可逆できる個数
    for i in range(n-1):
        b[i+1]=a[i]//10
        a[i+1]+=a[i]//10
        a[i]%=10
    # print(a)
    # print(b)
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ans[i]=a[i]//m
        if i:
            x=min(b[i],a[i]%m)
            a[i-1]+=x*10
    i=0
    # print(a)
    # print(ans)
    while i<len(a):
        if a[i]>=10:
            if i+1==len(a):
                a.append(a[i]//10)
            else:
                a[i+1]+=a[i]//10
        i+=1
    while ans[-1]==0:
        ans.pop()
        if len(ans)==0:
            ans=[0]
            break
    print(''.join(map(str,ans[::-1])))


for _ in range(int(input())):
    solve()