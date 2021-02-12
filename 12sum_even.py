#sum of even  number upto 100
sum=0
for i in range(1,101):
    if i%2==0:  # to check number is even
        sum=sum+i
print(sum)
