n=int(input())
ans=[]
def dfs(pre):
    if len(pre)==n:
        ans.append(pre)
        return
    flag=False
    t=max(list(pre))
    for i in "abcdefghijklmnopqrstuvwxyz":
        dfs(pre+i)
        if flag:
            return
        if i==t:
            flag=True
    return
dfs("a")
for i in ans:print(i)