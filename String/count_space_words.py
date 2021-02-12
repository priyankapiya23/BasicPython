# count the no. of space and words
A=input("Enter string")
space=0
for i in A:
      if(i==' '):
            space=space+1
print("Number of space in the string: ",space)
print("Number of words in the string: ",space+1)#words is always 1 more than space