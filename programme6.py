evenc=0
oddc=0
m=input().strip()
a=1
if len(m)==1:
    n=int(m)
    a=1
else:
    t=m.split()
    n=int(t[0])
    a=int(t[1])
str1=""
for i in range(n,a,-1):
    str1+=str(i)
    if i%2==0:
        evenc+=1
        if evenc%2==1:
            str1+="//"
        else:
            str1+="*"
    else:
        oddc+=1
        if oddc%2==1:
            str1+="+"
        else:
            str1+="-"
str1+=str(i-1)
res=eval(str1)
print(res)
