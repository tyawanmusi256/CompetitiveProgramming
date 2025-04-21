l,n1,n2=map(int,input().split())
vl1=[list(map(int,input().split())) for _ in range(n1)]+[[0,100]]
vl2=[list(map(int,input().split())) for _ in range(n2)]+[[0,100]]
i=1
j=0
ans=0
le1=vl1[0][1]
le2=0
while 1:
    if le1>=le2:
        if vl1[i-1][0]==vl2[j][0]:
            if le1>=le2+vl2[j][1]:
                ans+=vl2[j][1]
                le2+=vl2[j][1]
                j+=1
            else:
                ans+=le1-le2
                le2+=vl2[j][1]
                j+=1
        else:
            le2+=vl2[j][1]
            j+=1
    else:
        if vl1[i][0]==vl2[j-1][0]:
            if le2>=le1+vl1[i][1]:
                ans+=vl1[i][1]
                le1+=vl1[i][1]
                i+=1
            else:
                ans+=le2-le1
                le1+=vl1[i][1]
                i+=1
        else:
            le1+=vl1[i][1]
            i+=1
    if i==n1 and j==n2:break
print(ans)