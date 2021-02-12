#print sum of n natural number
n=eval(input('enter the value of n'   ))
sum=0
if(n>0):
    for i in range(1,n+1):
        sum=sum+i
print(sum)
