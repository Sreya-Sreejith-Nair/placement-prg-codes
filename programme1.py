# Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit
# assignment problems before the lecture. Today he got one tricky question. The problem statement is “A
# positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of
# it after the most significant bit including the most significant bit. Print the positive integer value after toggling
# all bits”.
# Constraints :
# 1<=N<=100
# Example 1:
# Input :
# 10 
# Output :
# 5
n=int(input())
i=n
str1=""
while i>0:
    a=i%2
    i=i//2
    str1+=str(a)
str2=str1[::-1]
print(str2)
str1=""
for i in str2:
    if i=="1":
        str1+="0"
    else:
        str1+="1"
print(str1)
i=len(str1)-1
k=0
for t in str1:
    if t=="1":
        k+=2**i
    i-=1
print(k)
