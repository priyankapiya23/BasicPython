#take 3 sides and determine whether they forms right angle triangle or not
a=int(input('enter first side  '))
b=int(input('enter second side  '))
c=int(input('enter third side  '))
if((a*a)==(b*b)+(c*c)) or ((b*b)==(a*a)+(c*c)) or ((c*c)== (a*a)+(b*b)):
    print('yes this is right angle triangle')
else:
    print('not a right angle triangle')
