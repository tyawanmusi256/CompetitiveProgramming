#xが書いてあるカードの集合とyが書いてあるカードの集合が一致するとダメ
#K<=2^N

#2^Nの部分集合を1~Kに割り当てろ

for _ in range(int(input())):
    n,k=map(int,input().split())
    if 2**min(n,20)<k:
        print(-1)
        continue
    d=1
    tmp=k
    counter=[]
    while tmp:
        c=min(tmp,9*10**(d-1))
        counter.append([d,c])
        tmp-=c
        d+=1
    counter=counter[::-1]
    #counterにコスト,個数の組
    #nCr(r=0..n)個ずつ割り当てていく

    ans=0
    tmp=k
    r=0
    nCr=1

    i=0
    while tmp:
        #カードr枚使用で割り当て可能
        x=min(tmp,nCr)
        tmp-=x

        tmp2=x
        while tmp2:
            cost,cnt=counter[i]
            #costで書き込む数字のcnt
            use=min(tmp2,cnt)
            ans+=r*cost*use
            counter[i][1]-=use
            tmp2-=use
            if counter[i][1]==0:
                i+=1
        if r<n:
            nCr=nCr*(n-r)//(r+1)
            if nCr>10**6:
                nCr=10**6+1
        r+=1
    print(ans)