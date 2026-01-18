n=int(input())
s=list(input())
c=list(map(int,input().split()))
cost01_front=[0]*n
cost10_front=[0]*n
cost01_back=[0]*n
cost10_back=[0]*n
for i in range(n):
    if s[i]=="0":
        if i&1:
            cost01_front[i]=c[i]
            cost01_back[i]=c[i]
        else:
            cost10_front[i]=c[i]
            cost10_back[i]=c[i]
    else:
        if i&1:
            cost10_front[i]=c[i]
            cost10_back[i]=c[i]
        else:
            cost01_front[i]=c[i]
            cost01_back[i]=c[i]
for i in range(1,n):
    cost01_front[i]+=cost01_front[i-1]
    cost10_front[i]+=cost10_front[i-1]
    cost01_back[n-1-i]+=cost01_back[n-i]
    cost10_back[n-1-i]+=cost10_back[n-i]
ans=10**18
for i in range(n-1):
    ans=min(ans,cost01_front[i]+cost10_back[i+1],cost10_front[i]+cost01_back[i+1])
# print(cost01_front)
# print(cost10_front)
# print(cost01_back)
# print(cost10_back)
print(ans)