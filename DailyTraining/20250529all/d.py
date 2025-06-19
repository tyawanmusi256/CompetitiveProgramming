h,w=map(int,input().split())
ans=[0]*w
for _ in range(h):
    s=input()
    for i in range(w):
        if s[i]=="#":
            ans[i]+=1
print(*ans)