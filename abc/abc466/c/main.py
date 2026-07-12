n=int(input())
ans=0
j=1
for i in range(n):
    j=max(j,i+1)
    while j<n:
        print("?",i+1,j+1,flush=True)
        s=input()
        if s=="Yes":
            ans+=j-i
            j+=1
        else:
            break
print("!",ans)