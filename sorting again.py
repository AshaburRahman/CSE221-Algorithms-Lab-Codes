#F-Sorting again:
t=int(input())
id=input()
a=id.split(' ')
mark=input()
b=mark.split(' ')
count=0
p=[]
q=[]
for i in range(len(b)-1):
    if b[i]>b[i+1]:
        p.append(a)
        q.append(b)
    elif b[i]==b[i+1]:
        for j in range(len(a)-i-1):
            if a[j]<a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
                p.append(a)
                q.append(b)
        count+=1
    '''else:
        p.append(a[i])
        q.append(b[i])'''
print(p)
print(count)