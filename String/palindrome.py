#print palindrome

str=input("enter string")
l=len(str)
str2=''
for i in range(l-1,-1,-1):#it returns the no. of elements based on test condition minus starting position
    str2=str2+(str[i])
if(str==str2):
    print("yes")
else:
    print('no')
