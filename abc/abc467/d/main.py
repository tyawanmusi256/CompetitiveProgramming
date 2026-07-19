for _ in range(int(input())):
    px,py,qx,qy,rx,ry,sx,sy=map(int,input().split())
    if (px-qx)*(ry-sy)!=(py-qy)*(rx-sx):
        print("Yes")
    else:
        mx=(px+qx)-(rx+sx)
        my=(py+qy)-(ry+sy)
        if mx*(px-qx)+my*(py-qy)==0:
            print("Yes")
        else:
            print("No")