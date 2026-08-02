n=int(input())
a=list(map(int,input().split()))
print(sum(1 for i in range(1,n-1) if a[i-1]<a[i]>a[i+1]))