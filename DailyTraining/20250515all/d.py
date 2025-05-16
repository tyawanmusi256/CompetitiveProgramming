s=input()
ans=0
if s[0]=="o":
    s="i"+s
    ans+=1
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        ans+=1
if s[-1]=="i":
    ans+=1
print(ans)