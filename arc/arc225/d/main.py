# なんか一瞬で解いてる人がまばらにいる ギャグ？
# |i-Pi|の総和/2とか?
# もし各要素がゴールにたどり着くまでに回り道をしなくてもよいならこれで良い
# 623514とかで困りそう いや困らない
# 出してみる
n=int(input())
p=list(map(int,input().split()))
print(sum(abs((i+1)-p[i]) for i in range(n))//2)