#桁DPで解く
#部分列ではなく連続部分列なので助かる
#l<=k<=rのうち、sを連続部分列にもつkの個数を求める
#sを置く桁の位置を固定→桁DP

#にぶたんで解けね
#sの出現位置を固定したら、それを満たすi番目の値は簡単に求められる

def solve():
    s,l,r=input().split()
    l=int(l)
    r=int(r)
    ans=solve2(s,r)-solve2(s,l-1)
    print(ans)

def solve2(s,x):
    m=len(str(x))
    n=len(s)
    ans=0
    for i in range(m+1):
        ng=100000000000000000
        ok=-1
        while ok+1!=ng:
            mid=(ok+ng)//2
            if s[0]=="0":
                mmid=mid+10**i
            else:
                mmid=mid
            t="0000000000000000"+str(mmid)
            k=t[:len(t)-i]+str(s)+t[len(t)-i:]
            if int(k)<=x:
                ok=mid
                # print("ok",k)
            else:
                ng=mid
        ans+=ok+1
        # print(i,t,ok+1)
        if ok==-1:
            break
    return ans

for _ in range(int(input())):
    solve()