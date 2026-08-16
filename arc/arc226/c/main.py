#自明な上界は(h//2)*(w//2)回
#各列各行で頂点を選べる回数が(h//2)回,(w//2)回だから
#そんな簡単なことある？？？？？
#勘違いしていた 選べる頂点は長方形ではなく正方形の角
#s=1で2x2の正方形を無限に置いたらいいんじゃないんですか？
#そんな簡単なことある？？？？？
#出してみる
#落ちた
#反例わからん
#5x5のとき
# 122.1
# .2233
# 44.33
# 4455.
# 1.551
#終わった
#偶数の時はs=1で埋めて、奇数の時はこれのフラクタルのようなものを作ってみる（未証明）
for _ in range(int(input())):
    H,W=map(int,input().split())
    h,w=H,W
    if h%2==0 or w%2==0:
        print((h//2)*(w//2))
        for i in range(0,h-1,2):
            for j in range(0,w-1,2):
                print(i+1,j+1,1)
    else:
        ans=[]
        if h>w:
            for i in range(w+1,h,2):
                for j in range(0,w-1,2):
                    ans.append((i,j+1,1))
        elif h<w:
            for i in range(h+1,w,2):
                for j in range(0,h-1,2):
                    ans.append((j+1,i,1))
        h=w=min(h,w)
        d=0
        while h>=5:
            ans.append((1+d,1+d,h-1))
            for i in range(2+d,d+h-1,2):
                ans.append((i,1+d,1))
            for j in range(2+d,d+h-1,2):
                ans.append((h-1+d,j,1))
            for i in range(h-2+d,1+d,-2):
                ans.append((i,h-1+d,1))
            for j in range(h-2+d,1+d,-2):
                ans.append((1+d,j,1))
            d+=2
            h-=4
            w-=4
        if h==3:
            ans.append((1+d,1+d,1))
        #debug
        # grid=[['..']*W for _ in range(H)]
        # for id in range(len(ans)):
        #     i,j,s=ans[id]
        #     print(i,j,s)
        #     grid[i-1][j-1]=str(id).zfill(2)
        #     grid[i-1][j-1+s]=str(id).zfill(2)
        #     grid[i-1+s][j-1]=str(id).zfill(2)
        #     grid[i-1+s][j-1+s]=str(id).zfill(2)
        # for i in range(H):
        #     print(''.join(grid[i]))
        print(len(ans))
        for i,j,s in ans:
            print(i,j,s)
            
