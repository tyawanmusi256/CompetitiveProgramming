n,k=map(int, input().split())
s=list("."+input()+".")
n+=2
for i in range(1,n-1):
    if s[i]=="o":
        k-=1
        s[i-1]="."
        s[i+1]="."
if k==0:
    for i in range(1,n-1):
        if s[i]=="?":s[i]="."
    print("".join(s[1:n-1]))
    exit()

f=False
c=[]
i=0
while i<n:
    if s[i]=="?":
        j=i
        while i<n and s[i]=="?":i+=1
        c.append(i-j)
        continue
    i+=1
flag=True
if sum((i+1)//2 for i in c)==k:flag=False
i=0
x=0
while i<n:
    if s[i]=="?":
        j=i
        while i<n and s[i]=="?":
            if flag or c[x]%2==0:
                s[i]="?"
            else:
                if (i-j)%2==0:
                    s[i]="o"
                else:
                    s[i]="."
            i+=1
        x+=1
        continue
    i+=1
print("".join(s[1:n-1]))