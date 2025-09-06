s=input()
ans=0
for i in range(1,len(s)):
    ans+=26**i
for i in range(len(s)):
    ans+=(ord(s[i])-ord('A'))*(26**(len(s)-i-1))
print(ans+1)