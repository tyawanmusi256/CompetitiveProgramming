h1,w1=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(h1)]
h2,w2=map(int,input().split())
b=[list(map(int,input().split()))for _ in range(h2)]
for bit1 in range(1<<h1):
    for bit2 in range(1<<w1):
        if bin(bit1).count('1')!=h2 or bin(bit2).count('1')!=w2:
            continue
        bi=0
        flag=True
        for i in range(h1):
            if bit1>>i&1:
                bj=0
                for j in range(w1):
                    if bit2>>j&1:
                        if a[i][j]!=b[bi][bj]:
                            flag=False
                            break
                        bj+=1
                bi+=1
        if flag:
            print("Yes")
            exit()
print("No")