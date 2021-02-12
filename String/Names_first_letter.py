#Subhash Chandra Bose ..Print S.C.# :
#if you only write s1="."+a[i+1] then only the last value will be printed
a=str(input("enter your string"))
l=len(a)
S1=a[0]
for i in range(0,l-1,1):
    if (a[i]==' '):
        S1=S1+"."+a[i+1]
print(S1)


#my code
#print first letter of every word name
name=input("enter your name")
l=name.split()
new=""
for i in range(len(l)):
    name=l[i]
    new+=(name[0].upper()+'.')
print(new)