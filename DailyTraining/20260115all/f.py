a=[1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111,111111111111,1111111111111,11111111111111,111111111111111]
ans=[]
for i in a:
    for j in a:
        for k in a:
            ans.append(i+j+k)
ans=list(set(ans))
ans.sort()
# print(len(ans))
print(ans[int(input())-1])