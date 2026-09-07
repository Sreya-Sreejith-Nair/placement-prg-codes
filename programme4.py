#phone mapping to nokia phone
val=input()
dict={"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
arr=[""]
str1=""
if val=="":
    arr=[]
    print(arr)
else:
    i=0
    while i<len(val):
        str1=dict[val[i]]
        arr=[x+y for x in arr for y in str1]
        i+=1
    print(arr)
