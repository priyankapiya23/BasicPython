# #reverse  every word in sentence using method
# str=str(input("enter string:  "))
# l=len(str)
# w=str.split(" ")
# nw=[i[::-1] for i in w]
# ns=" ".join(nw)
# print(ns)

#reverse using trick
str=str(input("enter string"))
l=len(str)
for i in range(0,l-1):
    print("before reversing",str[i],end="")
    if(str[i]==' '):
        for i in range