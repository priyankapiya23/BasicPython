#printing words in different line
a=input("enter your string:")
for i in a:
    if(i==' '):
        print()
    else:
        print(i,end="")
print()

#print all word in new line using split method
b=input("enter string")
for i in b.split(' '):
     print(i)