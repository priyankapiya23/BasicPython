#s=((a+1)/2)+((a+3)/4)+........n term
a=int(input("enter the value of a="))
n=int(input("enter the value of n="))
k=0
s=0
for i in range (1,n+1,2):
    k=((a+i)/i+1)
    s=s+k
print(round(s,2))




#s=a/2+a/3+..a/n+1
a=int(input("enter the value of a="))
n=int(input("enter the value of n="))
k=0
s=0
for i in range(2,n+2):
    k=a/i
    s=s+k
print(round(s,2))



#(1) + (1*2) + (1*2*3) +.10 term

sum = 0
k=1
for i in range(1,11):
    k=k*i
    sum=sum+k
print(sum)
