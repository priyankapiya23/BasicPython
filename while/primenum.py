#prime number
n=eval(input("enter a number"))
f=1
count=0
while(f<=n):
    if(n%f==0):
        count=count+1
    f=f+1
if(count==2):
    print("prime no.")
else:
    print("not a prime no.")
