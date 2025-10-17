sa,sb,ta,tb=map(int,input().split())
n,m,l=map(int,input().split())
s=[]
a=[]
t=[]
b=[]
for i in range(m):
    ss,aa=input().split()
    s.append(ss)
    a.append(int(aa))
for i in range(l):
    tt,bb=input().split()
    t.append(tt)
    b.append(int(bb))
ns,nt,c=[],[],[],
i,j=0,0
while 1:
    if i==m and j==l:
        break
    if i==m:
        nt.append(t[j])
        c.append(b[j])
        j+=1
    elif j==l:
        ns.append(s[i])
        c.append(a[i])
        i+=1
    elif a[i]<b[j]:
        ns.append(s[i])
        c.append(a[i])
        nt.append(t[j])
        b[j]-=a[i]
        i+=1
    elif a[i]>b[j]:
        ns.append(s[i])
        c.append(b[j])
        nt.append(t[j])
        a[i]-=b[j]
        j+=1
    else:
        ns.append(s[i])
        c.append(a[i])
        nt.append(t[j])
        i+=1
        j+=1
q=len(ns)
ans=0
for i in range(q):
    if ns[i]=="U":
        if nt[i]=="U":
            if sa==ta and sb==tb:
                ans+=c[i]
            sa-=c[i]
            ta-=c[i]
        elif nt[i]=="D":
            if sb==tb and c[i]>=(sa-ta)//2>0 and (sa-ta)%2==0:
                ans+=1
            sa-=c[i]
            tb+=c[i]
        elif nt[i]=="L":
