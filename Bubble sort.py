#E-Bubble sort:
t=int(input())
g=input()
l=g.split(' ')
for i in range(len(l)):
    f=False
    for j in range(len(l)-i-1): 
                
        u=int(l[j])
        v=int(l[j+1])
        if u>v:
            l[j], l[j+1]= l[j+1],l[j]
            f=True
    if f==False:
        break
for m in l:
    print(m, end=' ')
