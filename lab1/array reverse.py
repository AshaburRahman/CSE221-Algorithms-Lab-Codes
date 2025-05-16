T=input()
L=T.split(" ")
N=int(L[0])
K=int(L[1])
arr=input().split()
for i in range(K):
    print(arr[K-1-i])

#D-fast sum:
t=int(input())
for i in range(t):
    n=int(input())
    sum=(n*(n+1))/2
    print(int(sum))