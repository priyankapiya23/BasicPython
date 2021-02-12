# write first letter in lower and rest capital

a=(input("enter any string"))
a=a+" "
l=len(a)
a=a.upper()
p=0
s3=""
for i in range(0,l,1):
    if(a[i]==' '):
        s1=a[p:i]
        l1=len(s1)
        p=i+1
        s2=s1[0].lower()+s1[1:l1]
        s3=s3+s2+" "
        s2=""
print(s3)        


