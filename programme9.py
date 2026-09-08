#longest common subsequence

#subsequences of abcd are a, ab, abc, abcd, ac, acd, ad, b, bc, bcd, bd, c, cd, d
def subsequences(n, a, index=0, current=""):
    if index == len(n):
        a.append(current)
        return
    subsequences(n, a, index + 1, current)
    subsequences(n, a, index + 1, current + n[index])

n=input().strip()
m=input().strip()
a=[]
b=[]
d={}
subsequences(n,a)
subsequences(m,b)
for i in a:
    if i in b:
        d[i]=len(i)
max_k=max(d,key=d.get)
print(max_k)
