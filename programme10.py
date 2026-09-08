n=input().strip()
n=n.replace(",","")
a=[]
t=[]
i=0
while i<len(n):
    if n[i] =="(":
        b=[]
        i+=1
        while n[i] != ")":
            b.append(n[i])
            i+=1
        i+=1
        str1="("+", ".join(b)+")"
        t.append(str1)
    else:
        a.append(n[i])
        i+=1
a=sorted(a)
t=sorted(t,key=lambda x: x[1])
a.extend(t)
print(", ".join(a))
        
