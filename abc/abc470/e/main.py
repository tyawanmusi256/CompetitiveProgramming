#作れたペアの数をXとしてスコアの期待値はX*mean(A)
#残りライフl,作成ペア数x,既知a枚からスタートして取れるペアの期待値f(l,x,a)
#ans=f(L,0,0)*mean(A)
N,L=map(int,input().split())
A=list(map(int,input().split()))

memo=[[[-1]*(N+2) for _ in range(N+1)] for _ in range(L+1)]

def f(l,x,a):
    if memo[l][x][a]!=-1:
        return memo[l][x][a]
    if l==0:
        memo[l][x][a]=0
        return 0
    if x==N:
        memo[l][x][a]=0
        return 0
    if a>=N-x:
        memo[l][x][a]=N-x
        return N-x
    #残りカードN-x種のうち、a枚が既知で、N-x-a枚が未知
    #次のカードが既知のカードである確率はa/(2(N-x)-a)
    #この時必ずペアを作れる
    #次のカードが未知のカードである確率は(2(N-x)-2a)/(2(N-x)-a)
    #この時ペアを作れる確率は1/(2(N-x)-a-1)
    #2枚目がハズレの時、既知のカードが増える確率は(2(N-x)-2a-2)/(2(N-x)-a-1)
    #2枚目に既知のカードを引いた時、確率はa/(2(N-x)-a-1)
    p=0
    if a>0:
        known=a/(2*(N-x)-a)
        p+=known*(f(l,x+1,a-1)+1)
    unknown=(2*(N-x)-2*a)/(2*(N-x)-a)
    p+=unknown*(1/(2*(N-x)-a-1)*(f(l,x+1,a)+1))
    p+=unknown*((2*(N-x)-2*a-2)/(2*(N-x)-a-1)*f(l-1,x,a+2))
    p+=unknown*(a/(2*(N-x)-a-1)*(f(l-1,x+1,a)+1 if l-1>0 else 0))
    memo[l][x][a]=p
    return p
print(f(L,0,0)*sum(A)/N)