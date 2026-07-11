while True:
    n=int(input())
    if n==0:
        break
    s=input()
    if len(set(s))==1:
        print("IMPOSSIBLE")
    else:
        s=list(s)
        flag=False
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i]!=s[j]:
                    s[i],s[j]=s[j],s[i]
                    flag=True
                    break
            if flag:
                break
        print("".join(s))