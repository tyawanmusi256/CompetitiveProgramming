h,w=map(int,input().split())
s=[input() for _ in range(h)]
si,sj,gi,gj=h,w,0,0
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            si=min(si,i)
            sj=min(sj,j)
            gi=max(gi,i)
            gj=max(gj,j)
for i in range(si,gi+1):
    for j in range(sj,gj+1):
        if s[i][j]==".":
            print(i+1,j+1)
            exit()