a=int(input("Enter the value to reach: "))
d=list(map(int,input("Enter the denominations separated by space: ").strip().split()))
c=len(d)
w=a+1
a = [[0 for _ in range(w)] for _ in range(c)]
for i in range(w):
    a[0][i]=i
for i in range(1,c):
    a[i][0]=0
    x=int(d[i])
    for j in range (1,w):
        if x>j:
            a[i][j]=a[i-1][j]     
        else:
            a[i][j]=min(a[i-1][j],1+a[i][j-x])
print("c/w",end=" ")
for i in range(w):
    print(i,end=" ")
print()
for i in range(c):
    print(d[i],end="   ")
    for j in range(w):
        print(a[i][j],end=" ")
    print("")

print("Minimum number of coins required to reach the value =",a[c-1][w-1])
