#0がi個置かれたらその後ろにはi以上の値しか置けない
#先頭はかならず0、2番目は0か1
#A_i=kは必ずB_kにしか置けない
n=int(input())
a=list(map(int,input().split()))
s=sorted(set(a))
from collections import Counter
d=Counter(a)
ans=[-1]*n
able=[]
for i in range(len(s)):
    # print(d[s[i]],s[i])
    ans[s[i]]=s[i]
    able.append([s[i],d[s[i]]-1])
    if i!=len(s)-1:
        for j in range(s[i]+1,s[i+1]):
            if len(able)==0:
                print("No")
                exit()
            while able[-1][1]==0:
                able.pop()
                if len(able)==0:
                    print("No")
                    exit()
            ans[j]=able[-1][0]
            able[-1][1]-=1
            d[able[-1][0]]-=1
    d[s[i]]-=1
if ans[-1]==-1:
    idx=ans.index(-1)
    for i in s[::-1]:
        while d[i]>0:
            ans[idx]=i
            idx+=1
            d[i]-=1
if -1 in ans:
    print("No")
    exit()
print("Yes")
print(*ans)