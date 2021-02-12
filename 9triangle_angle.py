#take three angles and test its triangle types.
a=eval(input('enter first angle  '))
b=eval(input('enter second angle '))
c=eval(input('enter third angle  '))
if((a+b+c)<=180):
    print('TRIANGLE POSSIBLE')

    if((a<90)and (b<90) and (c<90)):
     print('ACUTE TRIANGLE')
    elif((a>90)or (b>90) or (c>90)):
     print("OBTUSE TRIANGLE")
    elif((a==90) or (b==90) or (c==90)):
     print('RIGHT ANGLE TRIANGLE')
else:
    print('TRIANGLE NOT POSSIBLE')
