#隣接スワップでの01の距離
#対応する1のindexの平均？
#110000001みたいなときは平均ではなく010000000が正しいから中央値
n=int(input())
a=input()
b=input()
c=input()
aa=[i for i in range(2*n) if a[i]=="1"]
bb=[i for i in range(2*n) if b[i]=="1"]
cc=[i for i in range(2*n) if c[i]=="1"]
ans=0
anss=["0"]*(2*n)
for i in range(n):
    id=aa[i]+bb[i]+cc[i]-min(aa[i],bb[i],cc[i])-max(aa[i],bb[i],cc[i])
    anss[id]="1"
    ans+=abs(aa[i]-id)+abs(bb[i]-id)+abs(cc[i]-id)
print(ans)
print("".join(anss))