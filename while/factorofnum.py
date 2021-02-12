#factors of a number
n=eval(input("enter a number"))
f=1
print("factors of",n,"are")
while(f<=n):
    if(n%f==0):
        print(f)
    f=f+1
