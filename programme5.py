def strongPassword(str1):
    numc=0
    Alc=0
    alc=0
    count=0
    sep=0
    for i in str1:
        if i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            alc+=1
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            numc+=1
        if i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            Alc+=1
    if alc<1:
        count+=1
    if Alc<1:
        count+=1
    if numc<1:
        count+=1
    i=0
    while(i+2<len(str1) and i+1<len(str1)):
        if str1[i]==str1[i+2] and str1[i]==str1[i+1]:
            sep+=1
        i+=1
    if sep>count:
        count=sep
    if len(str1)+count<6:
        count+=6-(len(str1)+count)
    if count+len(str1)>20:
        print("error")
    return count
val=input()
a=strongPassword(val)
print(a)
