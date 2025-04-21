x=int(input())
d={}
i=0
while 1:
    d[i**5]=i
    d[-i**5]=-i
    if x-i**5 in d:
        print(i,-d[x-i**5])
        break
    if x+i**5 in d:
        print(d[x+i**5],-i)
        break
    i+=1