#s=((a+1)/2)+((a+3)/4)+........n term
a=int(input("enter the value of a="))
n=int(input("enter the value of n="))
k=0
s=0
for i in range (1,n+1,2):
    k=((a+i)/i+1)
    s=s+k
print(round(s,2))
