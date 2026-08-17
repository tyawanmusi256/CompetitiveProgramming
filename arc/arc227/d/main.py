n,m,q=map(int,input().split())
s=[input()for _ in range(n)]
bit0=[0]*m
bit1=[0]*m
bit00=[[0]*m for _ in range(m)]
bit01=[[0]*m for _ in range(m)]
bit10=[[0]*m for _ in range(m)]
bit11=[[0]*m for _ in range(m)]
for i in range(n):
    for j in range(m):
        if s[i][j]=="0":
            bit0[j]+=1
        else:
            bit1[j]+=1
    for j in range(m):
        for k in range(j+1,m):
            if s[i][j]=="0" and s[i][k]=="0":
                bit00[j][k]+=1
            elif s[i][j]=="0" and s[i][k]=="1":
                bit01[j][k]+=1
            elif s[i][j]=="1" and s[i][k]=="0":
                bit10[j][k]+=1
            else:
                bit11[j][k]+=1
for _ in range(q):
    t=input()
    if t in s:
        print("Yes")
        continue
    ans="Yes"
    for i in range(m):
        if t[i]=="0":
            if bit0[i]<2:
                ans="No"
                break
        else:
            if bit1[i]<2:
                ans="No"
                break
    for i in range(m):
        for j in range(i+1,m):
            if t[i]=="0" and t[j]=="0":
                if bit00[i][j]==0:
                    ans="No"
                    break
            elif t[i]=="0" and t[j]=="1":
                if bit01[i][j]==0:
                    ans="No"
                    break
            elif t[i]=="1" and t[j]=="0":
                if bit10[i][j]==0:
                    ans="No"
                    break
            else:
                if bit11[i][j]==0:
                    ans="No"
                    break
    print(ans)