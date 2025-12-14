n=int(input())
login=False
ans=0
for _ in range(n):
    s=input()
    if s=="login":
        login=True
    elif s=="logout":
        login=False
    elif s=="private" and login==False:
        ans+=1
print(ans)