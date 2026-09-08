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
print("c/w",end="\t")
for i in range(w):
    print(i,end="\t")
print()
for i in range(c):
    print(d[i],end="\t")
    for j in range(w):
        print(a[i][j],end="\t")
    print("")
print("Total ways",a[c-1][w-1])
