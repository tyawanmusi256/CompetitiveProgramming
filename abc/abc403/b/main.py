t=input()
u=input()
n=len(t)
m=len(u)
for i in range(n):
    for j in range(m):
        if i+j==n:
            break
        if t[i+j]!=u[j] and t[i+j]!='?':
            break
        if j==m-1:
            print("Yes")
            exit()
print("No")