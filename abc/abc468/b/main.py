m,d=map(int,input().split())
s=input()
ans=0
for i in range(m):
    if not "G" in s[max(i-d,0):i+d+1]:
        ans+=1
print(ans)