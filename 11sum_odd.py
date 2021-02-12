#sum of odd number upto 100
sum=0
for i in range(1,100):
    if i%2!=0: # to check number is odd or not
        sum=sum+i
        print(sum)
