#約数列挙
def divisors(n):
    divs=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divs.append(i)
            if i!=n//i:
                divs.append(n//i)
    return divs

#SがループしてたらK=1にできない
#abaabは？
#a->20210 b->02003 a->30200 a->00320 b->000005
#Sの操作そのままでK=1になる
n=int(input())
s=input()
d=sorted(divisors(n))[::-1]
for i in d:
    if s==s[:n//i]*i:
        print(i)
        print((10**6//n)*n)
        print(s*(10**6//n))
        exit()