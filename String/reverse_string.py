#reverse string
string=input("enter any string")
print('reverse of string is using methhod')
print(string[::-1]) # extended slice syntax
'''Explanation : Extended slice offers to put a “step” field as [start,stop,step], and giving no field as start and stop indicates default to 0 and string length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.'''


# find in reverse 
a=str(input("enter your string"))
l=len(a)

for i in range(l-1,-1,-1):#it returns the no. of elements based on test condition minus starting position
    print(a[i],end="")
    

#print string 
b=str(input("enter your string"))
l=len(b)
for i in range(0,l,1):#it returns the no. of elements based on test condition minus starting position
    print(a[i],end="")
