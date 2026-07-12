#ABC->AB->Aの順で消化で良い
#消す順番も特に考えなくて良さそうなので手前から貪欲に
for _ in range(int(input())):
    s=input()
    n=len(s)
    stack=[]
    #stackにAかABを入れる（ABCは即捨てで良い）
    #ABを持ってるときにBが来た場合、そのBを捨てずにABを捨てるで多分良い
    dead=0
    for i in s:
        if i=="A":
            stack.append(1)
        elif i=="B":
            while stack and stack[-1]!=1:
                n-=stack.pop()
            if stack:
                stack.pop()
                stack.append(2)
            else:
                while stack:
                    n-=stack.pop()
        elif i=="C":
            while stack and stack[-1]!=2:
                n-=stack.pop()
            if stack:
                stack.pop()
                n-=3
            else:
                while stack:
                    n-=stack.pop()
        else:
            while stack:
                n-=stack.pop()
    while stack:
        n-=stack.pop()
    print(n)