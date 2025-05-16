
t=int(input())
for i in range(t):
    l=[]
    g=input()
    l= g.split(" ")
    m=float(l[1])
    n=float(l[3])
    p=l[2]
    ans=0
    if p=="+":
        ans=m+n
    elif p=="-":
        ans = m-n
    elif p=="*":
        ans=m*n
    elif p=="/":
        ans=m/n
    print(float(ans))
