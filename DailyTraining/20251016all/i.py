#この問題前に解いたことあったしコード残ってた
n,l,d=map(int, input().split())

#dealer[i]...dealerがy=iで終える確率
dealer=[0]*(l+d)
dealer[0]=1
tmp=1 #直近d個の和
for i in range(1,l+d):
    dealer[i]=tmp/d
    if i<l: #dealerは続ける
        tmp+=dealer[i]
    if 0<=i-d:
        tmp-=dealer[i-d]
for i in range(0,l):
    dealer[i]=0 #l未満では終えない

#win_rate[i]...playerがx=iで行動を終えたときの勝率
win_rate=[0]*(n+1)
win_rate[0]=sum(dealer[n+1:]) #dealerがbustする確率
for i in range(1,n+1):
    win_rate[i]=win_rate[i-1]+(dealer[i-1] if i-1 < l+d else 0) #dealerがi-1で終える確率を追加していけばよい

#ans[i]...x=iから行動したときの勝率
#ans[i]=max(win_rate[i],sum[j=1..d]ans[i+j]/d)
ans=[0]*(n+1)
tmp=0
for i in range(n,-1,-1):
    ans[i]=max(win_rate[i],tmp/d)
    tmp-=ans[i+d] if i+d<=n else 0
    tmp+=ans[i]
print(ans[0])


