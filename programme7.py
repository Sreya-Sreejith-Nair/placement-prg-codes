a=int(input("Enter the maximum value to reach: "))
d=list(map(int,input("Enter the denominations separated by space: ").strip().split()))
c=len(d)
w=a+1
a = [[0 for _ in range(w)] for _ in range(c)]
for i in range(w):
    if i%2==0:
        a[0][i]=1
for i in range(c):
    a[i][0]=1
    x=int(d[i])
    for j in range (1,w):
        if x>j:
            a[i][j]=a[i-1][j]     
        else:
            a[i][j]=a[i-1][j]+a[i][j-d[i]]
print(a[c-1][w-1])
