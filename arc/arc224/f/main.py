#見た目難しすぎ！！！！

#AND操作は広義単調減少、OR操作は広義単調増加
#後ろK個の総ORがMやん　そこはギャグなんか～い

#OR操作を後ろK個に割り当てた場合のxをMとして、このMを満たす操作列（のずらし方？）を数える

#後ろから考えるのが見通しが良い

#A_NにMが内包されていないならA_Nに対する操作は必ずOR
#OR操作を割り当てたのなら、A_{N-1}以降はM/A_Nについて考えるので良い

#A_NにMが内包されているならA_Nに対する操作はANDでもよい
#この時OR操作を割り当てたならあとは完全自由
#rを残りOR操作回数、残り項数をmとして、mC0+..+mCrが割り当ての数
#f(m,r)=mC0+..+mCrとして、f(m,r)からf(m-1,r)やf(m,r-1)（これは簡単）を計算したいね
#mCr=(m-1)Cr+(m-1)C(r-1)から、f(m-1,r)=(f(m,r)+(m-1)Cr)/2になるのかすげー

import sys
input=sys.stdin.readline

mod=998244353
MAX=2*10**5+5

fact=[1]*MAX
inv_fact=[1]*MAX
for i in range(1,MAX):
    fact[i]=fact[i-1]*i%mod
inv_fact[MAX-1]=pow(fact[MAX-1],mod-2,mod)
for i in range(MAX-2,-1,-1):
    inv_fact[i]=inv_fact[i+1]*(i+1)%mod

def comb(n,r):
    if n<0 or r<0 or n<r:return 0
    return fact[n]*inv_fact[r]%mod*inv_fact[n-r]%mod

class f:
    def __init__(self,n,r):
        self.n=n
        self.r=r
        self.inv2=pow(2,mod-2,mod)
        self.nowf=0
        for j in range(r+1):
            self.nowf+=comb(n,j)
            self.nowf%=mod
    #多分n,rは減る操作のみ
    def f(self,n,r):
        if n<0 or r<0:return 0
        while self.r>r:
            self.nowf-=comb(self.n,self.r)
            self.nowf%=mod
            self.r-=1
        while self.n>n:
            self.nowf=(self.nowf+comb(self.n-1,self.r))*self.inv2%mod
            self.n-=1
        return self.nowf


for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=0
    for i in range(n-k,n):m|=a[i]

    nowf=f(n,k)
    
    nowm=m
    ans=0
    for i in range(n-1,-1,-1):
        if nowm==0:
            if k>=0:
                ans+=nowf.f(i+1,k)
                ans%=mod
            break
        #A_NにMが内包されていない
        if nowm&a[i]!=nowm:
            k-=1
            nowm&=~a[i]
        #A_NにMが内包されている
        else:
            #ORを使ったら後は自由
            if k>0:
                ans+=nowf.f(i,k-1)
                ans%=mod
            #ANDを使う場合は後で計算する
        if i==0:
            if k>=0 and nowm==0:
                ans+=1
    # print("ans",ans%mod)
    print(ans%mod)
            