#length of string using len method
# string=input("Enter string:")
# #print("length of string using len method")
# # print(len(string))
# str=string.split(" ")
# print(str)
#
#
#
# #using for loop
#
# count=0
# for i in string:
#         count=count+1
# print('length of string using for loop')
# print(count)
#
#
#
# #using while
# while string[count:]:
#     count=count+1
# print('length of string using while loop')
# print(count)
#
#
# #replace e with *
# str=string.replace('e','*');
# print('replacing e with * then string will be')
# print(str)
#
# #printing words in different line
# a=input("enter your string:")
# for i in a:
#     if(i==' '):
#         print()
#     else:
#         print(i,end="")
#
#
#
#
 #reverse string
# print(string[-2])
# print('reverse of string is')
# print(string[::-1]) # extended slice syntax
# '''Explanation : Extended slice offers to put a “step” field as [start,stop,step], and giving no field as start and stop indicates default to 0 and string length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.'''
# # #capital
#
#
# find number of vowels,words,space,character
# string=input("Enter string:")
# vowels=0
# consonant=0
# space=0
# word=1
# char=0
# string=string.lower();
# for i in range(0,len(string)):
#       if string[i] in ('a','e','i','o','u'):
#             vowels=vowels+1
#       elif(string[i]>='a' and string[i]<='z'):
#           consonant=consonant+1
#       elif(string[i]==' '): #word is always one more than space
#           space=space+1
          
#       else:
#           char=char+1
# print("Number of vowels are:")
# print(vowels)
# print("Number of consonants are:")
# print(consonant)
# print("Number of words are:")
# print(space+1)
# print("Number of space are:")
# print(space)
# print("Number of characters are:")
# print(char)



#count the no. of space and words
# A=input("Enter string")
# space=0
# for i in A:
#       if(i==' '):
#             space=space+1
# print("Number of space in the string: ",space)
# print("Number of words in the string: ",space+1)#words is always 1 more than space


#find the no. of characters
# a=input("enter your string")
# char=0
# for i in a:
#     if(i!=' '):
#      char=char+1
# print("number of character in the given string is:",char)

#
#print all word in new line
# for i in string.split(' '):
#     print(i)
#
# #print short names
# name=input("enter your name")
# l=name.split()
# new=""
# for i in range(len(l)-1):
#     name=l[i]
#     new+=(name[0].upper()+'.')
# new+=l[-1].title()
# print(new)
#
#print first letter of every word name
name=input("enter your name")
l=name.split()
new=""
for i in range(len(l)):
    name=l[i]
    new+=(name[0].upper()+'.')
print(new)
#for i in string[::-1]:
   #print(i)
# find in reverse
 #   a=str(input("enter your string"))
#l=len(a)
#for i in range(l-1,-1,-1):#it returns the no. of elements based on test condition minus starting position
 #   print(a[i],end="")


#a=str(input("enter your string"))
#l=len(a)
#for i in range(1,l-1,1):#it returns the no. of elements based on test condition minus starting position
 #   print(a[i],end="")

 #Subhash Chandra Bose ..Print S.C.# :
#if you only write s1="."+a[i+1] then only the last value will be printed
a=str(input("enter your string"))
l=len(a)
S1=a[0]
for i in range(0,l-1,1):
    if (a[i]==' '):
        S1=S1+"."+a[i+1]
print(S1)

