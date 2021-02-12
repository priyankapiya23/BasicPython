#length of string using len method
string=input("Enter string:")
print("length of string using len method")
print(len(string))

# using for loop 
count=0
for i in string:
        count=count+1
print('length of string using for loop')
print(count)

#using while
while string[count:]:
     count=count+1
print('length of string using while loop')
print(count)