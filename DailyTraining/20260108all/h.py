n,m=map(int,input().split())
s=input()
t=input()
able=[False]*n
for i in range(n):
    if s[i:i+m]==t:
        for j in range(m):
            able[i+j]=True
        j=i+m
        while j<n and not able[j]:
            for k in range(1,m+1):
                if j+k>=n:
                    break
                if s[j:j+k]==t[-k:]:
                    for l in range(k):
                        able[j+l]=True
                    j+=k-1
            if able[j]:
                j+=1
            else:
                break
        j=i-1
        while j>=0 and not able[j]:
            for k in range(1,m+1):
                if s[j-k+1:j+1]==t[:k]:
                    for l in range(k):
                        able[j-l]=True
                    j-=k-1
            if able[j]:
                j-=1
            else:
                break
for i in range(n):
    if not able[i]:
        j=i
        while j<n and not able[j]:
            j+=1
        if s[i:j] in t:
            for k in range(i,j):
                able[k]=True
if all(able):
    print("Yes")
else:
    print("No")