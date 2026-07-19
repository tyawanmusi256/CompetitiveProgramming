# 0で分かれたブロックが最小単位になりそう
# 111->110で111は先手有利
# 1111->0110で先手有利
# 11111->11011で先手有利
# 111111->110110で先手有利
# 1111111->0110110で先手有利
# 11111111->11011011で先手有利
# 全部先手有利やん 11だけ後手有利
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=input().replace(" ","").rstrip('\n')
    x=a.split("0")
    # print(x)
    for i in x:
        if len(i)!=2 and len(i)!=0:
            print("Alice")
            break
    else:
        print("Bob")