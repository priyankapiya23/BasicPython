#check whether the 3 sides forms a triangle or not
a=int(input('enter first side   '))
b=int(input('enter first side   '))
c=int(input('enter first side   '))
if(a+b==c) or (b+c == a) or (c+a==b):
    print( 'NO' )
else:
    print('YES')
